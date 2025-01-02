import os
from fpdf import FPDF
from PIL import Image

images_folder = 'C:/Users/your_folder'
output_pdf = 'your_name.pdf' 

def images_to_pdf(images_folder, output_pdf):
    # List of every image in .png in images_folder
    image_files = [f for f in os.listdir(images_folder) if f.endswith('.png')]
    
    # Sort the list
    image_files.sort(key=lambda x: int(x.split('.')[0]))
    
    # Créer une instance du PDF
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)

    # Add each image to the pdf
    for image_file in image_files:
        image_path = os.path.join(images_folder, image_file)
        
        img = Image.open(image_path)
        img_width, img_height = img.size
        
        pdf.add_page()
        
        pdf.image(image_path, x=10, y=10, w=190)
    
    # Sabe the generated pdf
    pdf.output(output_pdf)
    print(f"The PDF has been created and his saved under the name: {output_pdf}")


images_to_pdf(images_folder, output_pdf)

