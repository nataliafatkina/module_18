from django.shortcuts import render

# Create your views here.
def main_page(request):
    title = 'Главная страница'
    context = {
        'title': title,
    }
    return render(request, 'third_task/main_page.html', context)

def catalog_page(request):
    title = 'Каталог товаров'
    games = ['Atomic Heart', 'Cyberpunk 2077', 'PayDay 2']
    context = {
        'title': title,
    }
    for i, game in enumerate(games):
        context[f'game_{i + 1}'] = game
    return render(request, 'third_task/catalog.html', context)

def basket_page(request):
    title = 'Корзина'
    context = {
        'title': title,
    }
    return render(request, 'third_task/basket.html', context)
