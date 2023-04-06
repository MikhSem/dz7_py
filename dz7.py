def check_rhythm(poem):
    """
    Функция принимает стихотворение и проверяет, есть ли в нем ритм.
    Ритм считается существующим, если число гласных букв в каждой фразе одинаковое.
    Если все фразы имеют одинаковое число гласных букв, функция возвращает "Парам пам-пам".
    В противном случае функция возвращает "Пам парам".
    """
    vowels = "аеёиоуыэюяАЕЁИОУЫЭЮЯ"
    phrase_vowel_counts = []
    for phrase in poem.split():
        vowel_count = sum(1 for letter in phrase if letter in vowels)
        phrase_vowel_counts.append(vowel_count)
    return "Парам пам-пам" if len(set(phrase_vowel_counts)) == 1 else "Пам парам"

poem = input("Введите стихотворение: ")
result = check_rhythm(poem)
print(result)

def print_operation_table(operation, num_rows=6, num_columns=6):
    # Выводим содержимое таблицы
    for i in range(1, num_rows+1):
        row = ""
        for j in range(1, num_columns+1):
            value = operation(i, j)
            row += str(value) + " "
        print(row.strip())

# Пример использования функции
print_operation_table(lambda x, y: x * y)

