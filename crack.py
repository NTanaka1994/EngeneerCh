import zipfile
c1=32
c2=32
c3=32
flag=0
s=chr(c1)+chr(c2)+chr(c3)
path="obj.zip"
for i in range(126-32):
    s=chr(c1)+chr(c2)+chr(c3)
    if flag==1:
        break
    try:
        with zipfile.ZipFile(path, 'r') as zip_file:
            zip_file.extractall(path=".", pwd=s.encode("utf-8"))
        flag=1
    except:
        if c1>126:
              c1=32
        else:
            c1=c1+1
    for j in range(126-32):
        s=chr(c1)+chr(c2)+chr(c3)
        if flag==1:
            break
        try:
            with zipfile.ZipFile(path, 'r') as zip_file:
                zip_file.extractall(path=".", pwd=s.encode("utf-8"))
            flag=1
        except:
            if c2>126:
                c2=32
            else:
                c2=c2+1
        for k in range(126-32):
            s=chr(c1)+chr(c2)+chr(c3)
            if flag==1:
                break
            try:
                with zipfile.ZipFile(path, 'r') as zip_file:
                    zip_file.extractall(path=".", pwd=s.encode("utf-8"))
                flag=1
            except:
                if c3>126:
                    c3=32
                else:
                    c3=c3+1
                    #print(s)
print("PassCord:"+str(chr(c1)+chr(c2)+chr(c3)))#+chr(c4)))#+chr(c5)+chr(c6)))
