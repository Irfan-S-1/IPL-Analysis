

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
%matplotlib inline

df=pd.read_csv("D:\\Data Science\\Practice\\IPL\\matches.csv")
df.shape
df.head()
df.tail()
df.isnull().sum()

#dropping columns with null values#
df=df.drop(["umpire3"],axis=1)


#corelation#
corelation=df.corr()
sns.heatmap(corelation,xticklabels=corelation.columns,yticklabels=corelation.columns,annot=True)

#No of matches played in stadium#
sns.set_style("darkgrid")
ls=df["venue"].value_counts().sort_values(ascending=False)
temp=sns.barplot(ls.index,ls.values,alpha=0.8)
plt.title("Most Played Venues")
plt.xlabel("Count")
plt.ylabel("Name of Stadium")
temp.set_xticklabels(rotation=90,labels=ls.index,fontsize=10)
plt.show()

#most umpired#
temp=pd.concat([df["umpire1"],df["umpire2"]]).value_counts().sort_values(ascending=False)
most_umpired=sns.barplot(temp.index,temp.values,alpha=0.9)
plt.figure(figsize=(20,5))
plt.title("Most Umpired")
plt.xlabel("Name of Umpires",fontsize=20)
plt.ylabel("Count",fontsize=15)
most_umpired.set_xticklabels(rotation=90,labels=temp.index,fontsize=15)
plt.show()

#Delhi Stadium winning percnetage#
Delhi_stadium=df.loc[(df["venue"]=="Feroz Shah Kotla")]
Delhi_stadium_win=Delhi_stadium[Delhi_stadium["win_by_runs"]>0]
slices=[len(Delhi_stadium_win),len(Delhi_stadium)-len(Delhi_stadium_win)]
labels=["Batting first","Batting second"]
plt.pie(slices,labels=labels,startangle=90,explode=(0,0.2),shadow=2,colors=['#1519ef','#fc4811'])
plt.show()


#Kolkata Stadium winning percnetage#
Kolkata_stadium=df.loc[(df["venue"]=="Eden Gardens")]
Kolkata_win_stadium=Kolkata_stadium[Kolkata_stadium["win_by_runs"]>0]
slices=[len(Kolkata_win_stadium),len(Kolkata_stadium)-len(Kolkata_win_stadium)]
labels=["Batting first","Batting second"]
plt.title("Eden Gardens Stats")
plt.pie(slices,labels=labels,startangle=130,explode=(0,0.5),shadow=2,autopct='%1.1f%%',colors=['#1519ef','#fc4811'])
plt.show()


toss=df.groupby(["Season","toss_winner"]).winner.value_counts().reset_index(name = 'count')
toss["result"]=np.where(toss.toss_winner==toss.winner,"win","lost")
toss_result=toss.groupby(["Season","toss_winner","result"])["count"].sum().reset_index()




for x in range(2008, 2018, 1):
    toss_result_x = toss_result[toss_result['Season'] ==x]
    plot = sns.barplot(x="toss_winner", y="count", hue="result", data=toss_result)
    plot.set_title('Matches won/lost by teams winning toss \nSeason ' +str(x))
    plot.set_xticklabels(toss_result['toss_winner'],rotation=30)
    plt.show()
    x+=1