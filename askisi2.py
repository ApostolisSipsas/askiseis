arxeio=input("δωσε αρχειο  :")
file=open(arxeio)
words=(file.read()).split()
fon="aeioyu"
badletters="fckr"
bad_count=0
good_count=0
good_or_bad_list=[]
for i in words:
    print (i)
    for j in i:
        if j not in fon:
            if j in badletters:
                bad_count+=1
            else:
                good_count+=1
    if bad_count > good_count:
        good_or_bad_list.append(i+"  : Κακη")
    else:
        good_or_bad_list.append(i+"  : Kαλη")
        print(1)
    bad_count=0
    good_count=0
file.close()
print (good_or_bad_list)
