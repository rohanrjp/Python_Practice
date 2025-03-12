numbers = [10,20,30,40]
target = 70

from typing import List

def find_1index(numbers:List[int],target:int)->List[int]:
    left,right=0,len(numbers)-1
    while left<right:
        current_sum=numbers[left]+numbers[right]
        if current_sum>target:
            right-=1
        elif current_sum<target:
            left+=1    
        else:
            return([left+1,right+1]) 
        
    return []   
                 
                
           
        
    



if __name__=="__main__":
    print(find_1index(numbers,target))
    
    
    
    
    