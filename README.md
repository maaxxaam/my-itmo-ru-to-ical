# ITMO schedule to iCalendar converter

CLI приложение, которое сходит на my.itmo.ru за расписанием и экспортирует его как iCalendar. Позволяет автоматически и с автообновлением экспортировать пары в календари Google, iCloud и другие.

## Пререквизиты

Понадобится:

- `python` версии 3.7+
- Модули `dateutil`, `requests`, `ics` можно загрузить через pip:
    ```bash
    python3 -m pip install -r requirements.txt
    # или
    python3 -m pip install dateutil requests ics
    ``` 

## Как запустить
1. 	Склонировать репозиторий:
	```bash
	git clone https://github.com/maaxxaam/my-itmo-ru-to-ical.git && cd my-itmo-ru-to-ical
	```
1. Запустить CLI через python:
    ```bash
    python3 app.py <ISU Login> <ISU Password>
    ```
1. Импортировать файл my.itmo.ics в свой календарь
1. ???
1. PROFIT!!!

