class Solution:
    def isPalindrome(self, s: str) -> bool:
        rebuild_string = "".join([item.lower() for item in s if item.isalnum()])
        
        
        n = len(rebuild_string)
        i = 0
        j = n - 1
        while i < j:
            if rebuild_string[i] != rebuild_string[j]:
                return False
            i+=1
            j-=1
        
        return True
        
