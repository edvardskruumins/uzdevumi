from transformers import pipeline

starter = "Reiz kādā tālā zemē..."

generator = pipeline("text-generation", model="gpt-2")
generated_text = generator(starter, max_length=50, num_return_sequences=1)

print(generated_text[0]['generated_text'])
