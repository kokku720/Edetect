# coding: utf-8
import os
import sys
import csv
import pandas as pd
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

import requests

from config import API_KEY, API_SECRET, DETECT_PATH ,ANALYZE_PATH
from example.common import get_input_file_path

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
    if face_rectangle:
        data.update({'face_rectangle': face_rectangle})
    input_file = get_input_file_path(os.path.abspath(os.path.dirname(__file__)), 'input')
    if not input_file:
        print('请将input.png/input.jpg文件放在detect目录下')
        return

    """
    if data{'return_landmark'}:
        data.update({'return_landmark' : return_landmark})
    input_file = get_input_file_path(os.path.abspath(os.path.dirname(__file__)), 'input')
    if not input_file:
        print('请将input.png/input.jpg文件放在detect目录下')
        return
    if data{'return_attributes'}:
        data.update({'return_attributes':return_attributes})
    input_file = get_input_file_path(os.path.abspath(os.path.dirname(__file__)), 'input')
    if not input_file:
        print('请将input.png/input.jpg文件放在detect目录下')
        return
    """

    files = {
        'image_file': open(input_file, 'rb').read()
    }
    resp = requests.post(DETECT_PATH, data=data, files=files).json()

    with open('emotion.csv','w') as csv_file:
        writer = csv.writer(csv_file)
        for key, value in resp.items():
            writer.writerows(resp)

    (pd.DataFrame.from_dict(data=resp,orient='index').to_csv('emotion_csv',header=False))



    osp = resp['faces']
    df = pd.io.json.json_normalize(osp)
    print(df)
    df.to_csv('emotion2_csv')
    #(pd.DataFrame.from_dict(data=osp, orient='index').to_csv('emotion2_csv', header=False))

    #print(resp['faces'])




if __name__ == "__main__":
    call_api()
