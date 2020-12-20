from sklearn.feature_extraction.text import TfidfVectorizer as tfidf
from sklearn.neural_network import MLPClassifier
from janome.tokenizer import Tokenizer
import speech_recognition as sr
import subprocess
import glob
import numpy as np

#文字起こし行う
total=[]
r=sr.Recognizer()
for path in glob.glob("folder/*.wav"):
    with sr.AudioFile("folder/"+path[6:]) as src:
        ad=r.record(src)
    text=r.recognize_google(ad, language='ja-JP')
    total.append(text)
print(total)

#台本の読み込み
f=open("story_doc/sample.txt","r",encoding="utf-8")
s=f.read()
f.close()
rm=s.split("\n")
print(rm)

#形態素解析
t=Tokenizer()
train=[]
test=[]
sumt=[]
for i in range(len(total)):
    train.append(t.tokenize(total[i],wakati=True))
    test.append(t.tokenize(rm[i],wakati=True))
for i in range(len(train)):
    sumt.append(train[i])
for i in range(len(test)):
    sumt.append(test[i])

#分かち書き
x_doc=[]
for i in range(len(sumt)):
    doc=""
    for j in range(len(sumt[i])):
        doc=doc+" "+sumt[i][j]
    x_doc.append(doc)

#TF-IDF
tivec=tfidf()
x=tivec.fit_transform(x_doc)
x=x.toarray()

#認識された文書と脚本を分割
x_train=x[0:int(len(x)/2)]
x_test=x[int(len(x)/2):len(x)]

out=[]
#脚本と入れ替え
for i in range(len(x_train)):
    num=0
    sim=np.dot(x_train[i],x_test[0]) / (np.linalg.norm(x_train[i]) * np.linalg.norm(x_test[0]))
    for j in range(len(x_test)):
        sim2=np.dot(x_train[i],x_test[j]) / (np.linalg.norm(x_train[i]) * np.linalg.norm(x_test[j]))
        if sim2>sim:
            num=j
            sim=sim2
    out.append(rm[num])

#修正した文書を保存
i=0
for path in glob.glob("folder/*.wav"):
    f=open("folder/"+path[6:]+".txt","w",encoding="shift-jis")
    f.write(out[i])
    f.close()
    i=i+1
