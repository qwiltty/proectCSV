import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('IMDB-Movie-Data.csv')


df = df[['Title', 'Rating', 'Revenue (Millions)', 'Runtime (Minutes)', 'Metascore']]
df = df.dropna(subset=['Rating', 'Revenue (Millions)', 'Runtime (Minutes)', 'Metascore'])


runtime_rating = df['Runtime (Minutes)'].corr(df['Rating'])
runtime_revenue = df['Runtime (Minutes)'].corr(df['Revenue (Millions)'])
runtime_metascore = df['Runtime (Minutes)'].corr(df['Metascore'])


if runtime_rating > 0.5 and runtime_rating <= 1:
    result1 = f"Продолжительность фильма положительно влияет на рейтинг фильма."
elif runtime_rating >= -1 and runtime_rating < -0.5:
    result1 = f"Продолжительность фильма отрицательно влияет на рейтинг фильма."
elif runtime_rating >= -0.5 and runtime_rating < 0.5:
    result1 = f"Продолжительность фильма не влияет на рейтинг фильма."

if runtime_revenue > 0.5 and runtime_revenue <= 1:
    result2 = f"Продолжительность фильма положительно влияет на заработок фильма."
elif runtime_revenue >= -1 and runtime_revenue < -0.5:
    result2 = f"Продолжительность фильма отрицательно влияет на заработок фильма."
elif runtime_revenue >= -0.5 and runtime_revenue < 0.5:
    result2 = f"Продолжительность фильма не влияет на заработок фильма."

if runtime_metascore > 0.5 and runtime_metascore <= 1:
    result3 = f"Продолжительность фильма положительно влияет на оценку критиков."
elif runtime_metascore >= -1 and runtime_metascore < -0.5:
    result3 = f"Продолжительность фильма отрицательно влияет на оценку критиков."
elif runtime_metascore >= -0.5 and runtime_metascore < 0.5:
    result3 = f"Продолжительность фильма не влияет на оценку критиков."


print("Результаты анализа:")
print(result1)
print(result2)
print(result3)
average_values = df.groupby('Runtime (Minutes)').agg({'Rating': 'mean', 'Metascore': 'mean', 'Revenue (Millions)': 'mean'}).reset_index()
print(average_values)

# df.plot(x = 'Runtime (Minutes)', y = 'Revenue (Millions)', kind = 'scatter')
# df.plot(x = 'Runtime (Minutes)', y = 'Rating', kind = 'scatter')
df.plot(x = 'Runtime (Minutes)', y = 'Metascore', kind = 'scatter')

# df.plot(x='Runtime (Minutes)', y='Metascore', kind='barh')
# df.plot(x='Runtime (Minutes)', y='Rating', kind='barh')
# df.plot(x='Runtime (Minutes)', y='Revenue (Millions)', kind='barh')

plt.show()
