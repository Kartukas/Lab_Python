users = ['user1', 'user2', 'user3', 'user1', 'user4', 'user2']

# TODO Добавьте словарь и замените в нем нулевые значения статисчикой посещений
Unic_users = {
    "Общее количество": 0,
    "Уникальные посещения": 0,
}
Unic_users["Общее количество"] = len(users)
Unic_users["Уникальные посещения"] = len(set(users))
print(Unic_users)
