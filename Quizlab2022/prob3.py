#Problem3 Labquiz2022
ints = input("Integer inputs: ").split()
pnums = [i for i in ints if int(i) > 0]
group_total = {}
group_value = {}
for i in pnums: #This i is each positive number
    if i[-1] not in group_total: #i[-1] is the last digit
        group_total[i[-1]] = 1
        group_value[i[-1]] = [int(i)]
    else:
        group_total[i[-1]] += 1
        group_value[i[-1]] += [int(i)]
for i in sorted(group_value.keys()): #key of group_value list
    for k,v in sorted(group_total.items()):
        if i == k:
            sort_value = sorted(group_value[i]) #list of sorted value of that digit group
            print("Group %s, Total %d, Values:"%(k,v),sort_value)
