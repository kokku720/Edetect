# coding: utf-8
import os
import sys
import csv
import json
import pandas as pd
import requests
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from config import API_KEY, API_SECRET, DETECT_PATH ,ANALYZE_PATH
import cv2
import codecs
import glob
import re
from PIL import Image
import numpy as np

return_landmark = 0
return_attributes = None
#calculate_all = 0
face_rectangle = ''
beauty_score_min = 0
beauty_score_max = 100

def call_api():
    data = {
        'api_key': API_KEY,
        'api_secret': API_SECRET,
        'return_landmark': 1,
        'return_attributes': 'gender,age,emotion'
        #'calculate_all': calculate_all,
        #'beauty_score_min': beauty_score_min,
        #'beauty_score_max': beauty_score_max
    }
    dir = 'images/images01/'
    imagefiles = glob.glob(dir + "*.jpg")
    for f in imagefiles:
        file = os.path.basename(f)          # 拡張子ありファイル名を取得
        if face_rectangle in file: 
            data.update({'face_rectangle': face_rectangle})
        input_file = file
        if not input_file:
            print('画像ファイルを正しいディレクトリに置いてください')
            return
        files = {
            'image_file': open(f, 'rb').read()
        }
        resp = requests.post(DETECT_PATH, data=data, files=files).json()
        
        for key, value in resp.items():
            osp =resp['faces']
        json_file = open("emotion.json","a")
        json.dump(osp,json_file)
    
if __name__ == "__main__":
    call_api()
    
