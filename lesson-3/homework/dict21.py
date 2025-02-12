d = {"b": 2, "a": 3, "c": 1}  

sorted_value = dict(sorted(d.items(), key=lambda item: item[1]))  

print(sorted_value)