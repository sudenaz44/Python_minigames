names_string = "Sude, Muslu, Nevin, Tina, Emir"
names= names_string.split(", ")
import random
num_items =len(names)
#print(num_items) ---> 5
random_choice = random.randint(0,num_items - 1)
#print(random_choice)---> 2 2 4 3 5 1 0 
print(names[random_choice])    #her isim karmaşık radom şekilde gelir.