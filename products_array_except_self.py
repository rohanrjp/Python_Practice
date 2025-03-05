nums = [1,2,4,6]
output=[1]*len(nums)
result=1
reverse_result=1

for i in range(0,len(nums)):
    output[i]=result
    result*=nums[i]
    
for i in range(len(nums)-1,-1,-1):
    output[i]*=reverse_result
    reverse_result*=nums[i]
       
print(output)    
    
        
    
    