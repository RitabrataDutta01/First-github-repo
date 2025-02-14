import sys
import os
import threading
from flask import Flask, render_template, request, send_file, redirect
from werkzeug.utils import secure_filename
import PyPDF2
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from PyQt5.QtWebEngineWidgets import QWebEngineView


app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['OUTPUT_FOLDER'] = 'output'
app.config['ALLOWED_EXTENSIONS'] = {'pdf'}

os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
os.makedirs(app.config['OUTPUT_FOLDER'], exist_ok=True)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

@app.route('/')
def index():
    return render_template('pdfmerge.html')

@app.route('/merge', methods=['POST'])
def merge_pdfs():

    if 'files' not in request.files:
        return redirect(request.url)

    files = request.files.getlist('files')

    if len(files) == 0:
        return redirect(request.url)

    file_paths = []
    for file in files:
        if file.filename == '':
            continue

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)
            file_paths.append(file_path)
        else:
            return render_template('pdfmerge.html', message='Invalid file format. Please upload PDF files.')

    merger = PyPDF2.PdfMerger()
    for file_path in file_paths:
        merger.append(file_path)

    output_filename = 'merged.pdf'
    output_file_path = os.path.join(app.config['OUTPUT_FOLDER'], output_filename)

    merger.write(output_file_path)
    merger.close()

    return send_file(output_file_path, as_attachment=True)


class BrowserWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PDF Merger")
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


def run_flask_app():
    app.run(debug=True, use_reloader=False)


def start_application():
    flask_thread = threading.Thread(target=run_flask_app)
    flask_thread.start()

    qt_app = QApplication(sys.argv)
    window = BrowserWindow()
    window.show()
    sys.exit(qt_app.exec_())


if __name__ == '__main__':
    start_application()
