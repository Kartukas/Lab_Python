# TODO импортировать необходимые молули
import csv
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"

  # TODO считать содержимое csv файла
  # TODO Сериализовать в файл с отступами равными 4

def task(filename) -> None:
    with open(INPUT_FILENAME, 'r') as input_file:
        reader = csv.DictReader(input_file, delimiter=',')
        json_data = []
        for row in reader:
            json_object = {}
            for key, value in row.items():
                json_object[key] = value
            json_data.append(json_object)
        print(json.dumps(json_data, indent=4))



if __name__ == '__main__':
    # Нужно для проверки
    task("input.csv")

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
