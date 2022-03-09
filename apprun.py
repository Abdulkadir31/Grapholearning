from flask import *
import os
import base64
import cv2
import image_resize
import report_mail
from train_predict import *


app= Flask(__name__)

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

@app.route('/')
def default():
    rus = image_resize.reduce_size("Images\\vishal.jpg")
    ans,careers = run_app("Images/Rescaled.jpg")
    print(ans)
    print(careers)
    return ans


@app.route('/upload',methods=['POST'])
def upload():

    target = os.path.join(APP_ROOT,'images/')

    if not os.path.isdir(target):
        os.mkdir(target)

    #filename = request.files['name']
    file = request.form['image']


    fh = open("images/imageToSave.jpg", "wb")
    fh.write(base64.b64decode(file))
    fh.close()

    rus = image_resize.reduce_size("images/imageToSave.jpg")
    print("File Sent")
    ans,career = run_app("Images/Rescaled.jpg")
    print("Ans is: "+ans)
    print(career)
    return ans+career

@app.route('/sendmail',methods=['POST'])
def mail():
    mail = request.form['mail']
    res = request.form['Results']
    print(mail)
    ans = report_mail.mail_send(res,mail)
    if ans:
        print("Mail Send")
        return "True"
    else:
        print("Mail Not Send")
        return "False"



if __name__=='__main__':
    app.run(host='192.168.0.10',debug='True')


