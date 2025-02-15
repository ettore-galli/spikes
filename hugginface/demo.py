import gradio as gr
from transformers import pipeline

# Carica il modello
generator = pipeline('text-generation', model='gpt2')

# Definisci la funzione che utilizza il modello
def generate_text(prompt):
    output = generator(prompt, max_length=50, num_return_sequences=1)
    return output[0]['generated_text']

# Crea l'interfaccia Gradio
iface = gr.Interface(fn=generate_text, inputs="text", outputs="text")

# Avvia l'interfaccia
iface.launch()