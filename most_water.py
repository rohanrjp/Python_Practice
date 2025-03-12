from typing import List

height:List = [1,7,2,5,4,7,3,6]

def get_volume(height:List)->int:
    left,right=0,len(height)-1
    volume=0
    max_volume=0
    
    while left<right:
        
        min_height=min(height[left],height[right])
        base=right-left
        volume=min_height*base
        max_volume=max(volume,max_volume)
        if height[left]<height[right]:
            left+=1
        else:
            right-=1      
                              
    return max_volume

if __name__=="__main__":
    print(get_volume(height))