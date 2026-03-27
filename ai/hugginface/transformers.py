from transformers import AutoTokenizer
import random

tokenizer = AutoTokenizer.from_pretrained("bert-base-cased")

sequence = "Using a Transformer network is simple"

tokens = tokenizer.tokenize(sequence)

ids = tokenizer.convert_tokens_to_ids(tokens)