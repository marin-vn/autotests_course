# Дан файл test_file/task_3.txt можно считать, что это запись покупок в магазине, где указана только цена товара
# В каждой строке файла записана цена товара.
# Покупки (т.е. несколько подряд идущих цен) разделены пустой строкой
# Нужно найти сумму трёх самых дорогих покупок, которые запишутся в переменную three_most_expensive_purchases

with open('C:/autotests_course/homework9/task_3.txt', 'r') as f:
    purchases = []
    purchase = []
    for line in f:
        if line.strip():
            purchase.append(float(line.strip()))
        else:
            purchases.append(purchase)
            purchase = []
    purchases.sort(key=lambda x: sum(x), reverse=True)
    three_most_expensive_purchases = sum(purchases[0] + purchases[1] + purchases[2])
    print(three_most_expensive_purchases)

assert three_most_expensive_purchases == 202346
