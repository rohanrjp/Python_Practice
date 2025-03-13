#Daily temperatures
def get_result(temperatures: list[int])->list[int]:
   
    stack:list=[]
    result:list=[0]*len(temperatures)
  
    for idx,temp in enumerate(temperatures):
        while stack and temperatures[stack[-1]]<temp:
            prev_idx=stack.pop()
            result[prev_idx]=idx-prev_idx
        stack.append(idx)
            
    return result        

if __name__=="__main__":
    temperatures:list = [30,38,30,36,35,40,28]
    print(get_result(temperatures))
    