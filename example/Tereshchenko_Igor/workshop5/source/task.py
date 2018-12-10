def convert_2_dict(lst):
    if len(lst[0]) == 2:
        return {
            'quantity': lst[0][0],
            'price': lst[0][1]
        }
    dct = {}
    for sublst in lst:
        key = sublst[0]
        if key not in dct:
            dct[key] = []
        dct[key].append(sublst[1:])
    for key in dct:
        dct[key] = convert_2_dict(dct[key])
    return dct


with open('orders.csv', encoding='utf-8') as f:
    f.readline()
    file = [[el.strip() for el in line.split(',')] for line in f]
    result = convert_2_dict(file)
print(result)


def add_to_dict(dct, lst):
    if len(lst) == 3:
        dct[lst[0]] = {
            'quantity' : lst[1],
            'price': lst[2]
        }
        return dct
    key = lst[0]
    if key not in dct:
        dct[key] = {}
    add_to_dict(dct[key], lst[1:])
    return dct


from functools import reduce

with open('orders.csv', encoding='utf-8') as f:
    f.readline()
    def convert_str(s):
        return list(map(str.strip, s.split(',')))
    result = reduce(add_to_dict, map(convert_str, f), {})
print(result)

res = set()

for name, val1 in result.items():
    for date, val2 in val1.items():
        res = res.union(set(val2.keys()))

for name in result:
    client_products = set()
    for date in result[name]:
        client_products = client_products.union(set(result[name][date].keys()))
    res = res.intersection(client_products)
print(res)

apples = {}

import plotly.offline as pl
import plotly.graph_objs as go

for _, dates in result.items():
    for date, products in dates.items():
        for prod, chars in products.items():
            if prod == 'apple':
                apples[date] = chars['price']

print(apples)

xs = sorted(list(apples.keys()))
ys = [apples[key] for key in xs]

pl.plot({
    'data' : [go.Scatter(
        x=xs,
        y=ys
    )]
})
# Створити dataset та працювати з ним

# Які продукти купляли усі покупці?

# Як змінювалась ціна на яблука? (графік)

# Скільки грошей витрачає кожний покупець на покупки? (графік)

# Який найпопулярніший товар?

# Якого товару було куплено найменше?

# Який найдорожчий товар?

# Якого товару, скільки покупців купляє? (графік)

# Написати функціонал для додавання нових даних
