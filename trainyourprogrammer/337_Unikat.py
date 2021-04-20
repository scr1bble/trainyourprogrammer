#a = "der pfannkuchen schmeckt süß"
#b = "der pfannkuchen schmeckt salzig"

#a = "apfel apfel"
#b = "BANANA"

#a = "so viele tolle menschen"
#b = "so viele dumme affen"

#a = "ich bin cool"
#b = "ich bin cool"

listea = a.split(" ")
listeb = b.split(" ")

tmp = []
for e in listea:
    if e in listeb:
        pass
    else:
        tmp.append(e)

for e in listeb:
    if e in listea:
        pass
    else:
        tmp.append(e)


print(tmp)
