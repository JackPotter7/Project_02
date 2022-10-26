#Imports
import json
import matplotlib.pyplot as plt
import csv

#Reading Data

with open('/Users/jackpotter/Desktop/CMC/Classes/Soph Fall/CS 40/topic_06_matplotlib/project_02/narcos.json') as f:
    narcos_data = json.load(f)

street_data = open('/Users/jackpotter/Desktop/CMC/Classes/Soph Fall/CS 40/topic_06_matplotlib/project_02/Street_Names.csv')

street_read = csv.reader(street_data)

street_list = list(street_read)



#Compiling Data 

#Average Ratings by episode
ratings_accumulator = []
for i in range(len(narcos_data['_embedded']['episodes'])):
    ratings_accumulator.append(narcos_data['_embedded']['episodes'][i]['rating']['average'])

'''
episodes_accumulator = []
for i in range(len(narcos_data['_embedded']['episodes'])):
    episodes_accumulator.append(i+1)
'''

episodes_accumulator = []
seasons = [1,2,3]
episodes = [1,2,3,4,5,6,7,8,9,10]

for season in seasons:
    for episode in episodes:
        episodes_accumulator.append('S' + str(season) + 'E' +  str(episode))







#Total number of streets starting with letter
counts_first_street_T = 0
counts_first_street_S = 0
counts_first_street_A = 0


for i in range(1,len(street_list)):
    if street_list[i][0][0] == 'T':
        counts_first_street_T += 1
    elif street_list[i][0][0] == 'S':
        counts_first_street_S += 1
    elif street_list[i][0][0] == 'A':
        counts_first_street_A += 1

# Percentage of streets 
per_first_street_T = 100*counts_first_street_T / (len(street_list)-1)
per_first_street_S = 100*counts_first_street_S / (len(street_list)-1)
per_first_street_A = 100*counts_first_street_A / (len(street_list)-1)
#total number of episodes starting with letter

counts_first_epi_T = 0
counts_first_epi_S = 0
counts_first_epi_A = 0


for i in range(len(narcos_data['_embedded']['episodes'])):
    if narcos_data['_embedded']['episodes'][i]['name'][0].lower() == 't':
        counts_first_epi_T += 1
    elif narcos_data['_embedded']['episodes'][i]['name'][0].lower() == 's':
        counts_first_epi_S += 1
    elif narcos_data['_embedded']['episodes'][i]['name'][0].lower() == 'a':
        counts_first_epi_A += 1
#Percentage of episodes 
per_first_epi_T = 100*counts_first_epi_T / len(narcos_data['_embedded']['episodes'])
per_first_epi_S = 100*counts_first_epi_S / len(narcos_data['_embedded']['episodes'])
per_first_epi_A = 100*counts_first_epi_A / len(narcos_data['_embedded']['episodes'])

# Compliling Data into a dictionary
data_dict = {'Streets-A': per_first_street_A, 'Streets-T': per_first_street_T, 'Streets-S': per_first_street_S, 'Episodes-A':per_first_epi_A, 'Episodes-T':per_first_epi_T, 'Episodes-S':per_first_epi_S}


# Pulling Keys and Values to use as x/y axis
names_data_list = list(data_dict.keys())
values_data_list = list(data_dict.values())

### PLOTTING 
'''
new_colors = ['green','green','green','red','red','red']
plt.bar(names_data_list,values_data_list, color =new_colors)
plt.title('Percentage of Episode Titles in Narcos and Streets Names in San Francisco starting with A, T, + S', fontsize = 10)
plt.xlabel('Episode/Street Starting with Letter')
plt.xticks(fontsize = 6)
plt.ylabel('Percentage of Episodes Titles/Streets')
plt.grid(True)
plt.show()
'''


plt.plot(episodes_accumulator,ratings_accumulator, color = 'red', marker = 'o')
plt.title('Narcos Episode vs. Average Rating')
plt.xlabel('|          Season 1          |          Season 2          |          Season 3          | \n Episode',fontsize = 10)
plt.xticks(fontsize  = 3.8)
plt.ylabel('Average Rating')
plt.grid(True)
plt.show()
