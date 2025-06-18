# Incremental triple extraction with **Relik**

This repo runs the *Relik* model in a continuous-incremental extractor on a corpus and stores triple additions, deletions and full outputs after **every word** in the text.

* Model source <https://github.com/SapienzaNLP/relik>  
* Corpus source <https://osf.io/srdhm>  
* Compute VU **BAZIS** HPC -­ <https://vu.nl/en/research/portal/research-impact-support-portal/high-performance-research-computing>

---

## Repository layout

| Path / file | What it holds |
| ------------| ------------- |
| **all_outputs/** | Final CSVs for each *model size × corpus text*<br>• `additions_*` – only new triples<br>• `deletions_*` – triples that disappeared<br>• `full_*` – whole triple set after every step |
| **model_test_runs/** | Test CSVs created with several **window_size** settings |
| **threshold_window_size_tests/** | Test CSVs created with several **threshold** settings |
| **step_outputs.7z** | JSON output for *every* incremental step (one file per word per text) |
| **code_for_BAZIS.py** | Python file that produces the step-level JSON files |
| **relik_test_batch.sh** | Bash script that queues `code_for_BAZIS.py` on the BAZIS cluster |
| **compile_relik.ipynb** | Notebook that converts the JSONs into the three (additions, deletions and full) CSVs |
| **check_outputs.ipynb** | Visualisation of any additions / deletions / full CSVs |
| **corpus_tests.ipynb** | Notebook that prints the corpus texts for easy reading |
| **corpus.csv** | All texts (Janus, Shaka, Doping, Thylacine, WED, Monocle, Wine, Orange, Beekeeping, Flag, International, Vehicle) in one file |

---

## File-naming pattern
* **model** is one of `relik-cie-small`, `relik-cie-large`, `relik-cie-xl`  
* **corpus** is one of the 12 text names above

Example: `additions_relik-cie-large_beekeeping.csv`

## How the CSV looks

Every CSV produced by the notebooks and scripts has the columns:

| Column | Meaning |
| ------ | ------- |
| `text_type` | Name of the corpus text |
| `output_step` | Word index |
| `current_word` | The word that triggered this output |
| `current_text` | Full text up to `current_word` |
| `new_triplets` | Triples just added at this step (JSON list) |
| `total_triplets` | Complete triple set present after this step |
| `triplet_scores` | Relik scores for `new_triplets`  |

---

