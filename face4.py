#⑴ ライブラリをインポートする
# 数値計算に必要なライブラリ
import numpy as np
import pandas as pd
# グラフを描画するパッケージ
import matplotlib.pyplot as plt
# 機械学習ライブラリscikit-learnの線形モデル
from sklearn import linear_model


#⑵ データを読み込む
from sklearn.datasets import load_boston
boston = load_boston()


#⑶ データの中身を確認し、分析用に加工する
print(boston)

print(boston.DESCR)


#⑷ データをPandasのデータフレームに変換する
boston_df = pd.DataFrame(boston.data)
print(boston_df)


#⑸ カラム名を指定し、目的変数を追加する

# カラム名を指定
boston_df.columns = boston.feature_names
print(boston_df)

# 目的変数を追加
boston_df['PRICE'] = pd.DataFrame(boston.target)
print(boston_df)

#####scikit-learnの基本的な文法####

#⑹ 説明変数、目的変数を作成する

# 目的変数のみ削除して変数Xに格納
X = boston_df.drop("PRICE", axis=1)
# 目的変数のみ抽出して変数Yに格納
Y = boston_df["PRICE"]
print(X)
print(Y)

#⑺ インスタンスを作成する①

model = linear_model.LinearRegression()

#⑻ モデルを作成する②

model.fit(X,Y)


#⑼ 回帰係数を算出する③

model.coef_

# 変数coefficientに係数の値を格納
coefficient = model.coef_
# データフレームに変換し、カラム名とインデックス名を指定
df_coefficient = pd.DataFrame(coefficient,
                              columns=["係数"],
                              index=["犯罪率", "宅地率", "製造業比率", "チャールズ川", "一酸化窒素濃度", 
                                     "平均室数", "持ち家率", "雇用センター", "幹線道路", "固定資産税率", 
                                     "生徒･教師比率", "黒人比率", "下層階級比率"])
df_coefficient


#⑽ 切片を算出する④

model.intercept_

#⑾ 決定係数を算出して精度を確認する⑤

model.score(X, Y)


#####クロスバリデーション######


#➊ サンプルを分割する

# sklearnのtrain_test_splitメソッドをインポート
from sklearn.model_selection import train_test_split
# 変数X, Yをそれぞれトレーニング用とテスト用に分割
X_train, X_test, Y_train, Y_test = train_test_split(X,Y)

print("変数xのトレーニング用データ:", X_train, sep="\n")
print("変数xのテスト用データ:", X_test, sep="\n")

#➋ インスタンスを作成する①

multi_lreg = linear_model.LinearRegression()

#➌ トレーニングデータでモデルを作成する②

multi_lreg.fit(X_train, Y_train)


#➍ トレーニングデータでの決定係数を算出する⑤


multi_lreg.score(X_train, Y_train)



#➎ テストデータでの決定係数を算出する⑤

multi_lreg.score(X_test,Y_test)