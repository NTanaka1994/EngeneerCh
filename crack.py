f=open("pass2.txt","r")
pw=f.read()
c1=32
c2=32
c3=32
c4=32
c5=32
c6=32
flag=0
s=chr(c1)+chr(c2)+chr(c3)+chr(c4)+chr(c5)+chr(c6)
step=0
for a in range(126-32):
    s=chr(c1)+chr(c2)+chr(c3)+chr(c4)+chr(c5)+chr(c6)
    if flag==1:
        break
    if pw==s:
        flag=1
    else:
        if c1>126:
            c1=32
        c1=c1+1
    for b in range(126-32):
        s=chr(c1)+chr(c2)+chr(c3)+chr(c4)+chr(c5)+chr(c6)
        if flag==1:
            break
        if pw==s:
            flag=1
        else:
            if c2>126:
                c2=32
            else:
                c2=c2+1
        for c in range(126-32):
            s=chr(c1)+chr(c2)+chr(c3)+chr(c4)+chr(c5)+chr(c6)
            if flag==1:
                break
            if pw==s:
                flag=1
            else:
                if c3>126:
                    c3=32
                else:
                    c3=c3+1
            for d in range(126-32):
                s=chr(c1)+chr(c2)+chr(c3)+chr(c4)+chr(c5)+chr(c6)
                if flag==1:
                    break
                if pw==s:
                    flag=1
                else:
                    if c4>126:
                        c3=32
                    else:
                        c4=c4+1
                for e in range(126-32):
                    s=chr(c1)+chr(c2)+chr(c3)+chr(c4)+chr(c5)+chr(c6)
                    if flag==1:
                        break
                    if pw==s:
                        flag=1
                    else:
                        if c5>126:
                            c5=32
                        else:
                            c5=c5+1
                    for f in range(126-32):
                        s=chr(c1)+chr(c2)+chr(c3)+chr(c4)+chr(c5)+chr(c6)
                        if flag==1:
                            break
                        if pw==s:
                            flag=1
                        else:
                            if c6>126:
                                c6=32
                            else:
                                c6=c6+1
print("PassCord:"+str(chr(c1)+chr(c2)+chr(c3)+chr(c4)+chr(c5)+chr(c6)))
