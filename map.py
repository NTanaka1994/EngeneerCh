#ライブラリのインポート
import pandas as pd

#データの読み込み
df=pd.read_csv("map.csv",encoding="shift-jis")
address=df["住所"].values
state=df["団体名"].values

#データの作成
table=[]
url="https://www.google.com/maps/place/"
for i in range(len(address)):
    tmp=[]
    nurl=url+state[i]+address[i]
    tmp.append(address[i])
    tmp.append(nurl)
    table.append(tmp)

#エクセルファイに変換   
dft=pd.DataFrame(table)
dft.columns=["住所","URL"]
dft.to_excel("map_url.xlsx",index=False,encoding="shift-jis")
