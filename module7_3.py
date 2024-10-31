import string


class WordsFinder:
    def __init__(self, *file_names):
        # Сохраняем названия файлов в виде кортежа
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        # Перебираем названия файлов и открываем каждый из них
        for file_name in self.file_names:
            try:
                with open(file_name, 'r', encoding='utf-8') as file:
                    # Считываем текст файла
                    text = file.read()
                    # Приводим текст к нижнему регистру
                    text = text.lower()
                    # Удаляем пунктуацию
                    text = text.translate(str.maketrans('', '', string.punctuation.replace('-', '')))
                    # Разбиваем текст на слова
                    words = text.split()
                    # Записываем результат в словарь
                    all_words[file_name] = words
            except FileNotFoundError:
                print(f"Файл {file_name} не найден.")
            except Exception as e:
                print(f"Произошла ошибка при чтении {file_name}: {e}")

        return all_words

    def find(self, word):
        result = {}
        all_words = self.get_all_words()  # Получаем все слова из файлов
        word = word.lower()  # Приводим к нижнему регистру для точности поиска

        # Перебираем каждый файл и его слова
        for file_name, words in all_words.items():
            # Поиск первого вхождения слова
            if word in words:
                position = words.index(word) + 1  # Индекс + 1 для человеческого счёта
                result[file_name] = position

        return result

    def count(self, word):
        result = {}
        all_words = self.get_all_words()  # Получаем все слова из файлов
        word = word.lower()  # Приводим к нижнему регистру для точности подсчета

        # Перебираем каждый файл и его слова
        for file_name, words in all_words.items():
            # Подсчет вхождений слова
            count = words.count(word)
            if count > 0:
                result[file_name] = count

        return result


# Пример использования класса
finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())  # Выводит все слова
print(finder2.find('TEXT'))  # Выводит позицию первого слова по счёту
print(finder2.count('teXT'))  # Выводит количество вхождений слова в тексте
