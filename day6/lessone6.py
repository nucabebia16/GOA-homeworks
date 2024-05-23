x=int(input(" enter  x your score :"))
y= int(input("enter y  your score :"))
z= int(input("enter  z your score :"))
arithmetic_average= (x + y + z)/ 3
if arithmetic_average > 9 :
    print("გილოცავ მატრიცელო შენ გადმოგეცა 300 ლარიანი ბანძი ტოსტერი რასაც შეალიე შეენი ცხოვრების წლები")
elif arithmetic_average < 5 :
    print(" გილოცავ  გაექეცი მატრიცას")

elif arithmetic_average >=5 and arithmetic_average <=9 :
    print(" you are mid")
else:
    
    print(" there is something wrong with you")

