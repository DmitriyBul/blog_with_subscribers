# nekidaem-blog

### Test assignment for nekidaem.ru
Задание:

Реализовать бэкенд с минимальным фронтендом (можно на голом HTML):

1.	Имеется база стандартных пользователей Django (добавляются через админку, регистрацию делать не надо).
2.	У каждого пользователя есть персональный блог. Новые создавать он не может.
3.	Пост в блоге — элементарная запись с заголовком, текстом и временем создания.
4.	Пользователь может подписываться (отписываться) на блоги других пользователей (любое количество).
5.	У пользователя есть персональная лента новостей, в которой в обратном хронологическом порядке выводятся посты из блогов, на которые он подписан.
6.	Пользователь может помечать посты в ленте прочитанными.
7.	При добавлении/удалении подписки содержание ленты меняется (при удалении подписки пометки о "прочитанности" сохранять не нужно).
8.	При добавлении поста в ленту — подписчики получают почтовое уведомление со ссылкой на новый пост.
9.	Изменение содержания лент подписчиков (и рассылка уведомлений) должно происходить как при стандартной публикации поста пользователем через интерфейс сайта, так при добавлении/удалении поста через админку.

Техника:
Python 3.x, Django > 3.х, Postgresql или SQLite. 
Проект должен быть на гитхабе и отражать процесс разработки.
Код максимально приближенный к боевому (насколько получится).
Реализовать на Class-based views.

Проект необходимо упаковать в докер. Запускать через docker-compose.

В проекте должно быть README с описанием запуска проекта.

Срок выполнения 1-2 дня.

Регистрация отсутствует, поэтому проверить работоспособность можно залогинившись в админку (логин - admin, пароль - admin).
