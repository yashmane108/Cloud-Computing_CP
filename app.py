import os
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Configuration for the upload folder
UPLOAD_FOLDER = os.path.join(os.getcwd(), 'uploads')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Check if the upload folder exists, if not, create it
if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

# Route for the homepage
@app.route('/')
def index():
    return render_template('index.html')

# Route to handle file uploads
@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return "No file part"
    file = request.files['file']
    if file.filename == '':
        return "No selected file"
    if file:
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filepath)
        return f"File uploaded successfully: <a href='/uploads/{file.filename}'>{file.filename}</a>"

if __name__ == '__main__':
    app.run(debug=True)