import sys
import csv
import pprint
import json
import torch
device = "cuda" if torch.cuda.is_available() else "cpu"
print(f"Using {device} device")

maxInt = sys.maxsize
pp = pprint.PrettyPrinter(indent=2, width=100, depth=5, compact=False)

text_janus = ("In ancient Roman religion and myth, Janus is the god of beginnings and gates. "
        "He has a double nature and is usually depicted as having two faces, since he looks to the future and to the past. "
        "Janus presided over the beginning and ending of conflict, and hence war and peace. "
        "The doors of his temple were open in times of war and closed during peacetime. "
        "As the god of gates, he was also associated with entering and exiting the doors of homes. "
        "Janus frequently symbolized change and transitions, such as the progress from one condition to another, from one vision to another, and the growth of young people into adulthood. "
        "Hence, Janus was worshipped at the beginning of the harvest and planting times, as well as at marriages, deaths, and other beginnings. "
        "Janus had no specialized priest assigned to him, but the high priest himself carried out his ceremonies. "
        "Janus represented the middle ground between barbarism and civilization, rural and urban space, youth and adulthood. "
        "The ancient Greeks had no equivalent to Janus, whom the Romans claimed as distinctively their own.")
        
text_shaka = ("The shaka sign, sometimes known as 'hang loose', is a gesture of friendly intent often associated with Hawaii and surf culture. " 
        "The gesture is made by extending the thumb and smallest finger while holding the three middle fingers curled and gesturing in salutation while presenting the front or back of the hand; the hand maybe rotated back and forth for emphasis." 
        "The shaka sign was adopted from local Hawaiian culture and customs by visiting surfers in the 1960s, and its use has spread around the world." 
        "It is primarily used as a greeting gesture or to express thanks, acknowledgement, or even praise from one individual to another." 
        "Residents of Hawaii use the shaka to convey the 'Aloha Spirit': a concept of friendship, understanding, compassion, and solidarity among the various ethnic cultures that reside in Hawaii." 
        "While the exact origin of the sign is unclear, some have suggested its origin was derived from Spanish immigrants, who folded their middle fingers and took their thumbs to their lips as a friendly gesture to represent sharing a drink with the natives they met in Hawaii.")
        
text_doping = ("In competitive sports, doping is the use of banned performance-enhancing drugs by athletic competitors. "
        "The term doping is widely used by organizations which regulate sporting competitions. "
        "The use of drugs to enhance performance is largely considered unethical, and is therefore prohibited by most international sports organizations, including the International Olympic Committee. "
        "Furthermore, athletes who take explicit measures to evade detection exacerbate the ethical violation with overt deception and cheating. "
        "Despite its prevalence in the headlines recently, doping is not a new phenomenon; in fact, it is as old as sport itself. "
        "From the use of substances in ancient chariot races to more recent controversies in baseball and cycling, popular views among athletes have varied widely over the years. "
        "In recent decades, authorities and sporting organizations have tried to strictly regulate the use of drugs in sport. "
        "The primary reasons for this ban are the health risks of performance-enhancing drugs, the equality of opportunity for athletes, and the positive example to the public set by drug-free sport. "
        "Anti-doping authorities have repeatedly emphasized that using performance-enhancing drugs goes against the spirit of sport.")
        
text_thylacine = ("The thylacine was the largest known carnivorous marsupial of modern times. "
      "It is commonly known as the Tasmanian tiger because of its striped lower back, or the Tasmanian wolf because of its canine-like appearance, traits and attributes. "
      "Native to continental Australia, Tasmania, and New Guinea, it is believed to have become extinct in the twentieth century. "
      "The thylacine was one of only two marsupials to have a pouch in both sexes. "
      "The male had a pouch that protected the external reproductive organs while running through thick brush. "
      "The thylacine has been described as a formidable predator because of its ability to survive and hunt prey in extremely sparsely populated areas. "
      "The thylacine had become extremely rare or extinct on the Australian mainland before British settlement of the continent, but it survived on the island of Tasmania. "
      "Intensive hunting encouraged by bounties is generally blamed for its extinction, but other contributing factors may have included disease, the introduction of dogs, and human encroachment into its habitat. "
      "Despite its official classification as extinct, sightings are still reported, though none have been conclusively proven.")
      
