import csv



f_name = [] # First Name
l_name = [] # Last Name
p_num = [] # Phone Number
e_adress = [] # Email  Adress
d_name = [] # Department
e_pos = [] # Employee's  position


print("|---------------|")
print("| Farid Hasanov |") 
print("|---------------|")
print("|     Lab#6     |")
print("|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|")
print("|     First  Name          Last Name                            Phone Number                           Email  Adress                     Department             Employee's Position             |")
print("|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|")
with open(" Select Your Dirrectory for lab6.csv ") as csvfile:        
    file = csv.reader(csvfile)
    for row in file:

        

            
            print("|Name :",row[0].rjust(10),"|Last Name:",row[1].rjust(10),"|Phone Number: ",row[2].rjust(15),"|Email Adress:",row[3].rjust(30),"|Department:",row[4].rjust(20),"|Employee's Position:",row[5].rjust(15),"|")


print("|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|")