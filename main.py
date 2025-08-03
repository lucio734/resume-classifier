# importa a biblioteca para ler PDF
import PyPDF2

# ferramente nltk para analisar textos
import nltk

# baixar dados
nltk.download('punkt')

# abrir pdf e extrair textos
def extract_text(pdf_path):
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ""
        for page in reader.pages:
            text += page.extract_text()
    return text.lower()

# classificação de palavras-chave
def classify_resume(text):
    if any(word in text for word in ["html", "css", "javascript"]):
        return "Front-End Developer"
    elif any(word in text for word in ["python", "pandas", "machine learning"]):
        return "Data Scientist"
    elif any(word in text for word in ["c#", "dotnet", "asp.net"]):
        return "Back-End Developer"
    else:
        return "Other"

# executar
if __name__ == "__main__":
    caminho_pdf = input("Digite o nome do PDF: ")  # Ex: curriculo.pdf
    texto = extract_text(caminho_pdf)
    categoria = classify_resume(texto)
    print(f"Categoria detectada: {categoria}")