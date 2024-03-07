import json
def create_cook_book(file_path):
    cook_book = {}

    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        dish_name = ''
        ingredients = []

        for line in lines:
            line = line.strip()
            if not line:
                continue

            if dish_name == '':
                dish_name = line
            elif '|' in line:
                ingredient_info = line.split(' | ')
                ingredient = {
                    'ingredient_name': ingredient_info[0],
                    'quantity': int(ingredient_info[1]),
                    'measure': ingredient_info[2]
                }
                ingredients.append(ingredient)
            else:
                cook_book[dish_name] = ingredients
                dish_name = line
                ingredients = []

        cook_book[dish_name] = ingredients

    return cook_book

cook_book = {
    'Омлет': [
        {'ingredient_name': 'Яйцо', 'quantity': 2, 'measure': 'шт.'},
        {'ingredient_name': 'Молоко', 'quantity': 100, 'measure': 'мл'},
        {'ingredient_name': 'Помидор', 'quantity': 2, 'measure': 'шт'}
    ],
    'Утка по-пекински': [
        {'ingredient_name': 'Утка', 'quantity': 1, 'measure': 'шт'},
        {'ingredient_name': 'Вода', 'quantity': 2, 'measure': 'л'},
        {'ingredient_name': 'Мед', 'quantity': 3, 'measure': 'ст.л'},
        {'ingredient_name': 'Соевый соус', 'quantity': 60, 'measure': 'мл'}
    ],
    'Запеченный картофель': [
        {'ingredient_name': 'Картофель', 'quantity': 1, 'measure': 'кг'},
        {'ingredient_name': 'Чеснок', 'quantity': 3, 'measure': 'зубч'},
        {'ingredient_name': 'Сыр гауда', 'quantity': 100, 'measure': 'г'}
    ],
    'Фахитос': [
        {'ingredient_name': 'Говядина', 'quantity': 500, 'measure': 'г'},
        {'ingredient_name': 'Перец сладкий', 'quantity': 1, 'measure': 'шт'},
        {'ingredient_name': 'Лаваш', 'quantity': 2, 'measure': 'шт'},
        {'ingredient_name': 'Винный уксус', 'quantity': 1, 'measure': 'ст.л'},
        {'ingredient_name': 'Помидор', 'quantity': 2, 'measure': 'шт'}
    ]
}

formatted_cook_book = json.dumps(cook_book, ensure_ascii=False, indent=4)
print(formatted_cook_book)