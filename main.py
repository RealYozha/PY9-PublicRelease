alphabet_ru = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
alphabet_en = "abcdefghijklmnopqrstuvwxyz"

lang = input("Введите язык (ru/en): ")
message = input("Введите текст: ").lower()
step = int(input("Введите длинну шага: "))
result_array = []
result_m_array = []

if lang == "ru":
    encryption_indexes = list([alphabet_ru.find(i)+step for i in message])
    result_array = [alphabet_ru[encryption_indexes[i]] for i in range(len(encryption_indexes))]
elif lang == "en":
    encryption_indexes = list([alphabet_en.find(i)+step for i in message])
    result_array = [alphabet_en[encryption_indexes[i]] for i in range(len(encryption_indexes))]
result = "".join(result_array)
print(result)

if lang == "ru":
    decryption_indexes = list([alphabet_ru.find(i)-step for i in result])
    result_m_array = [alphabet_ru[decryption_indexes[i]] for i in range(len(decryption_indexes))]
elif lang == "en":
    decryption_indexes = list([alphabet_en.find(i)-step for i in result])
    result_m_array = [alphabet_en[decryption_indexes[i]] for i in range(len(decryption_indexes))]
result_message = "".join(result_m_array)
print(result_message)
