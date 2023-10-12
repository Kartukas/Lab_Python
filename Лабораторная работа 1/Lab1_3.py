list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]
# TODO Разделите участников на две команды
Count_players = len(list_players)
Group_players = Count_players // 2
Group_1 = list_players[:Group_players]
Group_2 = list_players[Group_players:]
print(Group_1)
print(Group_2)
