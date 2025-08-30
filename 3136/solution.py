class Solution(object):
    def isValid(self, word):
        """
        :type word: str
        :rtype: bool
        """

        vowels = 'aeiou'
        vowels += vowels.upper()
        consonants = 'qwrtyplkjhgfdszxcvbnm'
        consonants += consonants.upper()
        allowed = vowels + consonants + '0123456789'

        if len(word) < 3:
            return False
        
        has_vowel = False
        has_consonants  = False

        for c in word:
            if c in vowels:
                has_vowel = True
            if c in consonants:
                has_consonants = True
            if c not in allowed:
                return False

        return has_vowel and has_consonants

#time complexity : O(n)
#space complexity : O(1)