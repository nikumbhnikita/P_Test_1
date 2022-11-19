#Q.28 Write a code to get the desired output of the following
# string = "Big Data iNeuron"
# desired_output = "iNeuron"
string = "Big Data iNeuron"
print(len(string))
print(string[9:17])

# Q.29Write a code to get the desired output of the following
# string = "Big Data iNeuron"
# desired_output = "norueNi"
print(string[-1:-8:-1])

#Q30. Resverse the string given in the above question
print(string[-1:-17:-1])

#Q31. How can you delete entire string at once?
# s3="Niki"
# #del s3[1]- # string is immutable, we cant add or delete item from list
# del s3
# print(s3)

# Q33. How can you print the below string?
# 'iNeuron's Big Data Course'
# s= "iNeuron's Big Data Course"
# print(s)

#Q86. Write a Python program to check if a string is palindrome or not.
# s="radar"
# if s==s[-1::-1]:
#     print("string is palindrome")
# else:
#     print("string is not palindrome")


#Q87. Write a Python program to remove i'th element from a string.
# s1="Nikita Nikumbh"
# print("original string :",s1)
# s2=s1.replace('i', '')
# print("string after removal of element :",s2)

#Q88. Write a Python program to check if a substring is present in a given string.
ss="Big Data Course"
print("String is :",ss)
if 'Data' in ss:
    print("yes, substring is present")
else:
    print("no, substring is not present")


