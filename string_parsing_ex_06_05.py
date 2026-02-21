# string_parsing
# This code extracts a float from a string using find and slicing

# Given string for the exercise
text_str = 'X-DSPAM-Confidence: 0.8475'

# Find the position of the colon in the sting
ipos = text_str.find(':')

# Slice the string to extract the portion after the colon
# Adding 2 to the index skips the colon and the space immediately following it
piece = text_str[ipos +2:]

# convert the extracted string piece into a floating-point number
value = float(piece)

# Print the final floating-point value
print(value)