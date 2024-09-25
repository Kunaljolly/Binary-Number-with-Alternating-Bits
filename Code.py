class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        n = list(bin(n)[2:])
        for x in range(len(n)-1):
            if n[x] == n[x+1]:
                return False
        return True
