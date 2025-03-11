from typing import List

nums:List[int] = [12,2,20,4,10,3,4,5,11,13,14]
start_nums:set[int]=set(nums)
seq:List[int]=[]
max_len:int=0


for num in start_nums:
    if num-1 not in start_nums:
        result:List[int]=[num]
        length=1
        while num+1 in nums:
            length+=1
            num+=1
            result.append(num)
        if length>max_len:
            seq=result[:]    
        max_len=max(max_len,length)

        
print(f"Longest subsequence is {seq} with length {max_len}")           
            


        
        

