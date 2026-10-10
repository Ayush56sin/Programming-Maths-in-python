sum =0
count= 0
for i in range(1,100000):
    if i % 2 ==0:
        continue
    else:
        j=1/i
    count +=1
    if count % 2 == 1:
        sum += j
    else:
        sum -= j
print(4*sum)

