import pandas as pd

import matplotlib.pyplot as plt

# first read the data with panda
df_genre = pd.read_csv(
    'https://raw.githubusercontent.com/williamykzhang/MAIS_CE/master/genre_data.csv')

df_movie = pd.read_csv(
    'https://raw.githubusercontent.com/williamykzhang/MAIS_CE/master/movies_data.csv')

# now, we only read the columns we want to manipulate the data
data = pd.merge(df_genre, df_movie)
data = data[['Main_Genre', 'imdb_rating']]
dict_data = {}

for i in range(data.shape[0]):

  if data.iloc[i,0] in dict_data:
    dict_data[data.iloc[i,0]].append(data.iloc[i,1])

  else:
    dict_data[data.iloc[i,0]] = [data.iloc[i,1]]

genre = []
final_rates = []

# now get the avgs
for key in dict_data:

  length = len(dict_data[key])
  summ = 0
  for rate in dict_data[key]:
    summ += rate 
  genre.append(key)
  dict_data[key] = summ/length

genre.sort()
for key2 in genre:
  final_rates.append(dict_data[key2])

final = pd.DataFrame({'Main_Genre':genre, 'imdb_rating':final_rates})
display(final)
################################################################################
plt.figure(figsize=(20,10))
plt.title("Average IMDB Rating")
plt.bar(genre, final_rates)
plt.ylabel("Main_Genre")
plt.xlabel("IMDB Rating")
plt.show()

 

import pandas as pd

import matplotlib.pyplot as plt

# first read the data with panda
data = pd.read_csv(
    'https://raw.githubusercontent.com/williamykzhang/MAIS_CE/master/movies_data.csv')

# now, we only read the columns we want to manipulate the data
data = data[['rating', 'title']]
dict_data = {}

for i in range(data.shape[0]):

  if data.iloc[i,0] in dict_data:
    dict_data[data.iloc[i,0]].append(data.iloc[i,1])

  else:
    dict_data[data.iloc[i,0]] = [data.iloc[i,1]]

# now we have the dict, we calculate the length of each value which is list
for key in dict_data:
  dict_data[key] = len(dict_data[key])


final_series = pd.Series(dict_data)
print(final_series.to_string())
key_list = []

value_list = []
for key2 in dict_data:

  key_list.append(key2)
  value_list.append(dict_data[key2])

################################################################################
plt.figure()
plt.title("Number of movies per rating")
plt.bar(key_list, value_list)
plt.ylabel("Count")
plt.xlabel("Ratings")
plt.show()
 
