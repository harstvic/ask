Техническое задание

Проект представляет собой сервис ответов на вопросы.
Пользователь сервиса имеет возможность зарегистрироваться, задать вопрос, 
ответить на вопросы других пользователей. Так же пользователь может отметить 
вопросы с помощь кнопки "лайк", изменяя их рейтинг. В качестве прототипа образца
можно использовать http://stackoverflow.com/

Основные сущности проекта

    Пользователь - email, имя, пароль, аватарка
    Вопрос - заголовок, текст, автор, рейтинг вопроса
    Ответ - текст, вопрос, автор, флаг "правильности"
    Лайк - вопрос, пользователь

Формы и страницы проекта

Главная страница

URL:  /

Назначение: представляет из себя список "популярных" вопросов. В списке 
выводятся вопросы за последнюю неделю в порядке убывания рейтинга.

Список новых вопросов

URL: /new/

Назначение: список вопросов по дате их добавления начиная с самого свежего.

Страница одного вопроса

URL: /question/123/

Назначение: на этой странице можно прочитать текст вопрос и список ответов к 
нему. Авторизованные пользователи могут добавить свой ответ.

Страница регистрации

URL: /signup/

Назначение: пользователь может ввести свой email, пароль, имя, выбрать аватарку 
и зарегистрироваться в проекте

Страница авторизации

URL: /login/

Назначение: пользователь может ввести email и пароль и авторизоваться (войти) в 
проекте.

Страница добавления вопроса

URL: /ask/

Назначение: авторизованный пользователь может задать вопрос, после чего перейдет
на страницу этого вопроса.
Примерный дизайн
https://lh3.googleusercontent.com/wU0kbS1H3KCYdMLmu2Bdzj-AU6sU4WnXFoco_A6WkEqPDKEVrl_4-oP6lu42amEHYnoMCxqf3TsUTnat4zH26vd7KCEf0T0HUbLf5Z24yxLcGqDApIUd9-u243d_n-qMyw=s1600
https://lh5.googleusercontent.com/pcnQwpaJAkN8j3ExRYmXFJ1ys6APbysuIukYSX_kW0XH3hb1q3LfIPj2OX-az7ezI5LUDRLD0WefyTaRAg_N51oU0oQiuYZC1s5iUEf-yyN3ndFyhOprQ3uhO9k8voBx=s1600
https://lh5.googleusercontent.com/Uy3iPZqCEiHa4aPpYWyYvm_j-Lnxfo_wIcwRkwLqn1HkKHWHWes3YP-OEGp434CTnzOTUwrDopWBZpjhVFKfRjhE3XEeoy77LuaK1Z8ftIwifIMt0MjoJkOlBLHr5-qU=s1600
https://lh6.googleusercontent.com/cy-2YNTpUUD7cPQZOQfP8MFSPsUzhWa8SJfSv9ly1tcIakC-IIlZ-PX_ShWJifu2bmLwis8WLx9J65Grazz3AEZciMaLDOp916uLNjdmmv8aiUGjsQPlpgAkSeJ9SqGh=s1600

AJAX запросы

URL: /like/123/

Назначение: пользователь может нажать кнопку "Лайк" у вопроса и это увеличит 
рейтинг вопроса. 
Пользователь может ставить "лайк" не более  1 раза для 1 вопроса.

Clone

git clone https://github.com/harstvic/ask.git ask

