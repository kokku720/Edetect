# 数値計算に必要なライブラリ
import numpy as np
import pandas as pd
# グラフを描画するパッケージ
import matplotlib.pyplot as plt
# 機械学習ライブラリscikit-learnの線形モデル
from sklearn import linear_model
import torch
from sklearn.preprocessing import normalize
from torch.utils.data import DataLoader, Dataset
from sklearn.datasets import load_boston
boston = load_boston()

class Wine(Dataset):
    def __init__(self, csv_path):
        # csv ファイルを読み込む。
        df = pd.read_csv(csv_path)
        data = df.iloc[:, 1:]  # データ (2 ~ 14列目)
        labels = df.iloc[:, 0]  # ラベル (1列目)
        # データを標準化する。
        data = normalize(data)
        # クラス ID を 0 始まりにする。[1, 2, 3] -> [0, 1, 2]
        labels -= 1

        self.data = data
        self.labels = labels

    def __getitem__(self, index):
        """サンプルを返す。
        """
        return self.data[index], self.labels[index]

    def __len__(self):
        """csv の行数を返す。
        """
        return len(self.data)


# Dataset を作成する。
dataset = Wine("https://raw.githubusercontent.com/kokku720/facee/main/emotion.csv")
print(dataset)
# DataLoader を作成する。
dataloader = DataLoader(dataset, batch_size=64)

#for X_batch, y_batch in dataloader:
    #print(X_batch.shape, y_batch.shape)


datasetdf = pd.DataFrame(dataset.data)
#print(datasetdf)

# カラム名を指定
#datasetdf.columns = dataset.feature_names
#print(datasetdf)
"""
# 'Score'(幸福スコア)を目的変数'target'とする
facemotion['target'] = datasetdf[['anger', 'disgust', 'fear', 'happiness', 'neutral',
       'sadness', 'surprise']]

# 説明変数を'data'に入れる
facemotion['DATA'] = datasetdf.loc[:, ['anger', 'disgust', 'fear', 'happiness', 'neutral',
       'sadness', 'surprise']]
"""