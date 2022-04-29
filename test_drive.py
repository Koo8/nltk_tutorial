import  string
letters = string.ascii_lowercase
print(type(letters))
mylength = 3

# Create all patterns possible with 26 letters into {length_value} of strings. e.g. {ab,af, gh ...}
def create_all_patterns(letter, length_value):
    re = letter
    while length_value > 1:
        
        newre = []
        for ele in re:  
            # print(f're is {re}')          
            for each in letter:
               newre.append(ele+each)
            
        re = newre
        
        length_value -= 1
        # print(f're new is {re}, and length changed to {length_value}')
    print(len(re))
    return re                
    

create_all_patterns(letters, 3 )


