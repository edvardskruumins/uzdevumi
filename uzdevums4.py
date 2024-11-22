from textblob import TextBlob

sentences = [
    "Šis produkts ir lielisks, esmu ļoti apmierināts!",
    "Esmu vīlies, produkts neatbilst aprakstam.",
    "Neitrāls produkts, nekas īpašs."
]

for sentence in sentences:
    blob = TextBlob(sentence)
    sentiment = "Pozitīvs" if blob.sentiment.polarity > 0 else "Negatīvs" if blob.sentiment.polarity < 0 else "Neitrāls"
    print(f"Teikums: {sentence} -> Noskaņojums: {sentiment}")
