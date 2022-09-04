dict1 = {'ram':{'math':60, 'phy':45, 'chem':78},'shyam':{'math':60, 'phy':32, 'chem':78},'dinesh':{'math':60, 'phy':80, 'chem':78},}

phy_marks = []

for k,v in dict1.items():
    for k1,v1 in v.items():
        if k1 == 'phy':
            phy_marks.append(v[k1])

print(phy_marks)