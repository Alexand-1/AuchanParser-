программа парсер для сайта Ашан которая выводит нужное количество товаров по нужному запросу в cURL
выводит товары для города:Москва


для того чтобы выводило товары для других городов, например Санк-Питербург добавьте в headers свои cookie значения и передайте нужный id региона


для того чтобы получать больше или меньше продуктов из парсера поменяйше значение в словаре data значение : perPage на нужное вам


выводит аткие значения как:
id товара из сайта/приложения,

наименование,
ссылка на товар,
регулярная цена,
промо цена,
бренд.

Необходимые зависимости:

Python 3.9+
json
request