def get_ascii_values(input_string):
    ascii_values = []
    modified_string=""
    checked_values=[]

    for char in input_string:
        char_ascii = ord(char)
        ascii_values.append(char_ascii)

    
    checked_values.append(ascii_values[0])

    for val in range(1,len(ascii_values)-1):

        if checked_values.count(ascii_values[val])>0:
            continue

        elif val==len(ascii_values)-1 and ascii_values[val]%2==0:
                break
        
        else:
            if ascii_values[val]%2==0:
                ascii_values[val+1]=ascii_values[val+1]+ascii_values[val]%7
            
            else:
                ascii_values[val-1]=ascii_values[val-1]-ascii_values[val]%5
            
            checked_values.append(ascii_values[val])
    
    
        
    for val in ascii_values:
        if(val>=0 and val<=255):
            modified_string+=chr(val)
            print(val,chr(val))
        else:
            modified_string+=chr(83)
            


       
                
    return modified_string

# Example usage:
input_string = input("enter your string:\t")
result = get_ascii_values(input_string)

print(result)
