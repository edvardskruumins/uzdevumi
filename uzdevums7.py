import spacy

nlp = spacy.load("lv_core_news_sm")

words = ["māja", "dzīvoklis", "jūra"]

word_vectors = [nlp(word).vector for word in words]

similarity = nlp("māja").similarity(nlp("dzīvoklis"))
print(f"Līdzība starp 'māja' un 'dzīvoklis': {similarity}")
