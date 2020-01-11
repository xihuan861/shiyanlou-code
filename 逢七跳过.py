a = 0
while a<100:
    a = a+1
    if a%7==0:
        continue
    if a%10==7:
        continue
    if a//10==7:
        continue
    print(a)
