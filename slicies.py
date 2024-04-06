line=input("Enter a line :")
lowercount=uppertcount=0
digitcount=alphacount=0
for a in line:
    if a.lower():
        lowercount+=1
    elif a.upper():
        uppertcount+=1
    elif a.digit():
        digitcount+=1
    else:
        alphacount+=1
        print("Following are the",uppercount)   
        print("Following are the",lowercount)   
        print("Following are the",digitcount)   
        print("Following are the",alphacount)   