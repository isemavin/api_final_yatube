## Yatube API
---
#### Описание:
Проект Yatube API представляет из себя социальную сеть в которой можно публиковать посты, оставлять комментарии к постам и подписываться на других пользователей.

---
#### Запуск проекта:
- Клонировать репозиторий и перейти в него в командной строке
- Cоздать и активировать виртуальное окружение:
`python3 -m venv env`
`source env/bin/activate`
- Установить зависимости из файла requirements.txt:
`python -m pip install --upgrade pip`
`pip install -r requirements.txt`
- Выполнить миграции:
`python3 manage.py migrate`
- Запустить проект:
`python3 manage.py runserver`
---
#### Примеры запросов к API:
- Получение публикаций:
`GET: /api/v1/posts/`
- Создание публикации:
`POST: /api/v1/posts/`
- Получение публикации:
`GET: /api/v1/posts/{id}/`
- Обновление публикации:
`PUT: /api/v1/posts/{id}/`
- Частичное обновление публикации:
`PATCH: /api/v1/posts/{id}/`
- Удаление публикации:
`DELETE: /api/v1/posts/{id}/`
- Получение комментариев:
`GET: /api/v1/posts/{post_id}/comments/`
- Добавление комментария:
`POST: /api/v1/posts/{post_id}/comments/`
- Получение комментария:
`GET: /api/v1/posts/{post_id}/comments/{id}/`
- Обновление комментария:
`PUT: /api/v1/posts/{post_id}/comments/{id}/`
- Частичное обновление комментария: 
`PATCH: /api/v1/posts/{post_id}/comments/{id}/`
- Удаление комментария:
`DELETE: /api/v1/posts/{post_id}/comments/{id}/`
- Список сообществ:
`GET: /api/v1/groups/`
- Информация о сообществе:
`GET: /api/v1/groups/{id}/`
- Подписки:
`GET: /api/v1/follow/`
- Подписка:
`POST: /api/v1/follow/`
- Получить JWT-токен:
`POST: /api/v1/jwt/create/`
- Обновить JWT-токен:
`POST: /api/v1/jwt/refresh/`
- Проверить JWT-токен:
`POST: /api/v1/jwt/verify/`

