# Homework 1

## Общее описание

Вам предстоит написать консольный вариант игры. Вы можете выбрать одну из двух задач. За выполнение стандартной задачи вы можете получить максимум 8 баллов, а за задачу повышенной сложности — 10.

Механику взаимодействия с игрой вы можете придумать сами, однако после каждого хода на экране должно присутствовать актуальное изображение игрового поля.

Вы можете посмотреть на игру "[slapjack](https://github.com/katiejiang/slapjack)", чтобы понять технические особенности работы с консолью применительно к играм. Данная реализация является примером кода неплохого качества, однако не стоит ориентироваться на нее как на идеальный вариант. Мы призываем вас использовать хорошие практики разработки. Помните, ваш код будут читать люди — постарайтесь написать максимально читаемый и логичный код.

## Общие требования

Параметры игры должны приниматься с помощью аргументов командной строки. Для этого рекомендуем воспользоваться библиотекой [argparse](https://habr.com/ru/post/144416/)

Обязательно должно быть описание проекта (readme) — как минимум, с описанием запуска игры. Скрины приветствуются.

Должна быть реализована возможность сохранить игру, чтобы после перезапуска скрипта продолжить с того же места. Для реализации может быть удобно воспользоваться модулем [pickle](https://docs.python.org/3/library/pickle.html).

Игра должна играть против вас, алгоритм выбора хода не важен, даже если противник делает случайные ходы (но допустимые с точки зрения правил).

## Стандартная задача

Ваша задача — реализовать консольный вариант игры "[Крестики-нолики](https://ru.wikipedia.org/wiki/Крестики-нолики)".
В игре должна присутствовать возможность выбирать произвольный размер поля N K, где N — длина поля, K — ширина поля.

Условие победы — min (N,K) последовательных крестиков / ноликов по горизонтали, по вертикали или по диагонали.

На вход программа должна принимать параметры N и K.


## Задача повышенной сложности

Ваша задача — реализовать консольный вариант игры "[Морской бой](https://ru.wikipedia.org/wiki/Морской_бой_(игра))".
В игре должна присутствовать возможность выбирать произвольный размер поля N K, где N— длина поля, K— ширина поля.

Корабли для обоих сторон могут расставляться автоматически без участия игрока.

Количество и возможные размеры кораблей должны вычисляться автоматически, исходя из пропорций в оригинальной версии игры. Вы можете не рассматривать размер карты меньше, чем 55.

На вход программа должна принимать параметры N и K.

## Дополнительная информация

- При создании Merge Request в поле Description опишите какой проект выбрали и информацию по нему.
- Срок выполнения ДЗ 1 неделя (до 23:59 среды).
- За каждую просроченную неделю -1 балл
- Срок проверки - 3 дня.
- После ревью даётся 3 дня на исправление замечаний
- Будет всего один раунд ревью, то есть: сдача домашки - наши замечания - можно запушить исправления - новые замечания (если будут) - приём домашки и выставление оценки. После этого вы можете присылать доработки, но мы их смотреть и учитывать уже не будем.