dictionary_goods = [ 
    {
    "id": 0,
    "name": "яблоко",
    "category": "фрукты",
    "price": 2000,
    "quantity": 30
    },
    {
    "id": 1,
    "name": "груша",
    "category": "фрукты",
    "price": 7000,
    "quantity": 10
    },
    {
    "id": 2,
    "name": "помэла",
    "category": "фрукты",
    "price": 20000,
    "quantity": 3
    },
    {
    "id": 3,
    "name": "тыква",
    "category": "овощи",
    "price": 1000,
    "quantity": 300
    },
    {
    "id": 4,
    "name": "огурец",
    "category": "овощи",
    "price": 4000,
    "quantity": 35
    },
    {
    "id": 5,
    "name": "помидор",
    "category": "овощи",
    "price": 100,
    "quantity": 0
    },
    {
    "id": 6,
    "name": "баклажан",
    "category": "овощи",
    "price": 300,
    "quantity": 340
    } 
]
no_quantity =[]
low_quantity=[]
else_quantity=[]
for item in dictionary_goods:
    if item['quantity'] == 0:
        no_quantity.append(item['name'])
    elif item['quantity'] < 5:
        low_quantity.append(item['name'])
    else:
        else_quantity.append(item['name'])

price = 0

for item in dictionary_goods:
    print(f"id {item['id']} название {item['name']} категория {item['category']} цена {item['price']} кол-во {item['quantity']}")
    
    price += item['price'] * item['quantity']

print(f"общая стоимость товаров {price} рублей")

search = input("введите свой товар который хотите ").lower()

found = []

for item in dictionary_goods:
    if search in item['name'].lower():
        found.append(item)

if found:
    for item in found:
        print(f"id {item['id']} имя {item['name']} категория {item['category']} цена {item['price']} кол-во {item['quantity']}")
else:
    print('нет таких товаров')

print(set(good["category"] for good in dictionary_goods))

search = input("введите категорию ").lower()
for item in dictionary_goods:
    if search in item['category'].lower():
        found.append(item)
if found:
    for item in found:
        print(f"id {item['id']} имя {item['name']} категория {item['category']} цена {item['price']} кол-во {item['quantity']}")
else:
    print('нет таких категорий')

