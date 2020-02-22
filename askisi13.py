try:
    num=input("δωσε 16 εξαψιφιο αριθμο καρτας")
except ValueError:
    print("αυτο που εδωσες δεν ηταν αριθμος")
    num=input("δωσε ξανα 16 ψιφιο αριθμος καρτας ")
sum1=0
sum2=0
finsum=0
num=str(num)
for i in range(1,16,2):
    sum1+=int(num[i])
for i in range(0,16,2):
    if int(num[i])*2>9:
        sum2+=int((int(num[i])*2)/10)+int((int(num[i])*2)%10)
    else:
        sum2+=int(num[i])*2
finsum=sum1+sum2
if finsum%10==0:
    print("Εγκηρος αριθμος καρτας")
else:
    print("μη εγκηρος αριθμος καρτας")
