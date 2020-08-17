Тестовое задание
===

Зависимости
---

1. Python 3.7 и выше
2. Docker 19.03 и выше
3. Docker Compose 1.25 и выше

Развертывание проекта
---

* Клонируем этот репозиторий к себе
* Создаем виртуальное окружение и устанавливаем туда зависимости
    
    
    python -m venv venv
    source venv/bin/activate
    pip install "sources/.[dev]"


* Создаем .env файл и меняем нужные настройки


    cp .env.example .env
    
* Собираем приложение


    inv build
    docker-compose build
    
* Запускаем приложение


    docker-compose up -d


Приложение доступно по адресу 127.0.0.1:8000.


API:
---

URL: /load_tariff/

Описание: загрузка тарифа в приложение из JSON-конфига

Пример:

    Request:
    POST http://127.0.0.1:8000/load_tariff/

    {
        "2000-07-07": [
            {
                "cargo_type": "Glass",
                "rate": 0.04
            },
            {
                "cargo_type": "Other",
                "rate": 0.01
            }
        ]
    }
    
    Response:
    {
        "loaded": true
    }


URL: /get_insurance_price/

Описание: получение цены страховки для определенного типа товара по дате и обьявленной стоимости

Пример:

    Request:
    POST http://127.0.0.1:8000/get_insurance_price/

    {
    
        "cargo_type": "Glass",
        "date": "2001-01-01",
        "declared_value": 100
    }

    
    Response:
    {
        "price": 4.0
    }

