from django.shortcuts import render

# Create your views here.
def main_page(request):
    title = 'Главная страница'
    context = {
        'title': title,
    }
    return render(request, 'fourth_task/main_page.html', context)

def catalog_page(request):
    title = 'Каталог товаров'
    context = {
        'title': title,
        'games': ['Atomic Heart', 'Cyberpunk 2077', 'PayDay 2']
    }
    return render(request, 'fourth_task/catalog.html', context)

def basket_page(request):
    title = 'Корзина'
    context = {
        'title': title,
    }
    return render(request, 'fourth_task/basket.html', context)

def menu(request):
    return render(request, 'fourth_task/menu.html')