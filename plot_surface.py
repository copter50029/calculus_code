age =          [16,17,15,20,24,13,17,18,16,18,19,20,22,25,26,31,33,16,21,12,36,14,25,35,6,20,10,23,11,26]
gender =       ['f','m','m','f','m','f','f','f','f','m','f','m','m','m','f','f', 'f', 'f', 'f', 'f', 'f', 'm', 'm', 'f', 'm', 'm', 'm', 'm', 'm', 'm']         #f is female, m is male
rating =       [5,5,4,5,3,4,3,4,5,2,1,2,5,4,5,4,2,3,2,4,3,1,1,3,5,5,1,5,4,2]         #rating [1,2,3,4,5] 5 is the highest score rating and 1 is the lowest score rating
vibe =         [5,5,3,2,4,5,3,5,4,2,1,1,5,5,5,1,4,2,3,5,2,4,1,3,5,1,4,2,5,3]           #vibe [1,2,3,4,5]   5 is the highest score and 1 is the lowest score
ice_or_hot =   ['i','h','i','i','i','h','i','i','i','h','h','i','i','i','h','h', 'h', 'i', 'h', 'i', 'i', 'h', 'i', 'i', 'i', 'h', 'i', 'h', 'h', 'i']
isStudent =    [1,1,1,0,0,1,1,0,1,0,0,0,0,0,0,2,5,3,2,1,4,4,3,1,2,1,4,5,3,5]    #0 is no, 1 is yes
isTeacher =    [0,0,0,1,1,0,0,0,0,0,0,0,0,1,1,2,1,5,4,4,5,1,2,3,5,3,4,2,1,3]    #0 is false, 1 is true
light_or_dark= [1,1,1,0,0,1,1,0,1,1,0,0,1,1,0,2,3,4,4,5,2,5,3,3,2,5,1,1,1,4] #0 is light, 1 is dark
love_coffee =  ['Yes','No','Yes','No','Yes','No','No','Yes','Yes','Yes','No','No','Yes','Yes','Yes','Yes', 'No', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'No', 'No', 'Yes', 'Yes', 'No', 'Yes']
cup_per_week = [2,2,1,5,6,3,2,1,2,2,5,4,7,5,7,9,2,4,3,12,0,13,8,10,6,14,5,15,7,1] #Number of cup per week


'''Dict'''
dict = {
        'age':age,
        'gender':gender,
        'rating':rating,
        'vibe':vibe,
        'ice_or_hot':ice_or_hot,
        'isStudent':isStudent,
        'isTeacher':isTeacher,
        'light_or_dark':light_or_dark,
        'love_coffee':love_coffee,
        'cup_per_week':cup_per_week,
        }

import pandas as pd
df = pd.DataFrame(dict) #create dataframe (df) from dict
print(df)                      #print dataframe (df)

#------------Part 2: Data Analysis--------------------------------
print(df.head())
print(df.tail())
print(df.sample(10))
print(df.columns)

# 2.1 Count NA/NaN values in each column
print(df.isna())
print(df.isna().sum())

# 2.2 Converting binary Nominal Variable Gender to numeric
df['gender'].replace({'m':1, 'f':0}, inplace=True)
print(df)

#DIY
df['ice_or_hot'].replace({'i':1, 'h':0}, inplace=True)
print(df)

#love_coffee
df['love_coffee'].replace({'Yes':1, 'No':0}, inplace=True)
print(df)
#df.love_coffee.replace(to_replace=['No', 'Yes'], value=[0, 1])

# 2.3 Show descriptive or summary statistics
print(df.describe())

# 2.4 Count the number of student
print(df['isStudent'].count())
print(df.isStudent.value_counts())
print(df.isTeacher.value_counts())

# 2.5 Show average rating score by 'ice_or_hot'
print(df.groupby(by='ice_or_hot').mean())
#print(df.groupby(by='light_or_dark').mean())

# 2.6 Select only the student
bool_idx_student = (df['isStudent'] == 1)
print(bool_idx_student)
print(df[bool_idx_student])

bool_idx_teacher = (df['isTeacher'] == 1)
print(df[bool_idx_teacher])

# 2.7 Filter (Age < 18, Rating <= 3, Love coffee)
#Filter
con1 = (df['age'] >= 18)
con2 = (df['rating'] <= 3)
con3 = (df['love_coffee'] == 1)

print(df[con1 & con2 & con3])
print(df[con1 | con2])

#------------Part 3: Visualization-------------------------
import matplotlib.pyplot as plt

plot01 = df['rating'].hist(bins=5)
plt.show(plot01)

plot02 = df['vibe'].hist(bins=5)
plt.show(plot02)

plot03 = df.plot.scatter(x='cup_per_week', y='light_or_dark')
plt.show(plot03)

plot04 = df.plot.scatter(x='cup_per_week', y='age',c='rating')
plt.show(plot04)

#add color map
plot05 = df.plot.scatter(x='cup_per_week', y='age',c='rating',colormap='viridis')
plt.show(plot05)

rating_and_vibe  = ['rating', 'vibe']
plot06 = df[rating_and_vibe].mean().plot.bar()
plt.show(plot06)

df1=df[con1 | con2 | con3]
rating_and_vibe  = ['rating', 'vibe','cup_per_week']
plot07 = df1[rating_and_vibe].mean().plot.bar()
plt.show(plot07)

df2=df[con2 & con3]
print(df2)
rating_and_vibe  = ['rating', 'vibe','cup_per_week']
plot08 = df2[rating_and_vibe].mean().plot.bar()
plt.show(plot08)

df['love_coffee_score']=0
status_cols_ = ['love_coffee']
for col in status_cols_:
  df['love_coffee_score'] += df[col]*5
df.head()
#print(df)

df['total_score'] = 0
status_cols = ['rating','vibe','love_coffee_score']

#sum

for col in status_cols:
  df['total_score'] += df[col]
df.head()
print(df)

print(df.sort_values("total_score",ascending=False))

col = ['rating','vibe','love_coffee_score','total_score']
df3 = df[col]
#df4=df3.sort_values(["total_score","rating"])
ax1=lines = df3.plot.line()
ax1.set(xlabel='ID', ylabel='Score',
       title='Customer Insight')
ax1.grid()
plt.show()


ax2=df3[col].mean().plot.bar()
ax2.set(xlabel='Catagory', ylabel='Score',
       title='Customer Insight')
ax2.grid()
plt.show()

'''------------------------------'''
plt.subplot(1,3,1)
ax3=df3[col].mean().plot.bar()
ax3.set(title='Mean')
ax3.grid()

plt.subplot(1,3,2)
ax4=df3[col].max().plot.bar()
ax4.set(title='Min')
ax4.grid()

plt.subplot(1,3,3)
ax5=df3[col].min().plot.bar()
ax5.set(title='Max')
ax5.grid()

'''------------------------------'''
#same scale only
col2 = ['rating','vibe','love_coffee_score']
df4 = df[col2]
#for col2 in col2:
df4.hist(alpha=0.4, bins=5)
plt.legend(col2)
