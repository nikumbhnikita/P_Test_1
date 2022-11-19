#Q90. Write a Python program to extract unquire dictionary values.
# d={1:100,2:200,3:400,4:100,5:500}
# print(d)
# print(d.values())


#Q91. Write a Python program to merge two dictionary.
# d1={1:100,2:200,3:400,4:100,5:500}
# d2={10:'nn',20:'kk',30:'aa'}
# print("Dictionary-1 :",d1)
# print("Dictionary-2 :",d2)
# d3=d1.copy()
# d3.update(d2)
# print("Dictionary after merging:",d3)




# Q92. Write a Python program to convert a list of tuples into dictionary.
# Input : [('Sachin', 10), ('MSD', 7), ('Kohli', 18), ('Rohit', 45)]
#  Output : {'Sachin': 10, 'MSD': 7, 'Kohli': 18, 'Rohit': 45}
# Input = [('Sachin', 10), ('MSD', 7), ('Kohli', 18), ('Rohit', 45)]
# print("list of tuples :",Input)
# print(type(Input))
# Output=dict(Input)
# print("List convesrion to dictionary",Output)
# print(type(Output))

# print(20/6)
# print(20//6)

#Q58. What will the output of the following?
var = {}
print(type(var))

#Q60. Create a dictionary and access all the values in that dictionary.
# d={100:"nikita",200:"amol",300:"shiva"}
# print(d.values())
# for v in d.values():
#     print(v)

#Q61. Create a nested dictionary and access all the element in the inner dictionary.
d1={100:"nikita",200:"amol",300:{1:"nn",2:"pp"}}
print(d1)
print(d1[300][2])
