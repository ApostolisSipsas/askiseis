arxeio=input("δωσε αρχειο  :")
file=open(arxeio)
data=file.read()
words=data.split()
def takeOf(value):
    word=""
    pho="αιεοωηυ"
    for i in range(len(value)):
        if value[i] not in pho:
            word+=value[i]
    return word

top5=[]
for j in range(5):
    maxlen=0
    for i in range(len(words)):
        if maxlen<len(words[i]):
            position=i
            maxlen=len(words[i])
    top5.append(words.pop(position))
for i in range(5):
    print(takeOf(top5[i][::-1]))
file.close()
