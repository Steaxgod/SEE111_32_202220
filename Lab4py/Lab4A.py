# Farid Hasanov
# Lab#4A
import csv
#------Main Code--->

d_num = 0
l_num = 0

typeList = []
brandList = []
cpuList = []
ramList = []
hdd1List = []
noHDDList = []
hdd2List = []
ocList = []
yrList = []

#------------------{Code}--------------->>>
with open("C:\SEE111_32_202220\Lab#4py\.csv\lab4a.csv") as csvfile:        #On the different divice,change directory.
    file = csv.reader(csvfile)
    for row in file:

      typeList.append(row[0])
      brandList.append(row[1])
      cpuList.append(row[2])
      ramList.append(row[3])
      hdd1List.append(row[4])
      noHDDList.append(row[5])
     
      if row[5] == '1':
         
          hdd2List.append(" ")
          ocList.append(row[6])
          yrList.append(row[7])

         



      else:
          #print(row[6])
          hdd2List.append(row[6])
          ocList.append(row[7])
          yrList.append(row[8])







      type =  (row[0])               #Stands for Type       
      brand = (row[1])               #Stands for Brand       
      cpu = (row[2])                 #Stands for CPU
      ram = (row[3])                 #Stands for RAM
      hdd1 =  (row[4])               #Stands for 1stHDD
      noHDD = (row[5])            #Stands for how many HDD 1 or 2
      cyr = 22

      if noHDD == '1':

          hdd2 = ' '
          oc = (row[6])
          yr = (row[7])

          df = int(cyr) - int(yr)

          if df >= 2:

              if type == 'D':

                  d_num = d_num + 1

              else:

                  l_num = l_num + 1

          else:

                print("Your computer is new!")

      else:

          hdd2 = (row[6])
          oc = (row[7])
          yr = (row[8])

          df = int(cyr) - int(yr)

          if df >= 2:

              if type == 'D':

                  d_num = d_num + 1

              else:

                  l_num = l_num + 1 

          else:

             print("Your computer is new!")
        
print(ram)




tasmod = d_num * 2000  # TASMOD - The Amount Spended On Desktops
tasmol = l_num * 1500  # TASMOL - The Amount Spended On Laptops 


#-----------------{Display}-------------->>>
print("------------------------------------------------------------------->>>")

print("|Desktops",d_num," | $",tasmod,"|")       
print("|Laptops  ",l_num," | $",tasmol,"|")

print("------------------------------------------------------------------->>>")


print("  ")
print("  ")
print("  ")


print("----" * 10)
print("typeList =|",typeList,'|\n')
print("----" * 10)
print("brandList =|",brandList,'|\n')
print("----" * 10)
print("cpuList = |",cpuList,'|\n')
print("----" * 10)
print("ramList =|" ,ramList,'|\n')
print("----" * 10)
print("hdd1List =|" ,hdd1List,'|\n')
print("----" * 10)
print("noHDDList =|",noHDDList,'|\n')
print("----" * 10)
print("hdd2List =|",hdd2List,'|\n')
print("----" * 10)
print("ocList =|",ocList,'|\n')
print("----" * 10)
print("yrList =|",yrList,'|\n')
print("----" * 10)


#------------------{Thanks}-------------->>>


