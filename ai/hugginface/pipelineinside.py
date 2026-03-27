# FULL WORKFLOW
from transformers import AutoTokenizer
from transformers import AutoModelForSequenceClassification
import torch 


raw_inputs = [
    "I've been waiting for a HuggingFace course my whole life.",
    "I hate this so much!",
]

checkpoint = "distilbert-base-uncased-finetuned-sst-2-english"
tokenizer = AutoTokenizer.from_pretrained(checkpoint)

inputs = tokenizer(raw_inputs, padding=True, truncation=True, return_tensors="pt")

print(inputs)

# from transformers import AutoModel

# checkpoint = "distilbert-base-uncased-finetuned-sst-2-english"
# model = AutoModel.from_pretrained(checkpoint)

# outputs = model(**inputs)



checkpoint = "distilbert-base-uncased-finetuned-sst-2-english"
model = AutoModelForSequenceClassification.from_pretrained(checkpoint)
outputs = model(**inputs)

predictions = torch.nn.functional.softmax(outputs.logits, dim=-1)
print(predictions)

 
print("outputs")
print(outputs)

print("predictions")
print(predictions)

print("labels")
print(model.config.id2label)

