import spacy

nlp = spacy.load("lv_core_news_sm")

text = "Valsts prezidents Egils Levits piedalījās pasākumā, ko organizēja Latvijas Universitāte."

doc = nlp(text)
for ent in doc.ents:
    print(f"Entity: {ent.text}, Type: {ent.label_}")
