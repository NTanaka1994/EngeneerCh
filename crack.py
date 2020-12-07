import zipfile
c=[]
for i in range(127-32):
    c.append(chr(i+32))
s=chr(ord(c[0]))+chr(ord(c[0]))+chr(ord(c[0]))#+chr(ord(c[0][0]))+chr(ord(c[0][0]))
flag=0

path="履歴書.zip"
for i in range(len(c)):
    if flag==1:
        break
    for j in range(len(c)):
        if flag==1:
            break
        for k in range(len(c)):
            s=chr(ord(c[i]))+chr(ord(c[j]))+chr(ord(c[k]))
            if flag==1:
                break
            else:
                try:
                    with zipfile.ZipFile(path,"r") as zip_file:
                        zip_file.extractall(path=".", pwd=s.encode("utf-8"))
                    flag=1
                except:
                    flag=0
                    """
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
print("PASSWORD:"+chr(ord(c[i-1]))+chr(ord(c[j-1]))+chr(ord(c[k-1])))#+chr(ord(c[0][l-1])))#+chr(ord(c[0][m-1]))+chr(ord(c[0][n-1])))
