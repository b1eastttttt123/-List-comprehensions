def textAnalyzer(text):

    vowels = ["а", "о", "у", "ы", "э", "е", "ё", "и", "ю", "я"]

    count = sum(1 for letter in text if letter in vowels)
    vowels_text_user = [letter for letter in text if letter in vowels]

    print(f"Список гласных букв: {vowels_text_user}")
    print(f"Длина списка: {count}")

text_user = input("Введите текст: ").lower()
textAnalyzer(text_user)
