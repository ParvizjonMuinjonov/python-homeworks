sentence = input("Enter a sentence: ")
change_word = input("Enter a word you want to change: ")
new_word = input("Enter a new word: ")

new_sentence = sentence.replace(change_word, new_word)

print(new_sentence)