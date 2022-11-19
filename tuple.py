# string="Nikita Nikumbh"
# print(string[0])

#Q43. Can two tuple be appended. If yes, write a code for it. If not, why?
t1=(10,20,30)
t2=(50,60,70)
print(t1+t2) #concate operator

#Q44. Take a tuple as an input and print the count of elements in it.

t=eval(input("enter the tuple:"))
count=0
for i in t:
    count=count+1
print("elements in tuple",count)
    