class Solution:
    def reverseWords(self, s: str) -> str:
        strings = s.split() 
        strings = [st[::-1] for st in strings]
        strings = ' '.join(strings)
        return strings