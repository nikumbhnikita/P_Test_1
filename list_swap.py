#Q82. Write a Python program to interchange the first and last element in a list.
# list =[1,2,5,6,7]
# print("list before intercahnge",list)
# temp=list[0]
# list[0]=list[4]
# list[4]=temp
# print("list after intercahnge",list)

#Q83. Write a Python program to swap two elements in a list.
# list1=[1,2,5,6,7]
# list2=[10,20,30,40]
# print("list1 before swap",list1)
# print("list2 before swap",list2)
# list3=[]
# list3=list1
# list1=list2
# list2=list3
# print("list1 after swap",list1)
# print("list2 after swap",list2)

#Q84. Write a Python program to find N largest element from a list.
# l=[10,20,30,40,]
# print(max(l))

#Q85. Write a Python program to find cumulative sum of a list.
ll=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  
print("list is",ll)
cum_list=[]
sum=0
for i in range(0,len(ll)):
    sum=sum+ll[i]
    cum_list.append(sum)
print("cumulative sum of list",cum_list)






