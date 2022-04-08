def is_palindrome(word):
    return word == word[::-1]
print(is_palindrome('hannah'))

from unittest import TestCase, main

class TestIsPalindrome(TestCase):
    def test_if_word_is_palindrome_true(self):
        result = is_palindrome('otto')
        self.assertTrue(result)

    def test_if_word_is_palindrome_false(self):
        result = is_palindrome('margot')
        self.assertFalse(result)
