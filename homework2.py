# ბილეთი ღირს 25 ლარი, მაგრამ ბავშვებისთვის უფასოა. გვყავს 13 ადამიანი , აქედან 10 დიდია და 3 ბავშვი.
# გამოითვალეთ რამდენი ლარი დასჭირდებათ
ammount_of_adulte = 0
ammount_of_kids = 0
total_cost = 0

for i in range (3):

    age=int(input("enter your age : "))
    if age > 18:
        print("25 lari")
        ammount_of_adulte+=1 
        total_cost+=25
        print("jamshi gadasaxdeli iqneba "  +  str (total_cost))
    elif age <=18  and age>0:
         print("0 lari")
         ammount_of_kids+=1
    else :
        print("0 lari")
print( " sul iqneba "  +  str(ammount_of_kids) + " bavshvi " + "da  "  +  str(ammount_of_adulte) + " didi")        

