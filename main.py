### INF601 - Advanced Programming in Python
### Alexander Escobedo
### Mini Project 2

import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# Create charts folder if it does not exists
charts = Path('charts')
if not charts.exists():
    Path(r'charts').mkdir()

# Number of movies with rating 8.5 or above

df_IMDB = pd.read_excel("./data/IMDB_processed_data.xlsx", index_col=0)

high_rated = df_IMDB[df_IMDB["Ratings"] >= 8.5]

high_rated["Ratings"].hist(bins=20, edgecolor="black", color = "green")
plt.xlabel("Ratings")
plt.ylabel("Number of Movies")
plt.title("Number of Movies per Rating 8.5 and Above")
plt.savefig(str(charts / "movies_high_rating_hist.png"))
plt.show()

# Number of males vs. females

df_adult = pd.read_csv("./data/adult.csv", index_col=0)

df_adult['sex'].value_counts().plot(kind='bar', color=['b','m'])
plt.xlabel("Gender")
plt.ylabel("Count")
plt.title("Number of Adults per Gender")
plt.savefig(str(charts / "adult_gender_count.png"))
plt.show()

# Age distribution

df_health = pd.read_csv("./data/health_lifestyle_dataset.csv")

df_health['age'].hist(bins=20, color='skyblue', edgecolor='black')
plt.xlabel("Age")
plt.ylabel("Number of Individuals")
plt.title("Number of Individuals per Age")
plt.savefig(str(charts / "age_distribution.png"))
plt.show()





# This project will be using Pandas dataframes. This isn't intended to be full blown data science project. The goal here is to come up with some question and then see what API or datasets you can use to get the information needed to answer that question. This will get you familar with working with datasets and asking questions, researching APIs and gathering datasets. If you get stuck here, please email me!
#
# (5/5 points) Initial comments with your name, class and project at the top of your .py file.
# (5/5 points) Proper import of packages used.
# (20/20 points) Using a data source of your choice, such as data from data.gov or using the Faker package, generate or retrieve some data for creating basic statistics on. This will generally come in as json data, etc.
# Think of some question you would like to solve such as:
# "How many homes in the US have access to 100Mbps Internet or more?"
# "How many movies that Ridley Scott directed is on Netflix?" - https://www.kaggle.com/datasets/shivamb/netflix-shows
# Here are some other great datasets: https://www.kaggle.com/datasets
# (10/10 points) Store this information in Pandas dataframe. These should be 2D data as a dataframe, meaning the data is labeled tabular data.
# (10/10 points) Using matplotlib, graph this data in a way that will visually represent the data. Really try to build some fancy charts here as it will greatly help you in future homework assignments and in the final project.
# (10/10 points) Save these graphs in a folder called charts as PNG files. Do not upload these to your project folder, the project should save these when it executes. You may want to add this folder to your .gitignore file.
# (10/10 points) There should be a minimum of 5 commits on your project, be sure to commit often!
# (10/10 points) I will be checking out the main branch of your project. Please be sure to include a requirements.txt file which contains all the packages that need installed. You can create this file with the output of pip freeze at the terminal prompt.
# (20/20 points) There should be a README.md file in your project that explains what your project is, how to install the pip requirements, and how to execute the program. Please use the GitHub flavor of Markdown. Be thorough on the explanations.

