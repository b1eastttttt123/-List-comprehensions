# Задание 5. Разворот
## Что нужно сделать
**На вход в программу подаётся строка, в которой буква h встречается как минимум два раза. Реализуйте код, который разворачивает последовательность символов, заключённую между первым и последним появлением буквы h, в противоположном порядке.**

## Пример 1:
```
Введите строку: hqwehrty

Развёрнутая последовательность между первым и последним h: ewq.
```
## Пример 2:
```
Введите строку: hh

Развёрнутая последовательность между первым и последним h: 
```
## Пример 3:
```
Введите строку: hhqwerh

Развёрнутая последовательность между первым и последним h: rewqh.
```

## Советы и рекомендации
- Индекс нужного элемента можно искать как вручную, так и при помощи готовых методов списка.
- У метода index есть «брат» — метод rindex. В отличие от первого второй метод начинает поиск с правой стороны (с конца). Подробнее о нём вы можете узнать в этой статье.
  
***Что оценивается:***
> Результат вычислений корректен.
> 
> Input содержит корректные приглашения для ввода.
> 
> Формат вывода соответствует примеру.
> 
> Переменные и функции имеют значимые имена, не только a, b, c, d. 
