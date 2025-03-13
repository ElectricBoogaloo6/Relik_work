import sys
import csv
import pprint
import json
import torch
device = "cuda" if torch.cuda.is_available() else "cpu"
print(f"Using {device} device")

maxInt = sys.maxsize
pp = pprint.PrettyPrinter(indent=2, width=100, depth=5, compact=False)

text = ("In ancient Roman religion and myth, Janus is the god of beginnings and gates. "
        "He has a double nature and is usually depicted as having two faces, since he looks to the future and to the past. "
        "Janus presided over the beginning and ending of conflict, and hence war and peace. "
        "The doors of his temple were open in times of war and closed during peacetime. "
        "As the god of gates, he was also associated with entering and exiting the doors of homes. "
        "Janus frequently symbolized change and transitions, such as the progress from one condition to another, from one vision to another, and the growth of young people into adulthood. "
        "Hence, Janus was worshipped at the beginning of the harvest and planting times, as well as at marriages, deaths, and other beginnings. "
        "Janus had no specialized priest assigned to him, but the high priest himself carried out his ceremonies. "
        "Janus represented the middle ground between barbarism and civilization, rural and urban space, youth and adulthood. "
        "The ancient Greeks had no equivalent to Janus, whom the Romans claimed as distinctively their own.")

model_name = "relik-ie/relik-cie-small"
corpus_name = 'meco'

while True:
    try:
        csv.field_size_limit(maxInt)
        # print(f"Successfully set field size limit to: {maxInt}")
        break
    except OverflowError:
        maxInt = int(maxInt / 10)
        # print(f"Reduced field size limit to: {maxInt}")

def safe_field_size_limit(limit):
    try:
        return csv._original_field_size_limit(limit)
    except OverflowError:
        return csv._original_field_size_limit(922337203)

csv._original_field_size_limit = csv.field_size_limit
csv.field_size_limit = safe_field_size_limit

from relik import Relik
from relik.inference.data.objects import RelikOutput

#########################################################################

if __name__ == '__main__':
    relik = Relik.from_pretrained(model_name, device="cuda", top_k=10, window_size="none") # window_size="none", window_stride=None, window_size="sentence"
    relik_out: RelikOutput = relik(text)

    print("=== Relik Output ===")
    pp.pprint(relik_out)

    # print(type(relik_out))

    model_name = model_name.replace('relik-ie/','')
    with open(f'output_{model_name}_{corpus_name}.json','w') as outfile:
        json.dump(relik_out.to_dict(), outfile, indent=4)