Logic:
pushing all the input string characters until we get ] , then evaluate each block. and continue 
:: similar to Post fix evaluation kind of.


strip=input("Enter format string :> ")
stlist=[]
j=0
k=""
num=0
tempstr=""
x=''
for i in range(len(strip)):
    x = strip[i]
    if(x.isdigit()):
        num = num*10 + int(x)
        if(strip[i+1].isdigit()):
            continue
        else:
            stlist.append(num)
            num=0
    elif(x == '['):
        stlist.append(x)
        if(strip[i+1].isdigit()):
            continue
    elif(x==']'):
        j=len(stlist)-1
        while(1):
            if(isinstance(stlist[j],str) and stlist[j]!= '['):
                tempstr =  stlist[j] + tempstr
                j = j-1
                stlist.pop()
            elif(stlist[j]=='['):
                stlist.pop()
                j = j-1
                if(isinstance(stlist[j],int)):
                    num=stlist[j]
                    stlist.pop()
                    j=j-1
                    if(num>0):
                        tempstr = tempstr * num
                break
        stlist.append(tempstr)
        tempstr=""
        num=0
    else:
        while(1):
            
            k = k + strip[i]
            i=i+1
            if(i>=len(strip)-1 or strip[i+1]!=']' or strip[i+1]!= '[' or strip[i+1].isdigit() ):
                break
        if(k!=""):
            stlist.append(k)
            k=""
    #print(stlist)
stout=""
for i in stlist:
    stout = stout + i
print(stout)



