import spacy
from spacy import displacy

# Load English core model
nlp = spacy.load("en_core_web_sm")

# Load policies from local file
f = open("../policy_pages_873/929nin.com.txt", "r")
doc = f.read()

# Apply NLP with the en_core model
doc = nlp(doc)

# Extract annotated sentences
sentence_spans = list(doc.sents) # [1] <- limit sentences if necessary

# Display the setence analyses per sentence as svg tree, served via localhost:5000 
displacy.serve(sentence_spans,
	style="dep",
	options={ "compact": True, "bg": "#fff", "color": "black", "font": "Palatino"})
# alternative serve(doc, ...) compact: False