from django.shortcuts import render


# контролеры=функции (подключаем их в urls.py в path())
def index(request):
    context = {
        'title': 'GeekShop - Catalogue',
    }
    return render(request, 'products/index.html', context)


def products(request):
    context = {
        'title': 'Products',
        'products': [
            {'name': 'Худи черного цвета с монограммами adidas Originals',
             'price': 6090,
             'description': 'Мягкая ткань для свитшотов. Стиль и комфорт – это образ жизни',
             'image': 'Adidas-hoodie.png'
             },
            {'name': 'Синяя куртка The North Face',
             'price': 23725,
             'description': 'Гладкая ткань. Водонепроницаемое покрытие. Легкий и теплый пуховый наполнитель.',
             'image': 'Blue-jacket-The-North-Face.png'
             },
            {'name': 'Коричневый спортивный oversized-топ ASOS DESIGN',
             'price': 3390,
             'description': 'Материал с плюшевой текстурой. Удобный и мягкий.',
             'image': 'Brown-sports-oversized-top-ASOS-DESIGN.png'
             },
            {'name': 'Черный рюкзак Nike Heritage',
             'price': 2340,
             'description': 'Плотная ткань. Легкий материал.',
             'image': 'Black-Nike-Heritage-backpack.png'
             },
            {'name': 'Черные туфли на платформе с 3 парами люверсов Dr Martens 1461 Bex',
             'price': 13590,
             'description': 'Гладкий кожаный верх. Натуральный материал.',
             'image': 'Black-Dr-Martens-shoes.png'
             },
            {'name': 'Темно-синие широкие строгие брюки ASOS DESIGN',
             'price': 2890,
             'description': 'Легкая эластичная ткань сирсакер Фактурная ткань.',
             'image': 'Dark-blue-wide-leg-ASOs-DESIGN-trousers.png'
             },
        ]
    }
    return render(request, 'products/products.html', context)
