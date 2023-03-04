# ----------------------------Encoding to a secret code------------------------

# 1. move first 2 character to the end
# 2. add 2 character to the begining
# 2. add 2 character in the middle
# 3. add 2 character to the end 

name = "Mishuk"

# shukMi
en_name = "ba" + name[2:] + "86" + name[:2] + "ma"
#name = name[2:] + name[:-4]


print(en_name)


# decode 
de_name= en_name[-4:-2] + en_name[2:6] 
print(de_name)
