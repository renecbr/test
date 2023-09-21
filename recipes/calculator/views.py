from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}


# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
def dish_view(request, dish):
    if dish in DATA.keys():
        servings = request.GET.get("servings")
        if servings:
            servings = int(servings)
            dish_serv = DATA[dish].copy()
            for key in dish_serv:
                dish_serv[key] = servings * dish_serv[key]
            context = {
                'recipe': dish_serv
            }
        else:
            context = {
                'recipe': DATA[dish]
            }
    else:
        context = {
            'recipe': {
            }
        }
    return render(request, 'calculator/index.html', context)










