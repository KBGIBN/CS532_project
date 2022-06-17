from flask import Flask, render_template, request, jsonify, redirect, url_for, flash
from werkzeug.utils import secure_filename
from werkzeug.datastructures import  FileStorage
import os
# from flask.ext.mysql import MySQL
import json
import extractor
from PIL import Image
import tensorflow as tf

app = Flask(__name__, template_folder='./')

@app.route("/", methods=['GET'])
def show_template():
    return render_template("./static/main.html")

UPLOAD_FOLDER = './input'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

graph = tf.compat.v1.get_default_graph()

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/uploader', methods=['GET', 'POST'])  
def upload_file():
    with graph.as_default():
        INPUT_IMG = os.listdir('./input')
        if INPUT_IMG is not None:
            for upload_img in INPUT_IMG:
                os.remove(os.path.join('./input', upload_img))
                
        if request.method == 'POST':  
            # Upload image from POST request
            file = request.files['file']         
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                
            result = extractor.main()
            
            print(result)
            
            response = {"data": result}
        
        return jsonify(response)
    

if __name__ == "__main__":
    app.run(host='0.0.0.0',port='8080',debug = True)

	