Предварительные шаги
1. docker run --name some-postgres -p 5432:5432 -e POSTGRES_PASSWORD=postgres -d postgres
2. Установить зависимости reqirements.txt
3. инициализировать БД % python init_db.py

Запуск приложения 
cd shop_app 
% python main.py

Использование
http://127.0.0.1:8080/items - получить все тов позиции
http://127.0.0.1:8080/stores - получить все торговые точки
http://127.0.0.1:8080/top_stores - топ 10 торговых точек
http://127.0.0.1:8080/top_sold - топ 10 продаваемых

python homework/client.py - внести запись о продаже
