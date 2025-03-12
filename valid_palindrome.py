"""
s:str = "Was it a car or a cat I saw?"

s=list(s.casefold())

s="".join(list(filter(lambda char:char.isalnum(),s)))

print(s==s[::-1])
"""

s:str = "Was it a car or a cat I saw?"

def is_palindrome(s:str):
    left,right=0,len(s)-1
    while left<right:
        while left<right and s[left].isalnum()!=True:
            left+=1
        while left<right and  s[right].isalnum()!=True:
            right-=1
        if s[left].casefold()!=s[right].casefold():
            return False 
        left+=1
        right-=1
    return True    
           
print(is_palindrome(s))            