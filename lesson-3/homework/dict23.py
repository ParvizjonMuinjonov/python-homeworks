d1 = {"a": 1, "b": 2, "c": 3}  
d2 = {"c": 4, "d": 5, "e": 6}  


common_keys = (d1.keys() & d2.keys())  
print(bool(common_keys))  

