import zipfile

c=["abcdefghijklmnopqrstuvwxyz1234567890"]
s=chr(ord(c[0][0]))+chr(ord(c[0][0]))+chr(ord(c[0][0]))+chr(ord(c[0][0]))#+chr(ord(c[0][0]))+chr(ord(c[0][0]))
flag=0
path="履歴書.zip"
for i in range(len(c[0])):
    print(c[0][i])
    if flag==1:
        break
    for j in range(len(c[0])):
        if flag==1:
            break
        for k in range(len(c[0])):
            if flag==1:
                break
            for l in range(len(c[0])):
                s=chr(ord(c[0][i]))+chr(ord(c[0][j]))+chr(ord(c[0][k]))+chr(ord(c[0][l]))
                if flag==1:
                    break
                else:
                    #print(s)
                    try:
                        with zipfile.ZipFile(path,"r") as zip_file:
                            zip_file.extractall(path=".", pwd=s.encode("utf-8"))
                        flag=1
                    except:
                        flag=0
                """
                for m in range(len(c[0])):
                    if flag==1:
                        break
                    for n in range(len(c[0])):
                        s=chr(ord(c[0][i]))+chr(ord(c[0][j]))+chr(ord(c[0][k]))+chr(ord(c[0][l]))+chr(ord(c[0][m]))+chr(ord(c[0][n]))
                        if flag==1:
                            break
                        else:
                            #print(s)
                            try:
                                with zipfile.ZipFile(path,"r") as zip_file:
                                    zip_file.extractall(path=".", pwd=s.encode("utf-8"))
                                flag=1
                            except:
                                flag=0
                                """
print("PASSWORD:"+chr(ord(c[0][i-1]))+chr(ord(c[0][j-1]))+chr(ord(c[0][k-1]))+chr(ord(c[0][l-1])))#+chr(ord(c[0][m-1]))+chr(ord(c[0][n-1])))
