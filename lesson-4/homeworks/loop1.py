list1 = [1, 2, 8]
list2 = [3, 5, 6, 7]
uncommon_list = []
for item in list1:
    if item not in list2:
        uncommon_list.append(item)

for item in list2:
    if item not in list1:
        uncommon_list.append(item)
uncommon_list.sort()
print(uncommon_list)