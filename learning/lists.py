# lists
line = [2, 1, 5, 6, 3, 4, 11]

# functions
len(line) #7 lenght of
min(line) #1 max value
max(line) #11 min value
sum(line) #32 sum whole list
sorted(line) #[1, 2, 3, 4, 5, 6, 11] sorted

#slices
line[0:2] # [2, 1]
line[2:4] # [5, 6]
line[4:6] # [3, 4]
line[0:7] # [2, 1, 5, 6, 3, 4, 11]
line[2:] # [5, 6, 3, 4, 11]
line[:2] # [2, 1]
line[:] # [2, 1, 5, 6, 3, 4, 11]

#methods
line.append(8) # [2, 1, 5, 6, 3, 4, 11, 8]
line.pop() # [2, 1, 5, 6, 3, 4] (returns lalue to list then remove it)
