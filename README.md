# Обработчик баз данных больших объёмов  

Веб-страница с отображением в табличном виде (datatable) данных из БД (100 тыс записей). Ключевая особенность - время загрузки таблицы менее 1 секунды.  

Особенности:  
1 Сортировка по всем столбцам  
2 Поиск по всем столбцам (поле поиска над столбцом)  
3 Фильтр по всем столбцам (с учетом типа данных, в т.ч по таблице модальностей)  
4 Пагинация  

## Стек технологий  

<img src="https://img.shields.io/badge/Python - black?style=for-the-badge&logo=Python&logoColor=blue"/> <img src="https://img.shields.io/badge/Django - black?style=for-the-badge&logo=Django&logoColor=white"/> <img src="https://img.shields.io/badge/jQuery - black?style=for-the-badge"/> <img src="https://img.shields.io/badge/HTML - black?style=for-the-badge&logo=sqlite&logoColor=blue"/>

## Установка проекта локально (Linux)  
+ Склонировать репозиторий и перейти в него в командной строке:  
```
git clone https://github.com/lobster2nd/datatable.git  
cd datatable/test_site
```  
+ Cоздать и активировать виртуальное окружение:   
```
python -m venv env
```  
```
source env/bin/activate
```  
+ Перейти в директорию и установить зависимости из файла requirements.txt:  
```
pip install -r requirements.txt
```
+ Применить миграции:
```
python3 manage.py migrate
```
+ Запустить сервер:  
```
python3 manage.py runserver
```
Сайт будет доступен на локальном хосте, порт 8000  
Заполнить базу данных http://127.0.0.1:8000/init_db/  
Работа с таблицей http://127.0.0.1:8000/view_studies/  
