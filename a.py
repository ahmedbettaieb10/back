import os
import shutil
import zipfile
from flask import Flask, request, send_file

app = Flask(__name__)

@app.route('/')
def index():
    # Chemin du dossier à créer
    dossier = os.path.join(os.getcwd(),  'pfe1')
    os.makedirs(dossier, exist_ok=True)
    return 'Dossier créé avec succès !'

@app.route('/copydossier')
def copydossier():
    # Chemin du dossier source à copier
    sourcePath = os.path.abspath('pfe')

    # Chemin du dossier de destination
    destinationPath = os.path.join(os.getcwd(), 'pfe1', 'l')

    # Utilisation de la fonction shutil.copytree pour copier le dossier
    try:
        shutil.copytree(sourcePath, destinationPath)
        message = f"The folder {sourcePath} was successfully copied to {destinationPath}"
    except Exception as e:
        message = f"An error occurred while copying the folder: {str(e)}"

    return message

@app.route('/copyfile', methods=['POST'])
def copyfile():
    file = request.files['file']
    filename = file.filename
    new_filename = "data.json"  # Remplacez "nouveau_nom.txt" par le nom que vous souhaitez donner au fichier.
    destination = os.path.join(os.getcwd(),  'pfe1', 'l', 'src', new_filename)
    new_filename1 = "a.json" 
    destination1 = os.path.join(os.getcwd(), 'flask', 'backend', new_filename1)
    file.save(destination)
    file.save(destination1)
    return 'File saved successfully!'

@app.route('/copypdf', methods=['POST'])
def copypdf():
    pdf_file = request.files['pdf_file']
    filename = pdf_file.filename
    new_filename = "document.pdf"  # Remplacez "document.pdf" par le nom que vous souhaitez donner au fichier PDF.
    destination = os.path.join(os.getcwd(),  'pfe1', new_filename)
    pdf_file.save(destination)
    return 'PDF file saved successfully!'

@app.route('/zipfolder')
def zipfolder():
    # Chemin du dossier à compresser
    folder_path = os.path.join(os.getcwd(),  'pfe1')

    # Chemin du fichier zip de destination
    zip_path = os.path.join(os.getcwd(),  'pf1.zip')

    # Utilisation de la fonction zipfile.ZipFile pour compresser le dossier
    try:
        with zipfile.ZipFile(zip_path, 'w', compression=zipfile.ZIP_DEFLATED) as zip_file:
            for root, dirs, files in os.walk(folder_path):
                for file in files:
                    file_path = os.path.join(root, file)
                    zip_file.write(file_path, os.path.relpath(file_path, folder_path))
        message = f"The folder {folder_path} was successfully compressed to {zip_path}"
    except Exception as e:
        message = f"An error occurred while compressing the folder: {str(e)}"

    return message

@app.route('/downloadzip')
def download_zip():
    # Chemin du fichier zip à télécharger
    zip_path = os.path.join(os.getcwd(),  'pf1.zip')

    # Vérifier si le fichier zip existe
    if not os.path.exists(zip_path):
        return "Le fichier zip n'existe pas !"

    # Lire le contenu du fichier zip
    with open(zip_path, 'rb') as file:
        zip_content = file.read()

    

    # Utilisation de la fonction send_file de Flask pour renvoyer le fichier zip en tant que réponse HTTP
    return send_file(zip_path, as_attachment=True)
if __name__ == '__main__':
    app.run(debug=True ,port=5000,host="0.0.0.0")
