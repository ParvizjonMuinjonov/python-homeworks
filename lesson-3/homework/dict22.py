d = {"a": 1, "b": 2, "c": 3, "e": 7},
{"a": 1, "b": 2, "c": 3, "e": 23},
{"a": 1, "b": 2, "c": 3, "e": 3}

filtered_values = [x for x in d if x["e"] > 7]

print(filtered_values)