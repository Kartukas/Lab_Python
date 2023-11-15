# TODO  Напишите функцию count_letters
def count_letters(text):
    new_text = "".join(c for c in text if c.isalpha())
    new_text = new_text.lower()
    dict_count_letters = {}
    default_count = 0
    for count in new_text:
        if new_text.isalpha():
            dict_count_letters[count] = dict_count_letters.get(count, default_count) + 1
    return dict_count_letters

# TODO Напишите функцию calculate_frequency
def calculate_frequency(d):
    total_count = sum(d.values())
    for s in d:
        d[s] = d[s] / total_count
        d[s] = f"{d[s]:.2f}"
    return d
main_str = """
У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо — песнь заводит,
Налево — сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кащей над златом чахнет;
Там русский дух… там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.
"""

# TODO Распечатайте в столбик букву и её частоту в тексте
d = calculate_frequency(count_letters(main_str))
for key in d:
    print(f"{key}: {d[key]}")

