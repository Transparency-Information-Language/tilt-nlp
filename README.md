# tilt-nlp
Experimental Natural Language Processing on Privacy Policies for Import to Transparency Information Language

## Overview
- `jupyter notebook NER_NLTK_Spacy - Privacy Policies.ipynb`  **main experiments**
- academy.dslrvideoshooter.com.txt/ **serialized output of policy**
- arstechnica.com.txt/ **serialized output of policy**
- academymortgage.com.txt/ **serialized output of policy**
---
- language detection.png **Screenshot of notebook for lang detection**
- langs.json **Results of language detection**
- dist.png **Distribution of languages**
---
- syntax-tree-visualizer.py **Syntax tree visualizer standalone**
- single-tree.svg **Examplary syntax tree**
- single-tree.pdf **Examplary syntax tree**
---
- media/ **archived main experiments and drafts**

## Author
Elias Grünewald

## License
[MIT License](LICENSE)


---

# Research Agenda
## Problem
-   users have certain rights as transparency information but are not able to conceive them
-   if data is transferred to multiple parties, the resulting network is not visible
-   lack of transparency information describing representation format

## Research questions
-   how should a transparency representation format look like?
-   how to automatically extract transparency information?
-   how to extract data flow networks?

## Sketched solution process
1.  define transparency representation format
2.  make use of existing corpora
    -   **Privacy Policies** e.g. OPP-115 Corpus
    -   **Transparency information key words or categories** list of
        (sensitive) personal data terms such as name, birthday, bank
        account details, picture, IP address…
    -   **Third parties** list of top *N* companies, institutions
3.  use NLP for semantics extraction (link each transparency key word to
    third party e.g. by distance)
4.  save *n*-tuples (incl. purpose, duration) to previously defined
    representation format
5.  visualize data flow networks

## Implementation
-   may extend Polisis framework
-   transparency representation is defined as json example/schema
-   make use of established NLP framework such as TensorFlow, PyTorch, Google Natural Language API, Amazon Comprehend
-   common web technologies for visualization

## Evaluation
-   try unseen privacy policies for precision, recall, F1-score
-   measure performance
