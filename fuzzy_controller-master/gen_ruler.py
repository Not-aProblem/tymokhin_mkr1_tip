import itertools

from model import input_lvs

data = dict()
j = []
for value in input_lvs:
    data[value["name"]] = [t for t in value["terms"]]
    j.append(value["name"])


print(j)


value = {
    "Quality_of_service": lambda x: 6 + x * -2,
    "Quality_of_dishes": lambda x: 1 + -(1 ** (x + 1))
}


rez = []
rez2 = []
for tupl in tuple(itertools.product(*[data[i] for i in data])):
    t = 0
    for index, param in enumerate(data):
        t += value[param](data[param].index(tupl[index]))
    rez2.append(t)
    t2 = (tupl, "low")
    if t > 3:
        t2 = (tupl, "medium")
    if t > 5:
        t2 = (tupl, "high")

    rez.append(t2)


print(rez)
print(rez2)