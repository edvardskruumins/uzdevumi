import re

text = "@John: Šis ir lielisks produkts!!! Vai ne? 👏👏👏 http://example.com"

cleaned_text = re.sub(r'[@!#\*\.\?\(\\)]', '', text)
cleaned_text = re.sub(r'http[^\s]+', '', cleaned_text)
cleaned_text = cleaned_text.lower()

print(cleaned_text)
