d = {"a": 1, "b": {"x": 10, "y": 20}, "c": 3}  


something = any(isinstance(v, dict) for v in d.values())  

print(something)