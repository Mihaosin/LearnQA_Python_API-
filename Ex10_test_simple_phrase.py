class Test_Simple_Phrase:
    def test_simple_phrase(self):
        phrase = input("Введите фразу короче 15 символов: ")
        phrase_len = len(phrase)
        assert phrase_len != 0, "Вы ничего не ввели!"
        assert phrase_len < 15, f"Вы ввели слишком длинную фразу. {phrase_len} - количество символов"

        print("Вы ввели фразу правильной длины!")