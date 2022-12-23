import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
pd.plotting.register_matplotlib_converters() #convetr dates in actual dates when we plot it make sence
import seaborn as sns
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
    elif n=='fileineering and Architectural Science':
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
def fac_list(faculties):
    for i in enumerate(faculties):
        print(i)

def run(new_file):
    s = []
    for index, row in new_file.iterrows():
        row['What gender do you identify as?'] = gender_to_value(row['What gender do you identify as?'])
        row['What year are you in?'] = int(year_to_value(str(row['What year are you in?'])))
        if row['What year are you in?'] == 1 and (
                row['TMU Which faculty are you in?'] == 5 or row['TMU Which faculty are you in?'] == 2):
            row['What year are you in?'] = 5
        row['Interesting BDPs'] = row['Interesting BDPs'].split(",")
        s = s + row['Interesting BDPs']
        if row['Favorite BDP']=="No favorite! (I'm equally happy working on any problems I picked earlier)":
            row['Favorite BDP']='No favorite!'
        if row['Biggest reason for joining Zero']=='No favorites, I liked all I picked before equally!':
            row['Biggest reason for joining Zero'] = 'No favorites'
        row['TMU Which faculty are you in?']=faculty_to_value(row['TMU Which faculty are you in?'])
    faculty=new_file['TMU Which faculty are you in?'].value_counts()
    fav_bdp = new_file['Favorite BDP'].value_counts()
    big_reason = new_file['Biggest reason for joining Zero'].value_counts()
    gender = new_file['What gender do you identify as?'].mean()
    self_ident = new_file['Do you self-identify as any of the following?'].value_counts()
    year = new_file['What year are you in?'].mean()
    num_of_participants = new_file['Email'].count()

    values, counts = np.unique(s, return_counts=True)
    # x=values
    # y=counts
    values = values.tolist()
    counts = counts.tolist()
    d = []
    for i in range(0, len(values)):
        t = (values[i], counts[i])
        d.append(t)
    d.sort(key=lambda tup: tup[1], reverse=True)

    print('Faculty:', faculty)
    print(f' Number of participants: {num_of_participants} \n Favourite BDPs: \n {fav_bdp} \n Biggest reason to join Zero: \n {big_reason} \n % of Male participants\n {gender}\n Self-Identity of the participants \n {self_ident}\n  Year of study\n {year}')
    print('Intersting BDPs:')
    for i in d:
        print(i)

    print("\n \n")

    sns.set(style="darkgrid")
    plt.figure(figsize=(16, 6))
    new_file.set_index(keys=new_file.index)

    sns.relplot(data=new_file, x=new_file.index, y='Biggest reason for joining Zero', hue='What year are you in?', style='What gender do you identify as?')
    # plt.show()


    # x=fav_bdp[:5].index #favourite bdp
    # y=fav_bdp[:5]
    # plt.title('Favourite problem')
    # x=big_reason[:5].index
    # y=big_reason[:5]
    # plt.title('Biggest reason to join the program')
    # plt.bar(x, y, color='red')
    # plt.xticks(rotation=9)
    # plt.show()



def merging_frames(s, faculties, file):
    df=pd.DataFrame()
    for i in enumerate(faculties):
        for j in range(0, len(s)):
            if int(s[j])==i[0]:
                df=pd.concat([df, file[file['TMU Which faculty are you in?']==i[1]]])
    return df



file=pd.read_csv('/Users/kirillevseev/Downloads/TMU F22.csv')
file=file[file['Accepted']=='checked']
# file=file[file['What gender do you identify as?']=='Female']
faculties=file['TMU Which faculty are you in?'].unique()
run(file)
# asw=input('do you want to merge faculties?: ')
# if asw=='yes':
#     fac_list(faculties)
#     s=input("enter codes of faculties you are interested in(enter space separated line): ")
#     s=list(s.split(' '))
#     run((merging_frames(s, faculties, file)))
# else:
#     fac_list(faculties)
#     s=input("enter codes of faculties you are interested in(enter space separated line): ")
#     s=s.split(' ')
#     for i in enumerate(faculties):
#         for j in range(0, len(s)):
#             if int(s[j])==i[0]:
#                 run(file[file['TMU Which faculty are you in?']==i[1]])