import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
pd.plotting.register_matplotlib_converters() #convetr dates in actual dates when we plot it make sence
def year_to_value(n):
    if n=='Masters':
       y=5
    elif n=="PhD":
        y=6
    elif n=="nan":
        y=0
    else:
        y=n[0]
    return y

def gender_to_value(n):
    if n=='Male':
        s=1 #Male=1, Female=0
    else:
        s=0
    return s

def accepted_to_value(n):
    if n=='checked':
        s=1
    else:
        s=0
    return s
def part_of_IBZ_to_value(n):
    if n=='Yes':
        s=1
    else:
        s=0
    return s
def faculty_to_value(n):
    if n=='Ted Rogers School of Management':
        s=1
    elif n=='Engineering and Architectural Science':
        s=2
    elif n=='Community Services' :
        s=3
    elif n=='The Creative School':
        s=4
    elif n=='Yeates School of Graduate Studies':
        s=5
    elif n=='Science':
        s=6
    else:
        s=0
    return s
def len_of_text(n):
    return len(n)


file=pd.read_csv('/Users/kirillevseev/Downloads/TMU F22.csv')
#print(file.dtypes)
new_table=file[['Email','First Name','Last Name','What gender do you identify as?', 'Accepted','What year are you in?', 'Would you like to be part of the IBZ Community?', 'TMU Which faculty are you in?', 'Interesting BDPs', 'Favorite BDP']].copy()
file.sort_values(by='Accepted', ascending=True)
n=input('faculty')
eng=file[file['TMU Which faculty are you in?']=='Ted Rogers School of Management']
eng=eng.iloc[17:]
s=[]
for index, row in eng.iterrows():
    row['What gender do you identify as?']=gender_to_value(row['What gender do you identify as?'])
    row['What year are you in?'] = int(year_to_value(str(row['What year are you in?'])))
    if row['What year are you in?'] == 1 and (row['TMU Which faculty are you in?'] == 5 or row['TMU Which faculty are you in?'] == 2):
        row['What year are you in?']=5
    row['Interesting BDPs'] = row['Interesting BDPs'].split(",")
    s=s+row['Interesting BDPs']

fav_bdp=eng['Favorite BDP'].value_counts()
big_reason=eng['Biggest reason for joining Zero'].value_counts()
gender=eng['What gender do you identify as?'].mean()
self_ident=eng['Do you self-identify as any of the following?'].value_counts()
year=eng['What year are you in?'].mean()

print(f'Favourite BDPs: \n {fav_bdp} \n Biggest reason to join Zero: \n {big_reason} \n % of Male participants\n {gender}\n Self-Identity of the participants \n {self_ident}\n  Year of study\n {year}')


values, counts=np.unique(s, return_counts=True)
values=values.tolist()
counts=counts.tolist()

for i in range(0, len(values)):
    print(values[i], counts[i])

# fav_bdp.plot(kind='bar')
# # plt.show()
# new_table=new_table.reset_index()
# #print(new_table.loc[ :, ['Email','What year are you in?', 'Accepted']])
# new_table.sort_values(by='Accepted', ascending=True)
# s=[]
# k=[]
# q=[]
# for index, row in new_table.iterrows():
#     #row['What gender do you identify as?']=gender_to_value(row['What gender do you identify as?'])
#     row['Accepted']=accepted_to_value(row['Accepted'])
#     row['What year are you in?']=int(year_to_value(str(row['What year are you in?'])))
#     row['Would you like to be part of the IBZ Community?']=part_of_IBZ_to_value(row['Would you like to be part of the IBZ Community?'])
#     row['TMU Which faculty are you in?']=faculty_to_value(row['TMU Which faculty are you in?'])
#     row['Interesting BDPs']=row['Interesting BDPs'].split(",")
#     n=row['Interesting BDPs']
#     s=s+n
#     if row['TMU Which faculty are you in?']==6:
#         q+=n
#     row['Favorite BDP'] = row['Favorite BDP'].split(',')
#     k+=row['Favorite BDP']
#     if row['What year are you in?']==1 and (row['TMU Which faculty are you in?']==5 or row['TMU Which faculty are you in?']==2):
#             row['What year are you in?']=5
# A_table=pd.DataFrame()
# A_table=new_table.iloc[18:]
#
# #male_percentage=new_table['What gender do you identify as?'].mean()
#
# #avg_year=new_table['What year are you in?'].mean()
#
# mode_year=new_table['What year are you in?'].mode()[0]
#
# faculty_members=new_table.groupby('TMU Which faculty are you in?')['TMU Which faculty are you in?'].count()
#
# #ac_gender=A_table['What gender do you identify as?'].mean()
#
# ac_year=A_table['What year are you in?'].mean()
#
# ac_mode_year=A_table['What year are you in?'].mode()[0]
#
# ac_count_year=A_table.groupby('What year are you in?')['What year are you in?'].count()
#
# IBZ=A_table['Would you like to be part of the IBZ Community?'].mean()
#
# ac_faculty_members=A_table.groupby('TMU Which faculty are you in?')['TMU Which faculty are you in?'].count()
#
# ac_faculty_members1=A_table['TMU Which faculty are you in?'].value_counts()
# #BDPs=['Environmental Emergencies', 'Access to Basic Necessities', 'Future Cities', 'Personal Health', 'Space Technology', 'Infection Control', 'Connecting with History', 'Youth Education', 'Better Food']
# int_bdp=A_table['Interesting BDPs'].value_counts()
# fav_bdps=A_table['Favorite BDP'].value_counts()
# #
# # values3, counts3=np.unique(q, return_counts=True)
# # values3=values3.tolist()
# # counts3=counts3.tolist()
# #
# values1, counts1=np.unique(s, return_counts=True)
# values1=values1.tolist()
# counts1=counts1.tolist()
# #
# for i in range(0, 9):
#     print(values1[i], counts1[i])
# values2, counts2=np.unique(k, return_counts=True)
# values2=values2.tolist()
# counts2=counts2.tolist()






#print('Percentage of the Male participants:', ac_gender*100,"%")
#print('Mode year of studies of the participants:', mode_year)
#print('Deviation of years of studies of the participants: \n', ac_count_year)
#print('Willingness to be a part of IBZ:', IBZ*100, "%")
#print('Faculty statistics:', ac_faculty_members)
#for i in range(0, 9):
    #print(values[i], counts[i])
#for i in range(0, 11):
   # print(i, values3[i], counts3[i])
   # print(i, values1[i], counts1[i])