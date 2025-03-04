input_list=["neet","code","love","you"]
encoded_list=[]
decoded_list=[]

encoding_dict={chr(ascii_num):str(ascii_num) for ascii_num in range(ord("a"),ord("z")+1)}

decoding_dict={v:k for k,v in encoding_dict.items()}

for input in input_list:
    encoded_string=""
    for char in input:
        encoded_string+=encoding_dict[char]+"#"
    encoded_list.append(encoded_string)
 
final_encoded_string="$".join(encoded_list)    
print(final_encoded_string)    

split_encoded_string=final_encoded_string.split("$")

for encoded_word in split_encoded_string:
    decoded_string=""
    temp=encoded_word.rstrip("#").split("#")
    for num in temp:
        decoded_string+=decoding_dict[num]
    decoded_list.append(decoded_string)
          
print(decoded_list)

  
        
    

