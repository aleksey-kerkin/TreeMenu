# Django Tree Menu

Этот проект представляет собой Django-приложение, которое реализует древовидное меню с возможностью редактирования через админку Django.

## Установка и запуск

### 1. Клонирование репозитория

```bash
git clone https://github.com/aleksey.kerkin/TreeMenu.git
cd TreeMenu
```

### 2. Установка зависимостей

```bash
python -m venv .venv
source .venv/bin/activate  # Для Linux
source venv\Scripts\activate  # Для Windows
pip install -r requirements.txt
```

### 3. Применение миграций

```bash
python manage.py migrate
```

### 4. Создание суперпользователя

```bash
python manage.py createsuperuser
```

### 5. Запуск сервера

```bash
python manage.py runserver
```

### 6. Доступ к админке

Перейдите по адресу `http://127.0.0.1:8000/admin/`, чтобы создать и настроить ваши меню.

## Примеры использования

### 1. Создание меню в админке

1. Войдите в админку Django.
2. Создайте новое меню, указав `Menu Title`(в данном примере 'main_menu').
3. Добавьте пункты меню, указав `Item Title`, `Item URL` или `Named URL`(например, 'home' или 'about' в данном примере).

### 2. Использование меню в шаблоне

```html
<!-- Пример использования в шаблоне -->

{% load menu_tags %}

<html>
  <head>
    <title>Tree Menu Example</title>
  </head>
  <body>
    <h1>Main Menu</h1>
    {% draw_menu 'main_menu' %} # Пишем имя меню, которое создали в админке в разделе 'Menu Title'
  </body>
</html>
```
