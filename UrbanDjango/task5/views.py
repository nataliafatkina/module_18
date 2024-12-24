from django.shortcuts import render
from .forms import ContactForm

# Create your views here.
users = ['user1', 'user2', 'user3']

def sign_up_by_html(request):
    info = {}
    success = None

    if request.method == 'POST':
        name = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = request.POST.get('age')

        if name not in users and password == repeat_password and int(age) >= 18:
            success = f'Приветствуем, {name}!'

        if name in users:
            info['error'] = 'Пользователь уже существует'
        if password != repeat_password:
            info['error'] = 'Пароли не совпадают'
        if int(age) < 18:
            info['error'] = 'Вы должны быть старше 18'

    context = {
        'error': info,
        'success': success
    }

    return render(request, 'fifth_task/registration_page.html', context)


def sign_up_by_django(request):
    info = {}
    success = None
    form = ContactForm()

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']

            if name not in users and password == repeat_password and int(age) >= 18:
                success = f'Приветствуем, {name}!'

            elif name in users:
                info['error'] = 'Пользователь уже существует'
            elif password != repeat_password:
                info['error'] = 'Пароли не совпадают'
            elif int(age) < 18:
                info['error'] = 'Вы должны быть старше 18'

    context = {
        'form': form,
        'error': info,
        'success': success
    }

    return render(request, 'fifth_task/registration_page.html', context)


