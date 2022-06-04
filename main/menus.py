from django.conf import settings


def get_simple_menus(request):
    if settings.LANGUAGE_CODE.lower().startswith("ru"):
        return get_simple_menus_ru(request)


def get_simple_menus_ru(request):
    return [
        {
            "title": "Навигация",
            "icon": "fa fa-route",
            "children": [
                {
                    "title": "Модерация - главная",
                    "icon": "fa fa-house-user",
                    "url": "/admin/",
                },
                {
                    "title": "Сайт - главная",
                    "icon": "fa fa-home",
                    "url": "/",
                },
            ],
        },

        {
            "title": "Контент",
            "icon": "fa fa-shopping-basket",
            "children": [
                {
                    "title": "Категории товаров",
                    "icon": "fa fa-folder",
                    "model": "main.category"
                },
                {
                    "title": "Товары",
                    "icon": "fa fa-prescription-bottle-alt",
                    "model": "main.product"
                },
            ],
        },

        {
            "title": "Авторизация",
            "icon": "fa fa-users-cog",
            "children": [
                {
                    "title": "Пользователи",
                    "icon": "fas fa-user",
                    "model": "auth.user",
                    "permissions": ["auth.view_user", ],
                },
                {
                    "title": "Группы",
                    "icon": "fas fa-users",
                    "model": "auth.group",
                    "permissions": ["auth.view_group", ],
                }
            ],
        },
    ]
