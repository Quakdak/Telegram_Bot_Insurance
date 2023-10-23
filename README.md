# Telegram_Bot_Insurance
Creating a chatbot that will enable the client to quickly and easily inspect the insured property without having special expert skills.


Для установки нужно проделать следующие шаги:
1. Склонировать данный репозиторий в среду разработки для питона, удобнее всего Pycharm.
2. Скачать программу для работы с базаой данных PostgreSQL - pgAdmin4(https://www.pgadmin.org/download/) Windows или macOS
3. В данной программе выбрать пароль для всех соединений и создать базу данных с именем "gino"
4. В config/.env заменить значение PGPASSWORD на выбранное вами
5. Запустить main.py(в def main закомментируйте await db.gino.drop_all() и await db.gino.create(), если не хотите обнулять бд после остановки бота)

(При нажатии /start в боте ваш id занесётся в таблицу users, для получения прав администратора измените значение is_admin в таблице users на True, прилагается фото)
![image](https://github.com/Quakdak/Telegram_Bot_Insurance/assets/76743076/4511e0de-bb81-421b-988e-d4575d4c285b)

