from tabnanny import check
from urllib import response
from flask import Flask,render_template,request,jsonify,url_for,redirect
from matplotlib import image
import numpy as np
from PIL import Image
import glob


input_date = []


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('base.html')

@app.route('/predict',methods=['POST','GET'])
def upload_image():
    check = True
    uploaded_file = request.files['image']
    if uploaded_file.filename is not None:
        i1 = Image.open(uploaded_file)
        path = "jpg/*"
        list_1=[]
        for x in glob.iglob(path):
            i2 = Image.open(x)
            assert i1.mode == i2.mode, "Different kinds of images."
            assert i1.size == i2.size, "Different sizes."
            pairs = zip(i1.getdata(), i2.getdata())
            if len(i1.getbands()) == 1:
                dif = sum(abs(p1-p2) for p1,p2 in pairs)
            else:
                dif = sum(abs(c1-c2) for p1,p2 in pairs for c1,c2 in zip(p1,p2))
            ncomponents = i1.size[0] * i1.size[1] * 3
            diff =(dif / 255.0 * 100) / ncomponents
            g = 100 - diff
            print ("File :", x)
            ans = float("{:.2f}".format(g))
            ok = (ans, x)
            list_1.append(ok)
            print ("Matches: ", ans,"%")

        Matches = max(list_1)[0]
        Per = max(list_1)[1]
        person = (Per.rsplit('/',1)[1])
        person2 = (person.rsplit('.',1)[0])
        JSONN = {
                "Patient Name" : person2,
                "Matches" : Matches
        }
        return(jsonify(JSONN))

if __name__=="__main__":
    app.run()