
strs = ["act","pots","tops","cat","stop","hat"]

from collections import defaultdict

strs_dict=defaultdict(list)

for string in strs:
    strs_dict["".join(sorted(string))].append(string)
        
print(list(strs_dict.values()))   
