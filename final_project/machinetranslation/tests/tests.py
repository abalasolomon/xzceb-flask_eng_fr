import unittest
from translator import english_to_french, french_to_english

class TranslationTests(unittest.TestCase):

    def test_english_to_french(self):
        english_text = "Man"
        expected_french_text = "Homme"
        translated_text = english_to_french(english_text)
        self.assertEqual(translated_text, expected_french_text)

    def test_french_to_english(self):
        french_text = "Homme"
        expected_english_text = "Men"
        translated_text = french_to_english(french_text)
        self.assertEqual(translated_text, expected_english_text)

    

if __name__ == '__main__':
    unittest.main()
