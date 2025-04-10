class Solution:
    def isValid(self, words: str) -> bool:
        # Check for minimum length and alphanumeric characters early
        if len(words) < 3 or not words.isalnum():
            return False

        vowels = {'a', 'e', 'i', 'o', 'u'}
        has_vowel = False
        has_consonant = False

        for char in words:
            # Check if character is a vowel
            if char.lower() in vowels:
                has_vowel = True
            # Check if character is a consonant
            elif char.isalpha():
                has_consonant = True

            if has_vowel and has_consonant:
                return True

        return False