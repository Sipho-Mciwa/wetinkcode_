import unittest
import word_processor

class MyTestCases(unittest.TestCase):

    def test_convert_to_word_list1(self):
        text = "These are indeed interesting, an obvious understatement, times. What say you?"
        expected_list = ['these','are','indeed','interesting','an','obvious','understatement','times','what','say','you']
        self.assertEqual(word_processor.convert_to_word_list(text), expected_list)

    def test_convert_to_word_list2(self):
        text = '"!!!" Instead of "Amazing!"'
        expected_list = ['instead', 'of', 'amazing']
        self.assertEqual(word_processor.convert_to_word_list(text), expected_list)

    def test_convert_to_word_list3(self):
        text = "This # is _ my * last > test > / ?"
        expected_list = ["this", "is", "my", "last", "test"]
        self.assertEqual(word_processor.convert_to_word_list(text), expected_list)

    def test_filter_words_less_than_5(self):
        text = "These are indeed interesting, an obvious understatement, times. What say you?"
        self.assertEqual(word_processor.words_longer_than(5, text), ['indeed', 'interesting', 'obvious', 'understatement'])

    def test_filter_words_less_than_10(self):
        text = "These are indeed interesting, an obvious understatement, times. What say you?"
        self.assertEqual(word_processor.words_longer_than(10, text), ['interesting', 'understatement'])

    def test_filter_words_less_than_15(self):
        text = "These are indeed interesting, an obvious understatement, times. What say you?"
        self.assertEqual(word_processor.words_longer_than(15, text), [])

    def test_words_length_map(self):
        text = "These are indeed interesting, an obvious understatement, times. What say you?"
        self.assertEqual(word_processor.words_lengths_map(text), {2: 1, 3: 3, 4: 1, 5: 2, 6: 1, 7: 1, 11: 1, 14: 1})

    def test_letters_count(self):
        text = "These are indeed interesting, an obvious understatement, times. What say you?"
        self.assertEqual(word_processor.letters_count_map(text), {'a':5, 'b': 1, 'c': 0, 'd': 3, 'e': 11, 'f': 0, 'g': 1, 'h': 2, 'i': 5, 'j': 0, 'k': 0, 'l': 0, 'm': 2, 'n': 6, 'o': 3, 'p': 0, 'q': 0, 'r': 3, 's': 6, 't': 8, 'u': 3, 'v': 1, 'w': 1, 'x': 0, 'y': 2, 'z': 0})

    def test_most_used_letter_empty_text(self):
        self.assertIsNone(word_processor.most_used_character(''))

    def test_most_used_letter_in_text(self):
        text = "These are indeed interesting, an obvious understatement, times. What say you?"
        self.assertEqual(word_processor.most_used_character(text), 'e')

        
if __name__ == "__main__":
    unittest.main()