text_WED = ("World Environment Day (WED) is celebrated on the fifth of June every year and is the United Nation\'s principal vehicle for encouraging awareness and action for the protection of the environment. "
       "First held in 1974, it has been a flagship campaign for raising awareness on emerging environmental issues from marine pollution, human overpopulation, and global warming. "
       "WED has grown to become a global platform for public outreach, with participation from over one hundred countries annually. "
       "Each year, WED chooses a new theme that major corporations, non-governmental organizations, communities, governments and celebrities worldwide adopt to advocate environmental causes. "
       "For example, the theme for 2018 is Beat Plastic Pollution. "
       "The goal is to encourage people to change their everyday habits in ways which can reduce plastic pollution. "
       "Specifically, the campaign hopes to reduce the prevalence of single-use or disposable plastic items, as they have severe environmental consequences. "
       "In response to this campaign, the Indian government has pledged to eliminate all single-use plastic in India by 2022.")

text_monocle = ("A monocle is a type of corrective lens used to correct or enhance the vision in only one eye. "
       "It consists of a circular lens, generally with a wire ring around the circumference that can be attached to a string or wire. "
       "The other end of the string is then connected to the wearer's clothing to avoid losing the monocle. "
       "During the late nineteenth century, the monocle was generally associated with wealthy, upper-class men. "
       "Combined with a long coat and a top hat, the monocle completed the costume of the stereotypical late nineteenth century capitalist. "
       "Monocles were also accessories of military officers from this period. "
       "Despite their prevalence in the late nineteenth century, monocles are rarely worn today. "
       "This is due in large part to advances in optometry, which allow for better measurement of refractive error, so that glasses and contact lenses can be prescribed with different strengths in each eye.")
       
text_wine = ("Wine tasting is the sensory examination and evaluation of wine. "
      "While the practice of wine tasting is as ancient as its production, a more formalized methodology has slowly become established from the late middle ages onwards. "
      "Modern, professional wine tasters use a constantly evolving specialized terminology which is used to describe the range of perceived flavors, aromas and general characteristics of a wine. "
      "In recent years, results challenging the reliability of wine tasting in both experts and consumers have surfaced. "
      "For example, studies showed that people expect more expensive wine to have more desirable characteristics than less expensive wine: When tasters are given wine that they are falsely told is expensive they virtually always report it as tasting better than the very same wine when they are told that it is inexpensive. "
      "Other studies show that tasters' judgment can be prejudiced by knowing details of a wine, such as geographic origin, reputation, or other considerations. Objective wine tasting therefore requires the wine to be served blind – that is, without the taster having seen the label or bottle shape. "
      "Blind tasting may also involve serving the wine from a black wine glass to mask the color of the wine.")
      
text_orange = ("Orange juice is a liquid extract of the orange tree fruit, produced by squeezing oranges. "
      "Commercial orange juice with a long shelf life is made by pasteurizing the juice and removing the oxygen from it. "
      "This removes much of the taste, necessitating the later addition of a flavor pack, generally made from orange products. "
      "Additionally, some juice is further processed by drying and later rehydrating the juice, or by concentrating the juice and later adding water to the concentrate. "
      "The health value of orange juice is debatable: it has a high concentration of vitamin C, but also a very high concentration of simple sugars, comparable to soft drinks. "
      "As a result, some government nutritional advice has been adjusted to encourage substitution of orange juice with raw fruit, which is digested more slowly, and limit daily consumption.")
      
text_beekeeping = ("Beekeeping is the maintenance of bee colonies by humans, typically with the use of man-made hives. "
      "The species most commonly used in bee colonies are honey bees. "
      "A beekeeper maintains these colonies in order to collect the honey and other products that the hive produces (such as beeswax), but also to pollinate crops, or to produce bees for sale to other beekeepers. "
      "The domestication of bees is depicted in Egyptian art from over four thousand years ago. "
      "Back then, simple hives and smoke were used for beekeeping, and honey was stored in jars – some of which were found in the tombs of pharaohs. "
      "This process was largely unchanged until the eighteenth century, when an improved understanding of the biology of bees led to the invention of the moveable comb hive in Europe, allowing honey to be harvested without destroying the entire colony. "
      "Today, some beekeepers believe that the more stings a beekeeper receives, the less irritation each one causes, and it is considered important for the safety of the beekeeper to be stung a few times a season. "
      "Indeed, recent studies found that beekeepers have high levels of antibodies that react to the major antigen of bee venom.")
      
