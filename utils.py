# now we will create two functions one for adding a logo and the other for adding text to an image
import numpy as np
import cv2
from PIL import Image

def add_logo(img, logo):
    # convert the image and the logo to numpy array 
    img = np.array(img.convert('RGB'))
    logo = np.array(logo.convert('RGB'))

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
    result = cv2.addWeighted(ROI, 1, logo, 0.2, 0)

    # draw the logo on the image
    img[roi["Top_right"][1]:roi["Bottom_left"][1], roi["Bottom_left"][0]:roi["Top_right"][0]] = result

    return Image.fromarray(img)



def add_text(img, text):
    # convert the image to numpy array
    img = np.array(img.convert('RGB'))

    # extract the shape of the image
    img_height, img_width, _ = img.shape
    img_width, img_width, _ = img.shape

    # define the font and the text size
    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 1
    font_thickness = 2
    text_size = cv2.getTextSize(text, font, font_scale, font_thickness)[0]

    # calculate the top left corner of the text
    text_x = (img_width - text_size[0]) // 2
    text_y = (img_height + text_size[1]) // 2

    # draw the text on the image
    cv2.putText(img, text, (text_x, text_y), font, font_scale, (255, 255, 255), font_thickness)

    return Image.fromarray(img)