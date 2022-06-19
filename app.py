from flask import Flask, render_template, request, jsonify, redirect, url_for, flash
from werkzeug.utils import secure_filename
from werkzeug.datastructures import  FileStorage
import os
# from flask.ext.mysql import MySQL
import json
import extractor
from PIL import Image
import time
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
# import tensorflow as tf

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')  # Path to .env file
load_dotenv(dotenv_path)

app = Flask(__name__, template_folder='./')
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://gkbuqaaatbfyli:4b3f2f5a61e6721431cc313c5e102a8f8c66198993abb38504d6b3a0901de41c@ec2-52-72-56-59.compute-1.amazonaws.com:5432/d7cdcbkmnad8pj'

# Initialize the database
db = SQLAlchemy(app)

# Create db model
class Information(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    No = db.Column(db.String(12), nullable=False)
    Name = db.Column(db.String(50), nullable=False)
    DoB = db.Column(db.Date, nullable=False)
    Nationality = db.Column(db.String(50), nullable=False)
    Address = db.Column(db.String(100), nullable=False)
    Class = db.Column(db.String(20), nullable=False)
    Expires = db.Column(db.String(20), nullable=False)
    date_added = db.Column(db.DateTime, default=datetime.utcnow)

    # def __repr__(self):
    #     return '<Name %r>' % self.id

@app.route("/", methods=['GET'])
def show_template():
    return render_template("./static/main.html")

UPLOAD_FOLDER = './input'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# graph = tf.compat.v1.get_default_graph()

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/uploader', methods=['GET', 'POST'])  
def upload_file():
    # with graph.as_default():
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
             
            start_time = time.time()    
            result = extractor.main()
            print("--- %s seconds ---" % (time.time() - start_time))
            
            response = {"data": result}
        
        return jsonify(response)
    

if __name__ == "__main__": 
    app.run(host='0.0.0.0',port='8080',debug = True)

