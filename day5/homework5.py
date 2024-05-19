#user's age and father's age ,print each year how many times her father will be older then her 
    
my_age=int(input("enter your age : "))
fathers_age=int(input("enter your fathers age : "))
year=int(input("enter year : "))
for i in  range(40):
    print(str(year + i) +  " my father will be " + str ((fathers_age + i) / (my_age + i)) + " years older" )


    



        