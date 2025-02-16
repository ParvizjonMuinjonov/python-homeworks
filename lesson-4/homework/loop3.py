txt = input("Enter a word: ")
vowels = "AEIOUaeiou"
result = []
count = 0
i = 0

while i < len(txt):
    result.append(txt[i])
    count += 1

    if count == 3:
        if txt[i] in vowels or (i + 1 < len(txt) and txt[i + 1] == "_"):
            if i + 1 < len(txt):
                result.append(txt[i + 1])
                i += 1
        if i + 1 < len(txt):
            result.append("_")
        count = 0 
    i += 1

modified_txt = "".join(result)
print(modified_txt)
