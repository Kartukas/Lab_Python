# TODO решите задачу
import json
def task(file) -> float:
    sum_of_products = 0

    with open('input.json') as file:
        data = json.load(file)

    sum_of_products = sum([item["score"] * item["weight"] for item in data])

    return round(sum_of_products, 3)


print(task("input.json"))
