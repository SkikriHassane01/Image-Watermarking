# importing libraries
from flask import Blueprint, render_template, redirect , request, url_for, current_app
# Blueprint is a way to organize a group of related views and other code. Rather than registering views and other code directly with an application, they are registered with a blueprint. Then the blueprint is registered with the application when it is available in the factory function.
from PIL import Image 
import os 
import cv2
import numpy as np
from werkzeug.utils import secure_filename 


# creating a Blueprint class
bp = Blueprint('watermark', __name__, template_folder='templates', static_folder='static')

# allowed file function
def allowed_file(filename):
    return '.' in filename and \
    filename.rsplit('.', 1)[1].lower() in current_app.config['ALLOWED_EXTENSIONS']

# '.' in filename will checks whether the filename contains a period '.'
# filename.rsplit('.', 1) splits the filename into two parts and 1 mean that the string should be split only once 

@bp.route('/', methods= ['GET', 'POST'])
def index():
    if request.method == 'POST':
        # check if the post request has the file part, file part is the name of the input field in the form 
        if 'file' not in request.files:
            flask('NO file part')
            return redirect(request.url) # redirect to the same page

        file = request.files['file']
        filename = file.filename
        # check if the file is empty
        if filename == '':
            flash('No selected file')
            return redirect(request.url)
        
        # check if the file is allowed
        if file and allowed_file(filename):
            filename = secure_filename(filename)
            filepath = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)
            # os.path.join is used to concatenate the directory paths and file names 
            file.save(filepath)

            # 