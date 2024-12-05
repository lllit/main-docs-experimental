import fitz  # PyMuPDF
import os

def pdf_to_text_with_images(pdf_path, output_text_path, output_image_dir):
    # Crear el directorio de imágenes si no existe
    if not os.path.exists(output_image_dir):
        os.makedirs(output_image_dir)
    
    # Abrir el archivo PDF
    pdf_document = fitz.open(pdf_path)
    
    # Crear o abrir el archivo de texto de salida
    with open(output_text_path, 'w', encoding='utf-8') as text_file:
        # Iterar a través de cada página
        for page_num in range(len(pdf_document)):
            page = pdf_document.load_page(page_num)
            
            # Extraer texto de la página
            text = page.get_text()
            text_file.write(text)
            
            # Extraer imágenes de la página
            image_list = page.get_images(full=True)
            for img_index, img in enumerate(image_list):
                xref = img[0]
                base_image = pdf_document.extract_image(xref)
                image_bytes = base_image["image"]
                image_ext = base_image["ext"]
                
                # Guardar la imagen
                image_path = f"{output_image_dir}/page_{page_num + 1}_img_{img_index + 1}.{image_ext}"
                with open(image_path, 'wb') as image_file:
                    image_file.write(image_bytes)

# Ejemplo de uso
pdf_path = r"C:\Users\litio\OneDrive - Aiep\AIEP\Aiep Archivos\METODOLOGÍAS DE DESARROLLO DE SOFTWARE\Semana 7\PRO204_s7.pdf"

output_text_path = "output.txt"
output_image_dir = "images"


pdf_to_text_with_images(pdf_path, output_text_path, output_image_dir)

print("Conversión de PDF completada. El texto y las imágenes se han guardado.")