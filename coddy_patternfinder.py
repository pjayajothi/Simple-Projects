#Create a function named find_occurrences that:
  #Takes two string arguments: text and pattern
  #Counts how many times pattern appears in text, including overlapping occurrences
  #Returns a tuple containing:
    #A boolean indicating if the pattern was found (True/False)
    #The number of occurrences of the pattern
    #A list of starting positions where the pattern was found

def find_occurrences(text, pattern):
    # Write your code here
    positions = []
    i = 0
    while i <= len(text) - len(pattern):
        if text[i:i+len(pattern)] == pattern:
            positions.append(i)
        i += 1  # Move by 1 to allow overlapping
    found = bool(positions)
    count = len(positions)
    return (found, count, positions)

# Read input
text = input()
pattern = input()

# Call your function and print the result
result = find_occurrences(text, pattern)
print(result)
