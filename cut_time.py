from moviepy.editor import *
import numpy as np
import librosa
import matplotlib.pyplot as plt
import subprocess

#mp4ファイルをwavファイルに変換
cmd=r'ffmpeg -i YuukiMovie/sample.mp4 YuukiMovie/sample.wav'
subprocess.call(cmd)

#wavファイルの読み込み
a,sr=librosa.load("YuukiMovie/sample.wav")

#デシベル計算
D=librosa.stft(a)
S,phase=librosa.magphase(D)
Sdb=librosa.amplitude_to_db(S)

#カットする音声の選出
interval=librosa.effects.split(a,top_db=max(Sdb.ravel())*1.75)
noSound=[]
tmp=[]
tmp.append(0)
tmp.append(interval[0][0])
noSound.append(tmp)
tmp=[]
for i in range(len(interval)-1):
    tmp.append(interval[i][1])
    tmp.append(interval[i+1][0])
    noSound.append(tmp)
    tmp=[]
print("無音区間")
for i in range(len(noSound)):
    print("開始位置:"+str(noSound[i][0]/sr)+"\t終了位置:"+str(noSound[i][1]/sr))

#動画の無音部分をカットして保存する
for i in range(len(interval)):
    video=VideoFileClip("YuukiMovie/sample.mp4").subclip(interval[i][0]/sr,interval[i][1]/sr)
    video.write_videofile("CutMovie/"+str(i+1)+".mp4",fps=29)
