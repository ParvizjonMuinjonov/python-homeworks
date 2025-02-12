d = {"a": 2, "b": 3, "c": 2, "d": 4, "e": 2}  
value = 2  

keys = list(filter(lambda k: d[k] == value, d))  
print(keys)