import requests

url = "https://abrdn.kurtosysweb.com/pdfs/F_STD_it-IT-NN_LU0779217537.pdf"  # URL del file da scaricare


# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
#     "(KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
# }


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                  '(KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
    'Accept': 'application/pdf',
    'Referer': 'https://abrdn.kurtosysweb.com/',  
}

session = requests.Session()
session.headers.update(headers)

response = session.get(url, headers=headers, stream=True)

# response = requests.get(url, headers=headers, stream=True)


if response.status_code == 200:
    with open("file.zip", "wb") as f:
        for chunk in response.iter_content(chunk_size=8192):
            if chunk:  # evita blocchi vuoti
                f.write(chunk)
    print("Download completato con successo.")
else:
    print(f"Errore nel download: {response.status_code}")
