sentence = input("Enter a sentence: ")

words = sentence.split()
acronym_word = "".join(word[0].upper() for word in words)

print(acronym_word)