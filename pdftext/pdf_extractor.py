import re
import fitz  # PyMuPDF


class PDFExtractor:
    def __init__(self, rules):
        """
        rules: dict con chiave = nome campo, valore = dict con:
            - 'pattern': regex da cercare
            - 'type': funzione di conversione (float, int, str)
        """
        self.rules = rules

    def extract_text(self, pdf_path):
        doc = fitz.open(pdf_path)
        text = ""
        for page in doc:
            text += page.get_text("text")
        return text

    def parse(self, text):
        results = {}
        for field, rule in self.rules.items():
            match = re.search(rule["pattern"], text, re.IGNORECASE)
            if match:
                # prendo il primo gruppo non None
                value = next((g for g in match.groups() if g), None)
                if value:
                    try:
                        results[field] = rule["type"](value.replace(",", "."))
                    except Exception:
                        results[field] = value
        return results

    def extract(self, pdf_path):
        text = self.extract_text(pdf_path)
        return self.parse(text), text


# 🔧 Definizione regole
example_rules = {"vcc": {"pattern": r"(?:vcc\s*([\d,.]+)", "type": float}}
