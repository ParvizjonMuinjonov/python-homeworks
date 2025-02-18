import string
ignoring_char = string.punctuation
def count_word(func):
    def wrapper():
        words_count = {}
        try:
            with open("sample.txt", "r") as file:
                
                words = file.read()
                for char in ignoring_char:
                    words = words.replace(char, "")
                
                words_lowered = words.lower()
                every_word = words_lowered.split()
                print(f"Total words: {len(every_word)}")
                for word in every_word:
                    words_count[word] = words_count.get(word, 0) + 1
                try:
                    a = int(input("Enter the number of top words you want to see: "))
                    if a <= 0:
                        print("Please enter a positive number")
                        return
                except ValueError:
                    print("Please enter only number")
                    return
                top_words = sorted(words_count.items(), key=lambda x: x[1], reverse=True)[:a]
                with open("word_count_report.txt", "wt") as another_file:
                    another_file.write(f"Total words: {len(every_word)}\n")
                    another_file.write(f"Top {a} common words:\n")
                    print(f"Top {a} common words:\n")
                    for word, count in top_words:
                        another_file.write(f"{word} - {count} times\n")
                        print(f"{word} - {count} times")
                
                

        except FileNotFoundError:
            print("sample.txt was not found")
       
           
        
        func()
        

    return wrapper


@count_word

def final_process():
    print("Counting words finished")
    


final_process()














