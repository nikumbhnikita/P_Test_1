
x = [12, 75, 150, 180, 145, 525,50]
print(len(x))
for i in range(0,len(x),1) :
    if x[i]>150:
        continue
    if x[i]>500:
        break
    if x[i]%5==0:
        print("Numbers",x[i])