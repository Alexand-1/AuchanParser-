import json

import requests


def get_all_products():
    url = 'https://www.auchan.ru/v1/catalog/products'

    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json;charset=UTF-8',
        'Origin': 'https://www.auchan.ru',
        'Referer': 'https://www.auchan.ru/catalog/konditerskie-izdeliya/pechene-vafli-pryaniki/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'добавь сюда свой user-agent',
        'sec-ch-ua': '"Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    data = {
        'filter': {
            'category': 'pechene_vafli_pryaniki',
            'promo_only': False,
            'active_only': False,
            'cashback_only': False
        },
        'page': 1,
        'perPage': 100, #количество товара которое нужно вывести
        'merchantId': 1,
    }

    all_products = []

    while True:
        response = requests.post(url, headers=headers, json=data)

        if response.status_code == 200:
            products = response.json().get('items', [])

            if not products:
                break

            all_products.extend(products)
            data['page'] += 1
        else:
            print(f"Failed to retrieve data. Status code: {response.status_code}")
            print(response.text)

            break

    return all_products

def process_products_list(all_products):
    processed_products = []

    for product in all_products:

        product_id = product.get("id")
        product_name = product.get("title")
        product_code = product.get("code")
        product_price = product.get("price", {}).get("value")
        product_currency = product.get("price", {}).get("currency")


        old_price_data = product.get("oldPrice", {})
        product_old_price = old_price_data.get("value") if old_price_data else None

        product_brand_name = product.get("brand", {}).get("name")


        product_link = f"https://www.auchan.ru/product/{product_code}/"

        processed_product = {
            'id': product_id,
            'name': product_name,
            'link': product_link,
            'oldPrice': product_old_price,
            'price': {
                'value': product_price,
                'currency': product_currency
            },
            'brand': {
                'name': product_brand_name,
            }
        }
        processed_products.append(processed_product)

    return processed_products

if __name__ == '__main__':
    all_products = get_all_products()

    if all_products:
        processed_products = process_products_list(all_products)

        json_data = json.dumps(processed_products, ensure_ascii=False, indent=2)
        print(json_data)

        with open('processed_products.json', 'w', encoding='utf-8') as json_file:
            json.dump(processed_products, json_file, ensure_ascii=False, indent=2)






