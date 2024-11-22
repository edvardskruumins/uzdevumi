import re

# Neapstrādāts teksts
text = "@John: Šis ir lielisks produkts!!! Vai ne? 👏👏👏 http://example.com"

# Noņem simbolus un pārveido uz mazajiem burtiem
cleaned_text = re.sub(r'[@#\*\.\(\\)]', '', text)  # Noņem īpašos simbolus
cleaned_text = re.sub(r'http[^\s]+', '', cleaned_text)  # Noņem URL

print(cleaned_text)
