import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('whitegrid')

Heart = pd.read_csv("heart.csv")

Heart.head().style.set_properties(**{'background-color':'pink','color':'grey','border-color':'black','font-size':'10pt','width':200})

Heart.shape
Heart.isna().sum()

Heart.columns

Heart['sex'].value_counts()

output = Heart.groupby('output').size()
output

def Heart_disease (row):
    if row == 0:
        return 'Absence'
    elif row == 1:
        return 'Presence'

Heart['Heart_disease'] = Heart['output'].apply(Heart_disease)

Hd = Heart.groupby('Heart_disease')['output'].count()
Hd

Heart.head()

plt.figure(figsize = (10,9))
plt.pie(Hd,labels= ['Absence','Presence'],autopct= '%0.1f%%')
plt.title('Heart Disease Population (%)', fontsize=20)
plt.show()

plt.figure(figsize = (18,9))
sns.countplot(x = 'age',data = Heart)
plt.title('Population of age', fontsize=19)
plt.xlabel('Age',fontsize=18)
plt.ylabel('Count',fontsize=18)
plt.show()

Min_Age = Heart['age'].min()
Max_Age = Heart['age'].max()
Mean_Age = Heart['age'].mean()
print('Minimum Age:>',Min_Age)
print('Maximum Age:>',Max_Age)
print('Mean Age:>',Mean_Age)


#Categorical Analysis

Young_Ages=Heart[(Heart['age']>=29) & (Heart['age']<40)]
Middle_Ages=Heart[(Heart['age']>=40) & (Heart['age']<55)]
Senior_Ages=Heart[(Heart['age']>=55)]
print('Young Ages =>',len(Young_Ages))
print('Middle Ages =>',len(Middle_Ages))
print('Senior Ages =>',len(Senior_Ages))


#Bar Plot Creation of Age Category using MatplotLib and Seaborn
plt.figure(figsize = (10,7))
sns.barplot(x = ['Young_Ages','Middle_Ages','Senior_Ages'], y = [len(Young_Ages),len(Middle_Ages),len(Senior_Ages)],palette='deep',data = Heart)
plt.title('Age Category', fontsize=17)
plt.xlabel('Age Range', fontsize=15)
plt.ylabel('Count', fontsize=15)
plt.show()

#Converting Numerical Data into Categorical Data
def Sex1 (row):
    if row == 1:
        return 'Male'
    elif row == 0:
        return 'Female'

    
Heart['Sex1'] = Heart['sex'].apply(Sex1)

Heart.head()

Heart['Sex1'].value_counts()

def age_range (row):
    if row >=29 & row <40:
        return 'Young age'
    if row >=40 & row <55:
        return 'Middle_age'
    if row >55:
        return 'Senior_age'

Heart['Age_range'] = Heart['age'].apply(age_range)

Heart.head()





