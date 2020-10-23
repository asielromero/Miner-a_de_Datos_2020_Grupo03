#!/usr/bin/env python
# coding: utf-8

# EJERCICIO 3: Diccionarios

# In[ ]:


Familia={'Aurelio':60,'Carmen':59,'Carlos':30,'Natalia':29,'Marco':23,'Mildred':14}
Edades=[Familia['Aurelio'],Familia['Carmen'],Familia['Carlos'],Familia['Natalia'],Familia['Marco'],Familia['Mildred']]
Edades.sort()
 
for Nombres in Familia:
    print(Nombres) 
    
Familia['Hugo']=31
Familia['Gaby']=29


# EJERCICIO 4:

# In[ ]:


import random

Set1_25=set()

for i in range(100):
    Set1_25.add(random.randint(1,25))
    
print(Set1_25)
print(len(Set1_25))

Set1_10=set()

for i in range(6):
    Set1_10.add(random.randint(1,10))
print(Set1_10)

print(Set1_10.issubset(Set1_25))

