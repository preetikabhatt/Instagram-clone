print("hello World")
print('bipul\'s')
print("bbs\"ss")
# \' ==> ' (In b/w)
# \" ==> " (In b/w)
# \\" ==> " (at end of the block)
# \t ==> tab
# \n ==> new line
# \b ==> backspace
# \\ ==> \
print("\\")
print(' a\\\\b ')
print('\\" \\\'')  # output --> /" /' 

# Q2--> /\/\/\
#sol-->
print("/\\/\\/\\") #type 1
print("/\/\/\\") # type 2

#Q3 --> \' \" \\ \t \n \b 
#sol-->
print("\\\' \\\" \\\ \\t \\n \\b")

# RAW STRING -->
print(r"Hello\"") # r 


##########
var = "que"
print(var)
var = "hello"
print(var)

first_name_of_user = "Bipul"  # snake convention
firstNameOfUser = "bipul"


var1,var2 = "bipul","jaiswal"
print(var1)
print(var2)

var1=var2=var3=5
print(var3)

var1=2 
var2=3
print(var1**var2)


var1=2 
var2=0.5
print(var1**var2)


#round(calculation, round value)
print(round(2**0.5)) #round()
print(round(2**0.5,7)) #round()


var= 2**0.5
print(round(var,7))#round(calculation, round value)



var= 5//2

print(var) #round(calculation, round value)

# // ==> gives integer output
# ** ==> use as power
# % ==> gives remainder


#############


#str() ==> changes anything to string
#int() ==> changes anything to int
#float() ==> changes anything to float
a=1 
b="2.2"
print(a+float(b))
