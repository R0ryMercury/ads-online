# Сайт объявлений

## Установка зависимостей и запуск проекта

Установка зависимостей через pip:

    python -m venv venv
    . env/bin/activate
    pip install -r requirements.txt

Установка зависимостей через poetry:

    poetry shell
    poetry install

Запуск проекта

    docker-compose -f market_postgres/docker-compose.yaml up -d
    skymarket/manage.py migrate
    skymarket/manage.py runserver

Проект будет доступен в браузере по адресу: http://0.0.0.0:3000/

## Описание проекта

### Главная страница

Авторизация

![login](https://github.com/gmoroz/ads-online/blob/master/readme_files/login.png)

Регистрация

![registration](https://github.com/gmoroz/ads-online/blob/master/readme_files/registration.png)
