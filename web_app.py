from flask import Flask, render_template, request, jsonify, redirect, url_for, flash
from werkzeug.utils import secure_filename
from werkzeug.datastructures import  FileStorage
import os
# from flask.ext.mysql import MySQL
import json
import extractor
from PIL import Image

app = Flask(__name__, template_folder='./')

@app.route("/", methods=['GET'])
def show_template():
    return render_template("./static/main.html")

UPLOAD_FOLDER = './upload'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/uploader', methods=['GET', 'POST'])  
def upload_file():
    INPUT_IMG = os.listdir('./upload')
    if INPUT_IMG is not None:
        for upload_img in INPUT_IMG:
            os.remove(os.path.join('./upload', upload_img))
            
    if request.method == 'POST':  
        # Upload image from POST request
        file = request.files['file']         
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            

        INPUT_IMG = os.listdir('./upload')
        if INPUT_IMG is not None:
            img = Image.open(os.path.join('./upload', INPUT_IMG[0]))
        else:
            print('Cant read image')

        input_img = img.copy()
        extractor.detect(input_img)
        
        result = extractor.ocr_extract()
        
        # response = ("No: " + result[0] + "\n" + 
        #             "Full name: " + result[1] + "\n" + 
        #             "Date of Birth: " + result[2] + "\n" + 
        #             "Nationality: " + result[3] + "\n" + 
        #             "Adress: " + result[4] + "\n" + 
        #             "Class: " + result[5] + "\n" + 
        #             "Expires: " + result[6]
        #            )
        
        response = {"data": result}
        
        return jsonify(response)
    
    else: 
        return "fail"

if __name__ == "__main__":
    app.run(debug = True)

	