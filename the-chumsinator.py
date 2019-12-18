import random

the_chums = ['Harry','Arran','Dave','Iliyan','James','Joe','Liam','Mark','Rowan','Sean']
random_chumsington =  []

for i in range(len(the_chums)):
    if(the_chums):
        random_chum = random.choice(the_chums)
        the_chums.remove(random_chum)
        random_chumsington.append(random_chum)

for i in range(0,random.randint(1, 35)):
    random.shuffle(random_chumsington)

random_chumsington
