def shortest_subString(str,minLength):
    subString=[]
    for x in range(0,len(str)-1):
        for y in range(x+minLength-1,len(str)):
            if str[x]==str[y] and y-x+1 >= minLength:
                tempString=str[x:y+1]
                if not subString or len(tempString) < len(subString[0]):
                    subString=[tempString]
                    if len(tempString)==len(str):
                        return "not-found"
                elif len(tempString)==len(subString[0]):
                    subString.append(tempString)
    return subString

Sentance=input("enter string:\t")
minLength=int(input("enter minimun length:\t"))

print(shortest_subString(Sentance,minLength))

# abccdbacca
# 0123456789