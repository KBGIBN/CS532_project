from datetime import datetime
import os
from email.headerregistry import Address
import torch
import matplotlib.pyplot as plt
from PIL import Image

import vietocr
from vietocr.tool.predictor import Predictor
from vietocr.tool.config import Cfg

config = Cfg.load_config_from_name('vgg_transformer')

config['weights'] = './transformerocr.pth'
config['cnn']['pretrained']=False
config['device'] = 'cpu'
config['predictor']['beamsearch']=False

detector = Predictor(config)

wf = open('./data.txt', 'w', encoding="utf-8")

# ID number
img_path = os.listdir('./runs/detect/exp/crops/cid_no/')
id_no = ''
for path in img_path:
    img = Image.open('./runs/detect/exp/crops/cid_no/' + path)
    temp = detector.predict(img)
    if temp.isnumeric() == True:
        id_no = temp
        break
wf.write("NUMBER: " + str(id_no))

# Name
img = './runs/detect/exp/crops/cname/input.jpg'
img = Image.open(img)
name = (detector.predict(img)).upper()
wf.write("\nNAME: " + str(name))

# Date of Birth
img_path = os.listdir('./runs/detect/exp/crops/cdob/')
dob = ''
for path in img_path:
    img = Image.open('./runs/detect/exp/crops/cdob/' + path)
    temp = detector.predict(img)
    if bool(datetime.strptime(temp,"%d/%m/%Y")) == True:
        dob = temp
        break
wf.write("\nDATE OF BIRTH: " + str(dob))

# Nationality
img_path = os.listdir('./runs/detect/exp/crops/cnationality/')
nation = ''
for path in img_path:
    img = Image.open('./runs/detect/exp/crops/cnationality/' + path)
    temp = detector.predict(img)
    if temp[0].isalpha() == True:
        nation = temp
        break

wf.write("\nNATIONALITY: " +str(nation.upper()))

# Address
img_path = os.listdir('./runs/detect/exp/crops/caddress/')
address = ''
for path in reversed(img_path):
    img = Image.open('./runs/detect/exp/crops/caddress/' + path)
    addr = detector.predict(img)
    if "VIỆT NAM" in addr:
        continue
    elif "ngày" in addr:
        continue
    elif addr == nation:
        continue
    else:
        address += addr + ' '

wf.write("\nADDRESS: " + address)

# Class
img_path = os.listdir('./runs/detect/exp/crops/cclass/')
lc_class = ''
for path in img_path:
    img = Image.open('./runs/detect/exp/crops/cclass/' + path)
    temp = (detector.predict(img)).upper()
    if temp[:2] in ["A1", "A2", "A3", "B1", "B2", "C", "D", "E", "FB2", "FC", "FD", "FE"]:
        lc_class = temp
        break

wf.write("\nLICENSE CLASS: " + str(lc_class))

# Expires
img_path = os.listdir('./runs/detect/exp/crops/cexpires/')
exp = ''
for path in img_path:
    img = Image.open('./runs/detect/exp/crops/cexpires/' + path)
    temp = (detector.predict(img)).upper()
    if temp == "KHÔNG THỜI HẠN":
        exp = temp
        break
    elif bool(datetime.strptime(temp,"%d/%m/%Y")) == True:
        exp = temp
        break
wf.write("\nEXPIRES: " + str(exp))

wf.close()