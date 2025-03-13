#Valid Parentheses

def is_valid(s:str)->bool:
    if len(s)%2!=0:
        return False
    
    parentheses_dict:dict={
        "{":"}",
        "[":"]",
        "(":")"
    }
    
    stack:list=[]
 
    for char in s:
        if char in "{([":
            stack.append(char)
        else:
            if stack and char==parentheses_dict[stack[-1]]:
                stack.pop()
            else:
                return False      
    return len(stack)==0       
            
if __name__=="__main__":
    s = "[(])"
    print(is_valid(s))