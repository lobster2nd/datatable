# Обработчик баз данных больших объёмов  

Веб-страница с отображением в табличном виде (datatable) данных из БД (100 тыс записей). Ключевая особенность - время загрузки таблицы менее 1 секунды.  

Особенности:  
1 Сортировка по всем столбцам  
2 Поиск по всем столбцам (поле поиска над столбцом)  
3 Фильтр по всем столбцам (с учетом типа данных, в т.ч по таблице модальностей)  
4 Пагинация  

## Стек технологий  

![Static Badge](https://img.shields.io/badge/python-white?style=for-the-badge&logo=python&logoColor=%233776AB&labelColor=%23ebe3ce&color=%233776AB)
  ![Static Badge](https://img.shields.io/badge/Django-white?style=for-the-badge&logo=Django&logoColor=%23092E20&labelColor=%23ebe3ce&color=%23092E20) ![Static Badge](https://img.shields.io/badge/html5-white?style=for-the-badge&logo=html5&logoColor=%23E34F26&labelColor=%23ebe3ce&color=%23E34F26) ![Static Badge](https://img.shields.io/badge/css3-white?style=for-the-badge&logo=css3&logoColor=%231572B6&labelColor=%23ebe3ce&color=%231572B6) ![Static Badge](https://img.shields.io/badge/jquery-white?style=for-the-badge&logo=jquery&logoColor=%230769AD&labelColor=%23ebe3ce&color=%230769AD)



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
