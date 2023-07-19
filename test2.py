# Open the text file
with open('hand.txt', 'r') as file:
    # Read all lines from the file
    lines = file.readlines()

    # Print each line
    for line in lines:
        print(line.strip())  # Use strip() to remove any trailing newline characters
