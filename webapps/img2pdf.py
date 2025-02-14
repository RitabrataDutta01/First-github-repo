import os
import sys
import threading
from fpdf import FPDF
from werkzeug.utils import secure_filename
from flask import Flask, render_template, request, send_file, redirect
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from PyQt5.QtWebEngineWidgets import QWebEngineView


app = Flask(__name__)


def get_base_folder():
    if getattr(sys, 'frozen', False): 
        return os.path.dirname(sys.executable)  
    else:
        return os.getcwd()  

def get_output_folder():
    base_folder = get_base_folder()
    output_folder = os.path.join(base_folder, 'output')

    os.makedirs(output_folder, exist_ok=True)
    return output_folder


def get_upload_folder():
    base_folder = get_base_folder()
    upload_folder = os.path.join(base_folder, 'uploads')

    os.makedirs(upload_folder, exist_ok=True)
    return upload_folder

AllowedExtension = ['jpg', 'jpeg', 'png']

app.config['UPLOAD_FOLDER'] = get_upload_folder()
app.config['OUTPUT_FOLDER'] = get_output_folder()

def allowedfilename(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in AllowedExtension

@app.route('/')
def index():
    return render_template('img2pdf.html')

@app.route('/convert', methods=['POST'])
def i2p():
    if 'files' not in request.files:
        return redirect(request.url)

    files = request.files.getlist('files')

    if len(files) == 0:
        return redirect(request.url)

    file_paths = []
    for file in files:
        if file.filename == '':
            continue

        if file and allowedfilename(file.filename):
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)
            file_paths.append(filepath)
        else:
            return render_template('img2pdf.html', message='Invalid file format. Please upload image files.')

    output_pdf_path = os.path.join(get_output_folder(), 'merged_images.pdf')

    convert_images_to_pdf(file_paths, output_pdf_path)

    return send_file(output_pdf_path, as_attachment=True)

def convert_images_to_pdf(image_paths, output_pdf_path):
    pdf = FPDF()

    for image_path in image_paths:
        pdf.add_page()
        pdf.image(image_path, x=10, y=10, w=190)

    pdf.output(output_pdf_path)

def run_flask_app():
    app.run(debug=True, use_reloader=False)

class BrowserWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Image to PDF Converter")
        self.setGeometry(100, 100, 800, 600)

        layout = QVBoxLayout()
        self.browser = QWebEngineView()
        layout.addWidget(self.browser)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        self.browser.setUrl(QUrl("http://127.0.0.1:5000/"))

    def closeEvent(self, event):
        os._exit(0)

def start_application():

    flask_thread = threading.Thread(target=run_flask_app)
    flask_thread.daemon = True 
    flask_thread.start()

    app = QApplication(sys.argv)
    window = BrowserWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    start_application()