text_flag = ("A national flag is a flag which represents and symbolizes a country. "
      "The national flag is usually flown by the government of a country, but it can also be flown by its citizens. "
      "A national flag is designed with specific meanings for its colours and symbols. "
      "Historically, flags originated as military standards, which were used as signs on the battlefield. "
      "The practice of flying national flags outside of the context of warfare only became common in the early seventeenth century. "
      "A country's constitution will often describe the national flag. "
      "All national flags are rectangular, except for the flag of Nepal, which uses a unique triangular shape. "
      "The ratios of height to width vary among standard rectangular flags, but none is taller than it is wide. "
      "The flags of Switzerland and the Vatican City are the only national flags which are exact squares. "
      "The most popular colours used for national flags are red, white, green, and blue. "
      "Although the national flag is meant to be a unique symbol for the country it represents, many flags have very similar colours and designs.")
      
text_international = ("'The International Union for Conservation of Nature is an international organization working in the field of nature conservation and the sustainable use of natural resources. "
      "It is involved in data gathering and analysis, research, field projects, advocacy, and education. "
      "Its mission is to influence, encourage and assist societies throughout the world to conserve nature and to ensure that any use of natural resources is equitable and ecologically sustainable. "
      "Over the past decades, the organization has widened its focus beyond conservation ecology and now incorporates issues related to sustainable development in its projects. "
      "Unlike many other international environmental organizations, it does not aim to mobilize the public in support of nature conservation. "
      "Instead, the organization tries to influence the actions of governments, business and other stakeholders by providing information and advice, and through building partnerships. "
      "The organization is best known to the wider public for compiling and publishing the 'Red List of Threatened Species', which assesses the conservation status of species worldwide. "
      "Today, the organization employs approximately one thousand full-time staff in more than fifty countries.'")
      
text_vehicle = ("A vehicle registration plate is a metal or plastic plate attached to a vehicle for official identification purposes. "
      "All countries require registration plates for road vehicles such as cars, trucks, and motorcycles. "
      "Whether they are required for other vehicles, such as bicycles, boats, or tractors, may vary by jurisdiction. "
      "The registration identifier is a series of letters and digits that uniquely identifies the vehicle owner within the issuing region's vehicle register. "
      "In some countries, the identifier is unique within the entire country, while in others it is unique within a state or province. "
      "France was the first country to introduce the registration plate, in the late nineteenth century. "
      "Early twentieth century plates varied in size and shape from one jurisdiction to the next, such that if a person moved, new holes would need to be drilled into the automobile to support the new plate. "
      "Standardization of plates came in the late fifties, when automobile manufacturers came to an agreement with governments and international organizations.")
      


word_split = text_vehicle.split()
word_count = len(word_split)
print(f"Word count: {word_count}")

model_name_full = "relik-ie/relik-cie-small"
model_name = model_name_full.replace('relik-ie/', '')
corpus_name = 'vehicle'
threshold = '0.1'


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

window_sizes = [128] #128, 256, 'sentence', 'none'

if __name__ == '__main__':
    for win_size in window_sizes:
        model_window_size = "none" if win_size == "None" else win_size
        # Initialize the model with the current window size
        #relik = Relik.from_pretrained(model_name_full, device="cuda", top_k=10, window_size=model_window_size)
        #relik_out: RelikOutput = relik(text)

        # Construct output file name
        #output_filename = f'output_{model_name}_{corpus_name}_{threshold}_{win_size}.json'
        #with open(output_filename, 'w') as outfile:
            #json.dump(relik_out.to_dict(), outfile, indent=4)
            
        for i in range(1, len(word_split)+1):
          pre_word = " ".join(word_split[:i])
          relik = Relik.from_pretrained(model_name_full, device="cuda", top_k=10, window_size=model_window_size)
          relik_out: RelikOutput = relik(pre_word)


          print("=== Relik Output ===")
          pp.pprint(relik_out)


          with open(f"output_step_{i:03d}_{model_name}_{corpus_name}_{threshold}_{win_size}.json", "w") as f:
              json.dump(relik_out.to_dict(), f, indent=4)