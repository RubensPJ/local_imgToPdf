import os
from PIL import Image
from reportlab.pdfgen import canvas

def extract_number(filename):
    """
    Extrai números de um nome de arquivo e retorna como um inteiro.
    Retorna None se nenhum número for encontrado.
    """
    numbers = ''.join(filter(str.isdigit, filename))
    return int(numbers) if numbers.isdigit() else None

def create_pdf(image_files, output_filename='output.pdf'):
    """
    Cria um PDF a partir de uma lista de arquivos de imagem.
    """
    c = canvas.Canvas(output_filename)
    for image_file in image_files:
        img = Image.open(image_file)
        c.setPageSize((img.width, img.height))
        c.drawImage(image_file, 0, 0, img.width, img.height)
        c.showPage()
    c.save()

def main():
    # Lista todos os arquivos na pasta atual
    files = [f for f in os.listdir('.') if os.path.isfile(f)]
    
    # Filtra apenas imagens
    image_extensions = ['.png', '.jpg', '.jpeg', '.gif', '.bmp']
    image_files = [f for f in files if any(f.endswith(ext) for ext in image_extensions)]
    
    # Ordena os arquivos com base nos números extraídos dos nomes
    image_files.sort(key=lambda f: extract_number(f))
    
    # Cria o PDF
    create_pdf(image_files)

if __name__ == "__main__":
    main()
