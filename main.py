import string # для роботи зі знаками пунктуації

while True:
    target_word = input("Введіть слово для пошуку або 'q' для виходу: ")
    if target_word.lower() == 'q':
        break

    try:
        with open("text.txt", 'r', encoding='utf-8') as file:
            paragraphs = file.read().split('\n\n')
            word_found = False
            for i, paragraph in enumerate(paragraphs, 1):
                words = [word.strip(string.punctuation).lower() for word in paragraph.split()] # прибираємо знаки пунктуації через strip() і переводимо в нижній регістр через lower()
                if target_word.lower() in words:
                    print(f"Абзац {i}:\n{paragraph}\n")
                    word_found = True
            if not word_found:
                print(f"Слово '{target_word}' не знайдено в жодному абзаці.")
    except FileNotFoundError:
        print("Файл 'text.txt' не знайдено.")
    except Exception as e:
        print(f"Виникла помилка: {e}")
