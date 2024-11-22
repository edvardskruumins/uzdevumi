from sklearn.feature_extraction.text import CountVectorizer
import numpy as np

text1 = "Rudens lapas ir dzeltenas un oranžas. Lapas klāj zemi un padara to krāsainu."
text2 = "Krāsainas rudens lapas krīt zemē. Lapas ir oranžas un dzeltenas."

vectorizer = CountVectorizer().fit([text1, text2])
vectors = vectorizer.transform([text1, text2]).toarray()

cosine_sim = np.dot(vectors[0], vectors[1]) / (np.linalg.norm(vectors[0]) * np.linalg.norm(vectors[1]))
print(f"Sakritības līmenis: {cosine_sim * 100:.2f}%")
