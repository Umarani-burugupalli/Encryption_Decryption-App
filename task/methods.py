global alphs
alphs="abcdefghijklmnopqrstuvwxyz"
def reverse(a):
    return a[::-1]
def Encryption(text,depth):
    rawtext=text
    len_text=len(text)
    text=reverse(text)
    cipher_text=""
    for i in text:
        if i==" ":
            cipher_text+=" "
        else:
            pos=alphs.index(i)
            value=(pos+len_text)%26
            cipher_text+=alphs[value]
    cipher_text=reverse(cipher_text)
    railfence=[]
    for _ in range(depth):
        l=[]
        for _ in range(len_text):
            l.append("*")
        railfence.append(l)
    a,b,c,up=0,0,0,0
    while(c<len_text):
        railfence[b][a]=cipher_text[a]
        a+=1
        c+=1
        if(up==0 and b<depth-1):
            b+=1
        elif(up==0 and b==depth-1):
            b-=1
            up=1
        elif(up==1 and b>0):
            b-=1
        elif(up==1 and b==0):
            b+=1
            up=0
    Encryp_text=""
    for i in range(depth):
        for j in range(len_text):
            if (railfence[i][j]!="*"):
                Encryp_text+=railfence[i][j]
    Encryp_text=reverse(Encryp_text)
    return Encryp_text
def Decryption(text,depth):
    d_r_text=reverse(text)
    length=len(d_r_text)
    railfence = []
    for _ in range(depth):
        l=[]
        for _ in range(length):
            l.append("*")
        railfence.append(l)
    a,b,c,l,up,pos=0,0,0,0,0,0
    while(c<depth*length):
		    if (l==b):
		        railfence[b][a]=d_r_text[pos]
		        pos=pos+1
		    a=a+1
		    c=c+1
		    if(up==0 and b<depth-1):
		        b=b+1
		    elif(up==0 and b==depth-1):
		        b=b-1
		        up=1
		    elif(up==1 and b>0):
		        b=b-1
		    elif(up==1 and b==0):
		        b=b+1
		        up=0
		    if (a==length):
		        a=0
		        b=0
		        l=l+1
    rev_rf_text=""
    a,b,c,up=0,0,0,0
    while(c<length):
        rev_rf_text+=railfence[b][a]
        a=a+1
        c=c+1
        if(up==0 and b<depth-1):
            b=b+1
        elif(up==0 and b==depth-1):
            b=b-1
            up=1
        elif(up==1 and b>0):
            b=b-1
        elif(up==1 and b==0):
            b=b+1
            up=0
    rev1_rf_text=reverse(rev_rf_text)
    decrypted_text=""
    for i in range(length):
        if rev1_rf_text[i]==" ":
            decrypted_text+=" "
        else:
            pos1=alphs.index(rev1_rf_text[i])
            value=(pos1-length)%26
            if(value<0):
                value+=26
            value=(value)%26
            decrypted_text+=alphs[value]
    decrypted_text=reverse(decrypted_text)
    return decrypted_text
