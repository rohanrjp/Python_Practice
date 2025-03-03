from collections import Counter

nums = [10,7,7,8,8,8]
k = 2

counter=dict(Counter(nums))

sorted_counter=sorted(counter.items(),reverse=True,key= lambda dict_item:dict_item[1])

print([item[0] for item in sorted_counter[:k]])

