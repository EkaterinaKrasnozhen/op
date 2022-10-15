# Джек
data = open("jack.txt", "r")
k = data.read()\
                .replace(',','').split()

data.close()

dict_cmp = {i: k.count(i) for i in k}
print(dict_cmp)

# не поняла слова с разными окончаниями считать как разные? если нет - как их посчитать как одно и тоже слово?