dictionary_goods = [ 
    {
    "id": 0,
    "name": "яблоко",
    "category": "фрукты",
    "price": 100,
    "quantity": 30
    },
    {
    "id": 1,
    "name": "груша",
    "category": "фрукты",
    "price": 250,
    "quantity": 10
    },
    {
    "id": 2,
    "name": "помэла",
    "category": "фрукты",
    "price": 600,
    "quantity": 3
    },
    {
    "id": 3,
    "name": "тыква",
    "category": "овощи",
    "price": 500,
    "quantity": 300
    },
    {
    "id": 4,
    "name": "огурец",
    "category": "овощи",
    "price": 150,
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

def group_by_quantity(goods):
    no_quantity = []
    low_quantity = []
    else_quantity = []

    for item in goods:
        if item['quantity'] == 0:
            no_quantity.append(item['name'])
        elif item['quantity'] < 5:
            low_quantity.append(item['name'])
        else:
            else_quantity.append(item['name'])

    print("Товары без остатка:", no_quantity)
    print("Товары с низким остатком (<5):", low_quantity)
    print("Остальные товары:", else_quantity)


def print_all_and_total_price(goods):
    total_price = 0
    for item in goods:
        print(f"id {item['id']} название {item['name']} категория {item['category']} цена {item['price']} кол-во {item['quantity']}")
        total_price += item['price'] * item['quantity']

    print(f"Общая стоимость всех товаров: {total_price} рублей")
    return total_price

def search_by_name(goods):
    search = input("Введите название товара для поиска: ").lower()
    found = []
    for item in goods:
        if search in item['name'].lower():
            found.append(item)

    if found:
        for item in found:
            print(f"id {item['id']} имя {item['name']} категория {item['category']} цена {item['price']} кол-во {item['quantity']}")
    else:
        print('Нет таких товаров')
    return found


def show_categories(goods):
    print("Доступные категории:", set(good["category"] for good in goods))


def search_by_category(goods):
    search = input("Введите категорию для поиска: ").lower()
    found = []
    for item in goods:
        if search in item['category'].lower():
            found.append(item)

    if found:
        for item in found:
            print(f"id {item['id']} имя {item['name']} категория {item['category']} цена {item['price']} кол-во {item['quantity']}")
    else:
        print('Нет товаров в такой категории')
    return found


def update_quantity(goods, action):
    try:
        target_id = int(input("Введите ID товара для обновления количества: "))
        item_found = None
        for item in goods:
            if item["id"] == target_id:
                item_found = item
                break

        if not item_found:
            print("Товар с таким ID не найден.")
            return

        if action == "add":
            new_quantity = int(input("Введите новое значение количества: "))
            item_found["quantity"] = new_quantity
            print(f"Успешное обновление. Новое количество: {new_quantity}")
        elif action == "sell":
            selling = int(input("Введите количество для продажи: "))
            if selling <= item_found["quantity"]:
                item_found["quantity"] -= selling
                print(f"Успешно продано: {selling} штук!")
            else:
                print("Недостаточно товара на складе.")
                return

        print(f"id {item_found['id']} имя {item_found['name']} категория {item_found['category']} цена {item_found['price']} кол-во {item_found['quantity']}")

    except ValueError:
        print("Пожалуйста, вводите корректные числа.")


def show_stats(goods):
    fruits_quantity = 0
    veg_quantity = 0
    max_price = 0
    min_price = 0

    for item in goods:
        if item["category"] == "фрукты":
            fruits_quantity += item["quantity"]
        elif item["category"] == "овощи":
            veg_quantity += item["quantity"]

    all_quantity = sum(item["quantity"] for item in goods)
    all_price = sum(item["price"] * item["quantity"] for item in goods)
    max_price += max(item["price"] for item in goods)
    min_price += min(item["price"] for item in goods)
        
    category_totals = {}
    
    for item in goods:
        cat = item["category"]
        qty = item["quantity"]
        if cat not in category_totals:
            category_totals[cat] = 0
        category_totals[cat] += qty

    max_cat = max(category_totals, key=category_totals.get)
    max_qty = category_totals[max_cat]
    average_price = sum(item["price"] for item in dictionary_goods) / len(dictionary_goods)

    fruit_prices = [item["price"] for item in dictionary_goods if item["category"].lower() == "фрукты"]
    veg_prices = [item["price"] for item in dictionary_goods if item["category"].lower() == "овощи"]

    avg_fruit_price = sum(fruit_prices) / len(fruit_prices) if fruit_prices else 0
    avg_veg_price = sum(veg_prices) / len(veg_prices) if veg_prices else 0
    

    print(f"Общее количество фруктов: {fruits_quantity}")
    print(f"Общее количество овощей: {veg_quantity}")
    print(f"Общее количество всех товаров: {all_quantity}")
    print(f"Общая стоимость всех товаров: {all_price} рублей")
    print(f"Самая большая цена: {max_price}")
    print(f"Самая мелкая цена: {min_price}")
    print(f"Средняя цена товаров Фрукты: {avg_fruit_price}")
    print(f"Средняя цена товаров Овощи: {avg_veg_price}")
    print(f"Средняя цена товара вообщем {average_price}")
    print(f"Категория с наибольшим количеством единиц: {max_cat} ({max_qty} шт.)")
    return max_cat, max_qty



group_by_quantity(dictionary_goods)
print_all_and_total_price(dictionary_goods)
search_by_name(dictionary_goods)
show_categories(dictionary_goods)
search_by_category(dictionary_goods)

print("Хотите внести изменения?")
a = input("да или нет: ").lower()
if a in ("да", "lf", "д"):
    b = input("1 — пополнить товар, 2 — продать товар, 3 — статистика: ")

    if b == "1":
        update_quantity(dictionary_goods, "add")
    elif b == "2":
        update_quantity(dictionary_goods, "sell")
    elif b == "3":
        show_stats(dictionary_goods)
    else:
        print("неверно!!!")
else:
    print("ок")