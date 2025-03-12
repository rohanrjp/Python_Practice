#3sum

def find_3sum(nums:list[int])-> list:
    result=[]
    nums.sort()
    for idx in range(len(nums) - 2):
        if idx>0 and nums[idx]==nums[idx-1]:
            continue
        left,right=idx+1,len(nums)-1
        while left<right:
            current_sum=nums[left]+nums[right]+nums[idx]
            if current_sum>0:
                right-=1
            elif current_sum<0:
                left+=1
            else:
                result.append([nums[idx],nums[left],nums[right]])    
                left+=1
                right-=1
                
                while left<right and nums[left]==nums[left-1]:
                    left+=1
                while left<right and nums[right]==nums[right+1]:
                    right-=1    
    return result                
        
if __name__ == "__main__":
    nums:list = [-1,0,1,2,-1,-4]
    print(find_3sum(nums))