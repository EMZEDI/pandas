Part 1
This part asks you to analyze a dataset using libraries. To learn more about movies grosses, we have provided you with two csv's: movies_data.csv and genre_data.csv. The urls to the files are
https://raw.githubusercontent.com/williamykzhang/MAIS_CE/master/genre_data.csv
and
https://raw.githubusercontent.com/williamykzhang/MAIS_CE/master/movies_data.csv
The file movies_data.csv contains information about movies such as their title, imdb rating, length, rank, rating, studio, worldwide gross, and year in a comma separated format as shown below. CSV example 1
The file genre_data.csv contains the genre for each movie in the movies_data.csv file, as shown below. CSV example 2
Question 1

In the provided cell, load the datasets from their urls, parse the information and determine the average IMDB rating for each of the genres using the pandas library. https://pandas.pydata.org/.
Plot the results onto a graph using the pyplot module of the matplotlib library. https://matplotlib.org/.
Note. You are not allowed to use other libraries, and you are required to write all the code in the following cell. You are also not allowed to run bash commands. You must use the libraries we ask you to use.
[ ]
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

 
The output of the cell should be similar to the results shown below.
results1.1.png results1.2.png
Question 2

In the provided cell, using the same dataset and the pandas library, parse the information and display the number of movies in the dataset which have each rating (G, PG, PG-13, etc.). https://pandas.pydata.org/.
Plot the results onto a graph again using the pyplot module of the matplotlib library. https://matplotlib.org/.
[ ]
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
 
The output of the cell should be similar to the results shown below:
results2.1.png
results2.2.png
Part 2
For the second half of the coding challenge, you are not allowed to use libraries. More specifically, you are not allowed to use imported code from the standard library nor from external libraries.
First Task

Your first task is to write a helper function to_grade_point which converts a grade out of 100 into a tuple whose first entry is a string representing the letter grade and whose second entry is a float representing the Grade Points.
Letter Grade Table
Note. Inputs are assumed to be valid. That is, inputs will be integers from 0 to 100 inclusive.
[ ]
 def to_grade_point(grade_out_100):
  grade_dict = {
      (85, 100) : ('A', 4.0),
      (80, 84) : ('A-', 3.7),
      (75, 79) : ('B+', 3.3),
      (70, 74) : ('B', 3.0),
      (65, 69) : ('B-', 2.7),
      (60, 64) : ('C+', 2.3),
      (0, 59) : ('F', 0.0),
  }
  for min, max in grade_dict:
    if min <= grade_out_100 <= max:
      return grade_dict[(min, max)]
You can test your code with the following snippet. If your code is correct, you should see
Example Code 1
[ ]
 for grade in [0, 99, 80, 85, 84, 60, 59, 74]:
  print("{} -> {}".format(grade, to_grade_point(grade)))
 0 -> ('F', 0.0)
99 -> ('A', 4.0)
80 -> ('A-', 3.7)
85 -> ('A', 4.0)
84 -> ('A-', 3.7)
60 -> ('C+', 2.3)
59 -> ('F', 0.0)
74 -> ('B', 3.0)
Second Task

