fruits = [
    {"name":"apple", "calories":"130"},
    {"name":"avocado", "calories":"50"},
    {"name":"banana", "calories":"110"},
    {"name":"cantaloupe", "calories":"50"},
    {"name":"grapefruit", "calories":"60"},
    {"name":"grapes", "calories":"90"},
    {"name":"honeydew melon", "calories":"50"},
    {"name":"kiwifruit", "calories":"90"},
    {"name":"lemon", "calories":"15"},
    {"name":"lime", "calories":"20"},
    {"name":"nectarine", "calories":"60"},
    {"name":"orange", "calories":"80"},
    {"name":"Peach", "calories":"60"},
    {"name":"pear", "calories":"100"},
    {"name":"pineapple", "calories":"50"},
    {"name":"plums", "calories":"70"},
    {"name":"strawberries", "calories":"50"},
    {"name":"sweet cherries", "calories":"100"},
    {"name":"tangerine", "calories":"50"},
    {"name":"watermelon", "calories":"80"}
]

answer = input("Item: ")

for fruit in fruits:
    fruitName = fruit["name"]
    fruitCalory = fruit["calories"]
    if answer.lower() == fruit["name"]:
        print(f"Calories: {fruitCalory}")
