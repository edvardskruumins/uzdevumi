import re

text = "@John: Šis ir lielisks produkts!!! Vai ne? 👏👏👏 http://example.com"

cleaned_text = re.sub(r'[@#\*\.\(\\)]', '', text)
cleaned_text = re.sub(r'http[^\s]+', '', cleaned_text) 

print(cleaned_text)
