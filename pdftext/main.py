from pdf_extractor import PDFExtractor


if __name__ == "__main__":
    rules = {
        "TOTALE_DOCUMENTO": {
            "pattern": r"(?:TOTALE DOCUMENTO\s*([\d,.]+))",
            "type": float,
        },
    }

    extractor = PDFExtractor(rules)
    data, text = extractor.extract("./files/fattura.pdf")
    print("-" * 78)
    print(data)
    print("-" * 78)
    print(text)
