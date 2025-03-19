#Find Minimum in Rotated Sorted Array
def binary_search(nums)->int:
    left,right=0,len(nums)-1
    if nums[left]<nums[right]:
        return nums[left]
    while left<right:
        mid=left + (right-left)//2
        if nums[mid]>nums[right]:
            left=mid+1
        else:
            right=mid
    return nums[left]            
            
if __name__=="__main__":
    nums = [3,4,5,6,7,1,2]
    print(binary_search(nums))