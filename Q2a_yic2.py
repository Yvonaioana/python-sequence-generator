# Generate the  sequence

# Initialise the inputs
a = 8        # first value of the sequence
d = 7        # difference between values
n = 10       # number of values

#  Set value to the first value of the sequence
value = a

#  Set sequence to the empty list
sequence = []

#  Set a counter to 1
counter = 1

#  Append value to the sequence
sequence.append(value)

#  While the counter is less than 10
while counter < 10:

     #  Set value to the next value of the sequence
    value = value + d

     #  Append value to the sequence
    sequence.append(value)

     # Increase the counter by 1
    counter = counter + 1

# Step 7: Print the sequence
print(sequence)
