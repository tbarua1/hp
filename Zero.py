import random
pos=0
apos=0.0
sum=0
avg=0.0
noe=0
cnt=0
noe=input("Enter number of experiments: ")
steps=input("Enter number of steps per experiment: ")
print("Performing experiments...")
for a in range(0,noe):
    for i in range(0,steps):
        j=random.randint(0,1)
        if j==1:
            pos+=1
        else:
            pos-=1
    sum=sum+abs(pos)
    apos=abs(pos)*1.0
    if apos==(0.9*(steps**(0.5))):
        cnt=cnt+1
    pos=0
noe=noe*1.0
avg=sum/noe
print("Expected value of distance: %d"%(steps**(0.5)))
print("Number of experiments agreeing with the theory = %d"%cnt)
print("Absolute average distance: "+ str(avg))
if cnt>=(noe-cnt):
    print("The average experiment satisfies the theory.")
else:
    print("The average experiment disagrees with the theory.")