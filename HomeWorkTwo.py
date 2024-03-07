import json
def get_shop_list_by_dishes(dishes, person_count, cook_book):
    shop_list = {}

    for dish in dishes:
        for ingredient in cook_book[dish]:
            ingredient_name = ingredient['ingredient_name']
            quantity = ingredient['quantity'] * person_count
            measure = ingredient['measure']

            if ingredient_name not in shop_list:
                shop_list[ingredient_name] = {'measure': measure, 'quantity': quantity}
            else:
                shop_list[ingredient_name]['quantity'] += quantity

    return shop_list

json_data = '''
{
  "\u041a\u0430\u0440\u0442\u043e\u0444\u0435\u043b\u044c": {
    "measure": "\u043a\u0433",
    "quantity": 2
  },
  "\u041c\u043e\u043b\u043e\u043a\u043e": {
    "measure": "\u043c\u043b",
    "quantity": 200
  },
  "\u041f\u043e\u043c\u0438\u0434\u043e\u0440": {
    "measure": "\u0448\u0442",
    "quantity": 4
  },
  "\u0421\u044b\u0440 \u0433\u0430\u0443\u0434\u0430": {
    "measure": "\u0433",
    "quantity": 200
  },
  "\u042f\u0439\u0446\u043e": {
    "measure": "\u0448\u0442",
    "quantity": 4
  },
  "\u0427\u0435\u0441\u043d\u043e\u043a": {
    "measure": "\u0437\u0443\u0431\u0447",
    "quantity": 6
  }
}
'''

data = json.loads(json_data)

formatted_data = json.dumps(data, indent=2, ensure_ascii=False)
print(formatted_data)