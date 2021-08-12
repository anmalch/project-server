from django.shortcuts import render


# контролеры=функции (подключаем их в urls.py в path())
def index(request):
    return render(request, 'products/index.html')


def products(request):
    return render(request, 'products/products.html')
