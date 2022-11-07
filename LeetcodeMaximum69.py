class Solution:
    def maximum69Number (self, num: int) -> int:
        s = [int(x) for x in str(num)]
        for i in range(0,len(s)):
            if(s[i] == 6):
                s[i] = 9
                break
        inte = [str(integer) for integer in s]
        a_string = "".join(inte)
        res = int(a_string)
        return res
        