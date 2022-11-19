#Q47. Create a set and add "iNeuron" in your set.
s={1,2}
s.add("iNeuron")
print(s)

#Q48. Try to add multiple values using add() function.
s.add(7)
s.add(10)
#s.add(10,20,30)  # add takes only one argument 
s.update(range(5)) # update takes multiple iterable arguments 
print(s)


