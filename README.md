# where_to_go
 
Интерактивная карта Москвы, с известными местами для активного отдыха с подробными описаниями и комментариями. Ознакомиться с сайтом можно [по ссылке](https://yuraml.pythonanywhere.com/).

### Как установить

Python3 должен быть уже установлен. 
Затем используйте `pip` (или `pip3`, есть есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```

Для работы программы необходим файл `.env` с необходимыми данными, заполненный подобным образом:

```
SECRET_KEY=your_secret_key
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
ENGINE=django.db.backends.postgresql
NAME=your_database_name
USER=your_database_username
PASSWORD=your_database_password
HOST=localhost
PORT=5432
STATIC_URL=/static/
MEDIA_URL=/media/
MEDIA_ROOT=/path/to/media/directory
```

### Запуск

Для запуска введите в командную строку следующие команды по очереди:

```console
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py runserver
```

Затем откройте сайт по [адресу 127.0.0.1:8000](http://127.0.0.1:8000/)


### Админка

Для запуска админки создайте суперюзера, введя в командную строку:

```console
python3 manage.py createsuperuser
```

Затем откройте сайт по [адресу 127.0.0.1:8000/admin](http://127.0.0.1:8000/admin)


### Загрузка пользовательских данных

Вы можете пополнить интерактивную карту Москвы своими локациями. Для этого вам нужен JSON файл, заполненный следующим образом:

```
{
    "title": "Название места",
    "imgs": [
        "Список ссылок на ваши картинки, через запятую",
    ],
    "description_short": "Краткое описание места",
    "description_long": "Подробное описание места",
    "coordinates": {
        "lng": "Долгота",
        "lat": "Широта"
    }
}
```

Скопируйте ссылку на ваш JSON файл, а затем введите в консоли команду:

```console
python3 manage.py load_place {ссылка на JSON файл}
```


### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).