Your second task is to write a class named GradeRecords with a certain specification. This part will use the helper function defined in the first part so make sure to do that first.
A GradeRecords object has the following attributes:
term, a string representing the current semester;
grades, a list object containing tuples, where the first entry of each tuple is a string representing the code of the class, the second entry of each tuple is the grade out of 100, and the third entry is the number of credits for this course. grades can be initialized (see below) as an empty list.
num_courses an int which contains the number of courses in the record. This can be initialized as 0.
Note. You are not allowed to add more attributes.
Furthermore, a GradeRecords object has the following methods:
an initialization method which takes as input the current term and initializes the three attributes;
add_course, a method which takes a string representing the course code, an int for the grade out of 100 and the number of credits. The method adds a new tuple to grades.
get_best_courses, a method which takes no parameters and outputs a list of course codes with the best grades. For instance, if the best grade is a 'B', it will output all course codes with a 'B', i.e. all courses codes with a grade between 70 and 74 (inclusive). You are required to use the helper function defined in the first part.
get_GPA, a method which outputs the Grade Point Average for the semester, assuming all classes all weighted by the number of credits. You are required to use the helper function from the first task. Round it to one decimal place.
to_dict, a method which returns a dict whose keys are the class codes and whose corresponding values are the letter grades. Once again, you must use the helper function from the first task.
Note. All inputs are assumed to be valid. Particularly, you may assume there won't be duplicate class codes.
[ ]
 class GradeRecords:

  # constructor
  def __init__(self, term_str, grades_list = [], course_num = 0):
    # current semester in string
    self.term = term_str 
    # grades list which contains tuples containing the code of the class and the
    #-grade outta 10 
    self.grades = grades_list
    # integer representing the number of courses
    self.num_courses = course_num

  # methods
  def add_course(self, course_code, grade_out_100, num_creds):
    # simply append the tuple into the initial list
    self.grades.append((course_code, grade_out_100, num_creds))
    self.num_courses += 1

  def get_best_courses(self):
    # first, make a new list like grades list

    course_name_list = []
    course_dict = {}

    for class_tuple in self.grades:
      # change the grade into letter 
      grade_letter = to_grade_point(class_tuple[1])[0] 

      if grade_letter not in course_dict:
        course_dict[grade_letter] = [class_tuple[0]]
      
      else:
        course_dict[grade_letter].append(class_tuple[0])
    # sort the keys of the dict and extract the courses names
    letters = list(course_dict.keys())
    letters.sort()

    return course_dict[letters[0]]

  def get_GPA(self):
    sum = 0.0
    for class_tuple in self.grades:
      grade_out_4 = to_grade_point(class_tuple[1])[1]
      sum += grade_out_4

    return round(sum / len(self.grades), 1)

  def to_dict(self):
    final_dict = {}

    for class_tuple in self.grades:
      grade_letter = to_grade_point(class_tuple[1])[0]
      final_dict[class_tuple[0]] = grade_letter

    return final_dict


You can test your code with the following snippet. If your code is correct you should see
code example 2
[ ]
 gr = GradeRecords("Fall 2019")
print("First batch")
print("Term: {}".format(gr.term))

gr.add_course("COMP 202", 83, 3)
gr.add_course("CLAS 203", 75, 3)
gr.add_course("LING 360", 81, 3)

print("Number of courses: {}".format(gr.num_courses))
print("Best courses: {}".format(gr.get_best_courses()))
print("GPA: {}".format(gr.get_GPA()))
print("Dictionary: {}".format(gr.to_dict()))

print() 

print("Second batch")
print("Term: {}".format(gr.term))

gr.add_course("COMP 551", 67, 4)
gr.add_course("HIST 318", 88, 3)

print("Number of courses: {}".format(gr.num_courses))
print("Best courses: {}".format(gr.get_best_courses()))
print("GPA: {}".format(gr.get_GPA()))
print("Dictionary: {}".format(gr.to_dict()))
 First batch
Term: Fall 2019
Number of courses: 3
Best courses: ['COMP 202', 'LING 360']
GPA: 3.6
Dictionary: {'COMP 202': 'A-', 'CLAS 203': 'B+', 'LING 360': 'A-'}

Second batch
Term: Fall 2019
Number of courses: 5
Best courses: ['HIST 318']
GPA: 3.5
Dictionary: {'COMP 202': 'A-', 'CLAS 203': 'B+', 'LING 360': 'A-', 'COMP 551': 'B-', 'HIST 318': 'A'}
Third Task

For the third task, please complete the following function that multiplies two matrices. Usage of any other libraries containing functions that perform matrix multiplication (including but not limited to numpy) is NOT allowed.
[ ]
def matrix_mult(x,y):        #make sure the shapes match so we can perform matrix multiplication    assert len(x[0]) == len(y)        #create the result with the correct shape    result = [[0 for j in range(len(y[0]))] for i in range(len(x))]        #TODO: multiply x and y    #hint: use nested loops    # start from the rows of x and right after, iterate    # thru the colns of y to multiply the matrices!    for row1 in range(len(x)):      # then iterate thru the number of clons of y (row 0)      for coln2 in range(len(y[0])):        # iterate thru rows of y        for row2 in range(len(y)):          # using the formula of matrix multiplication          result[row1][coln2] += x[row1][row2] * y[row2][coln2]    return result

Run the following block to check if your implementation is correct
[ ]
x = [[1,2],[3,4]]y = [[1,2],[3,4]]assert [[7,10],[15,22]] == matrix_mult(x,y)x = [[1,2,3],[3,4,5]]y = [[1,2],[3,4],[5,6]]assert [[22,28],[40,52]] == matrix_mult(x,y)
