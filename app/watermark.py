# importing libraries
from flask import Blueprint, render_template, redirect , request, url_for, current_app,flash
# Blueprint is a way to organize a group of related views and other code. Rather than registering views and other code directly with an application, they are registered with a blueprint. Then the blueprint is registered with the application when it is available in the factory function.
from PIL import Image 
import os 
import cv2
import numpy as np
from werkzeug.utils import secure_filename 
from utils.utils import add_logo, add_text


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
    result_filename = None

    if request.method == 'POST':
            option = request.form['options']
            
            if option == 'logo':
                if 'file1' not in request.files or 'file2' not in request.files:
                    flash('No file part')
                    return redirect(request.url)

                file1 = request.files['file1']
                file2 = request.files['file2']

                if file1.filename == '' or file2.filename == '':
                    flash('No selected file')
                    return redirect(request.url)

                if file1 and allowed_file(file1.filename) and file2 and allowed_file(file2.filename):
                    photo_folder = os.path.join(current_app.config['UPLOAD_FOLDER'], 'photos')
                    logo_folder = os.path.join(current_app.config['UPLOAD_FOLDER'], 'logos')
                    result_folder = os.path.join(current_app.config['UPLOAD_FOLDER'], 'results')

                    # create the folders if it doesn't exist
                    os.makedirs(photo_folder, exist_ok=True)
                    os.makedirs(logo_folder, exist_ok=True)
                    os.makedirs(result_folder, exist_ok=True)

                    filename1 = secure_filename(file1.filename)
                    filepath1 = os.path.join(photo_folder, filename1)
                    file1.save(filepath1)

                    filename2 = secure_filename(file2.filename)
                    filepath2 = os.path.join(logo_folder, filename2)
                    file2.save(filepath2)

                    # Apply logo watermarking
                    result_photo_path = add_logo(filepath1, filepath2)
                    result_filename = os.path.basename(result_photo_path)
                    flash('Logo watermark added successfully!')

            elif option == 'text':
                if 'file1' not in request.files or 'text' not in request.form:
                    flash('No file part or text provided')
                    return redirect(request.url)

                file1 = request.files['file1']
                text = request.form['text']

                if file1.filename == '':
                    flash('No selected file')
                    return redirect(request.url)

                if file1 and allowed_file(file1.filename):
                    filename1 = secure_filename(file1.filename)
                    filepath1 = os.path.join(current_app.config['UPLOAD_FOLDER'], 'photos', filename1)
                    file1.save(filepath1)

                    # Apply text watermarking
                    result_photo_path = add_text(filepath1, text)
                    flash('Text watermark added successfully!')
                    result_filename = os.path.basename(result_photo_path)
            return render_template('index.html', result_filename=result_filename)
    return render_template('index.html')