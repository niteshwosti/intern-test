num=0
for i in range (9999,100,-1):
    for j in range (i,100,-1):
        prod=i*j
        if  prod > num:
            z=str(i*j)
            if z==z[::-1]:
                num=i*j
print (num)
    