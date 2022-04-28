print("Enter some words for the program ")
line = input()
#have to add a + 1 to count the last word. .count() only counts words with white space behind them
total_words = line.count(' ') + 1
print("The total words you entered is ", total_words)
print("This is your sentence in all upper case", line.upper())
print("This is your sentence with the letter A removed", line.strip('a'))