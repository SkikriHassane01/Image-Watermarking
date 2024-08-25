# now we will create two functions one for adding a logo and the other for adding text to an image
import numpy as np
import cv2
from PIL import Image
import os 

def add_logo(img_path, logo_path):
    # Open the main image and the logo image
    img = Image.open(img_path).convert('RGB')
    logo = Image.open(logo_path).convert('RGB')


    img = img.resize((500,600))
    logo = logo.resize((150,150))

    # Convert to numpy arrays
    img = np.array(img)
    logo = np.array(logo)

    # extract the shape of the image and the logo
    img_height, img_width, _ = img.shape
    logo_height, logo_width, _ = logo.shape

    # calculate the top left corner of the logo
    x = (img_width - logo_width) // 2
    y = (img_height - logo_height) // 2

    # create the ROI
    roi = {
        "Bottom_left" : (x, y + logo_height),
        "Top_right" : (x + logo_width, y)
    }

    # extract the ROI
    ROI = img[roi["Top_right"][1]:roi["Bottom_left"][1], roi["Bottom_left"][0]:roi["Top_right"][0]]

    # merge the logo and the ROI using opencv
    result = cv2.addWeighted(ROI, 1, logo, 0.5, 0)

    # draw the logo on the image
    img[roi["Top_right"][1]:roi["Bottom_left"][1], roi["Bottom_left"][0]:roi["Top_right"][0]] = result

    # convert the array to an image
    img = Image.fromarray(img)
    
    # Save the image
    result_path = img_path.replace('photos', 'results')
    result_path = os.path.splitext(result_path)[0] + '_watermarked.png'
    img.save(result_path)

    return result_path


def add_text(img_path, text):
    print(f"Loading image from: {img_path}")
    img = Image.open(img_path).convert('RGB')
    img = img.resize((500, 600))
    img = np.array(img)

    img_height, img_width, _ = img.shape
    print(f"Image dimensions: {img_width}x{img_height}")

    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 1
    font_thickness = 2
    text_size = cv2.getTextSize(text, font, font_scale, font_thickness)[0]
    print(f"Text size: {text_size}")

    text_x = (img_width - text_size[0]) // 2
    text_y = (img_height + text_size[1]) // 2

    print(f"Text position: {text_x}, {text_y}")
    cv2.putText(img, text, (text_x, text_y), font, font_scale, (255, 255, 255), font_thickness)

    img = Image.fromarray(img)
    result_path = img_path.replace('photos', 'results')
    result_path = os.path.splitext(result_path)[0] + '_watermarked.png'
    
    print(f"Saving image to: {result_path}")
    img.save(result_path)
    
    return result_path