import os
import requests

url = 'http://127.0.0.1:5000/predict'
path_img = 'jpg/101_4.jpg'
with open(path_img, 'rb') as img:
  name_img= os.path.basename(path_img)
  files= {'image': (name_img,img,'multipart/form-data',{'Expires': '0'}) }
  with requests.Session() as s:
    r = s.post(url,files=files)
    print(r.status_code)
    print(r.text)