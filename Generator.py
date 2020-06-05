#Rogue Trader system generator

#Generate system feature

import pandas
import random


def roll(up,down):
    random.randrange(up, down)
    

df = pandas.read_csv('System.csv', sep=';')

#print (df)

row = random.randrange(1,100)

#print (row)

i = 0 
while row > df.at[i, 'R1']:
    i +=1
    if i == 11:
        break
    
#nieudolna pętla wymaga korekty
i -= 1
    
#Paramentry range do funkcji randrange do generowania 
#typu gwiazdy zawarte w tabeli system, przypisane jako zmienne dla wygody
        
sr1 = df.at[i, 'SR1']
sr2 = df.at[i, 'SR2']


#SF star feature
sf = df.at[i, 'Feature']

print ('System feature:\t\t', sf)                                          

#stt star type table
stt = pandas.read_csv('Star.txt', sep = '\t')

#random_star - star type determined by sr1 & sr2
random_star = random.randrange(sr1,sr2)
#print (random_star)                         #dotąd ok

star_row = 0

while random_star > stt.at[star_row, 'Range2']:
    star_row += 1
    if random_star == 100:
        star_row = 11
        break
    
print ('Star type:\t\t',stt.at[star_row, 'Class'])
print ('Star description:', '\n',stt.at[star_row, 'Description'])

inner_flag = stt.at[star_row, 'Inner']
biosphere_flag = stt.at[star_row, 'Biosphere']
outer_flag = stt.at[star_row, 'Outer']
life_flag = stt.at[star_row, 'Natural Life']

#test flag:
print ('Inner Cauldron:\t\t\t\t', inner_flag)
print ('Primary biosphere: \t\t\t', biosphere_flag)
print ('Outer reaches: \t\t\t\t', outer_flag)
print ('Possible natural life in the system: \t', life_flag)

#inner cauldron objects
inner_objects = 0
if inner_flag == 'Weak':
    inner_objects = random.randrange(1,6) -2
    if inner_objects < 0:
        inner_objects = 0
elif inner_flag == 'Normal':
    inner_objects = random.randrange(1,6)
elif inner_flag == 'Dominant':
    inner_objects = random.randrange(1,6) +2
else:
    inner_objects = 0
    
print ('Number of objects in Inner Cauldron is\t', inner_objects)

#primary biosphere objects
biosphere_objects = 0
if biosphere_flag == 'Weak':
    biosphere_objects = random.randrange(1,6) -2
    if biosphere_objects < 0:
        biosphere_objects = 0
elif biosphere_flag == 'Normal':
    biosphere_objects = random.randrange(1,6)
elif biosphere_flag == 'Dominant':
    biosphere_objects = random.randrange(1,6) +2
else:
    biosphere_objects = 0
    
print ('Number of primary biosphere objects is:\t', biosphere_objects)

#outer reaches objects
outer_objects = 0
if outer_flag == 'Weak':
    outer_objects = random.randrange(1,6) -2
    if outer_objects < 0:
        outer_objects = 0
elif outer_flag == 'Normal':
    outer_objects = random.randrange(1,6)
elif outer_flag == 'Dominant':
    outer_objects = random.randrange(1,6) +2
else:
    outer_objects = 0
    
print ('Number of objects in outer reaches is:\t', outer_objects)
        
#inner_features - table with objects in inner cauldron

inner_features = pandas.read_csv('Inner Cauldron.tsv', sep = '\t')

inner_list = []



