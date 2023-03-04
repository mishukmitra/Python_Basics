name = "Mishuk is married to Manashi"

#--------------------encode-------------------------------------------
words = name.split()
print(words)

add_1 = "ma"
add_2 = "ba"

import reverse_func as r
l = []


for i in range (len(words)):
    if i == 0:
        word = add_1 + words[i] 
       
    elif i == (len(words)-1):
        word  = add_2 + words[i]
       
    else: 
        word = r.reverse(words[i])
        

    l.append(word)
   

print(l)

encode_name = ' '.join(l)
print(encode_name)



#-------------------------------------------decode-------------------------

n = encode_name.split()
print(n)

d=[]

for i in range (len(n)):
    if i == 0:
        de_word = n[i][2:]
       
    elif i == (len(n)-1):
        de_word  =  n[i][2:]
       
    else: 
        de_word = r.reverse(n[i])

    d.append(de_word)

decode_name = ' '.join(d)
print(decode_name)