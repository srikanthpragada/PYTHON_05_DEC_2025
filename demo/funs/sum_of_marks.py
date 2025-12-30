data = "56,89,a,70"

# Split str using , to get marks in string form
marks = data.split(",")

# Select only valid marks (numbers)
valid_marks = filter(str.isdigit, marks)

# Convert each str to int and then get total
total = sum(map(int, valid_marks))
print(total)
