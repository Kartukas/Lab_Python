# TODO Напишите функцию find_common_participants
def find_common_participants(first_line,second_line,delimiter = ","):
    first = first_line.split(delimiter)
    second = second_line.split(delimiter)
    general = list(set(first).intersection(second))
    general.sort()
    return general

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой

participants = find_common_participants(participants_first_group,participants_second_group,"|")
print("Общие участники:", participants)
