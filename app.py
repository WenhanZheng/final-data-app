import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
import numpy as np
plt.style.use('seaborn')
st.title('Steam games Data by Vanessa & Amanda')

st.subheader('See more filters in the sidebar:')

df = pd.read_csv('year_rank.csv')

del df['ReleaseDate']
del df['ReleaseDate.1']

year = st.sidebar.radio(
    "Choose publish year of games",
    ('2012','2013','2007','2011','2015','2009','2004','1998','2010','2016','2006','2000','2008','2014','2005','2001','2003','1999','1997','2017'))

if year == '2012':
    df = df[0:1]
elif year == '2013':
    df = df[1:2]
elif year == '2007':
    df = df[2:3]
elif year == '2011':
    df = df[3:4]
elif year == '2015':
    df = df[4:5]
elif year == '2009':
    df = df[5:6]
elif year == '2004':
    df = df[6:7]
elif year == '1998':
    df = df[7:8]
elif year == '2010':
    df = df[8:9]
elif year == '2016':
    df = df[9:10]
elif year == '2006':
    df = df[10:11]
elif year == '2000':
    df = df[11:12]
elif year == '2008':
    df = df[12:13]
elif year == '2014':
    df = df[13:14]
elif year == '2005':
    df = df[14:15]
elif year == '2001':
    df = df[15:16]
elif year == '2003':
    df = df[16:17]
elif year == '1999':
    df = df[17:18]
elif year == '1997':
    df = df[18:19]
elif year == '2017':
    df = df[19:20]

fig, ax = plt.subplots()
df.sum().plot(kind='bar')
plt.ylabel('count')
plt.xlabel('Game_genre')
st.pyplot(fig)
st.title('Feature Selection')
dc=pd.read_csv('year_rank.csv')
#list1=list(dc.keys().unique())
#feature_list=np.array(list1[1:14])
#year = [1998,2000,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016]
list1=list(dc.keys().unique())
feature_list=list1[1:]
count1 = [5,155	,175,	98,	45,	76,	61,	33,	1	,27,	9,	13,	20,	2012,	318]
count2=[6	,224	,227	,143	,58	,102	,83	,73	,17	,27	,17	,19	,15	,2013,	421]
count3=[0,	8	,56	,9	,9,	21,	9,	1,	0,	1	,0	,3	,0	,2007,	91]
#count=dc.loc[3]
count=dc.loc[3]
count4=count.tolist()[1:]
count=dc.loc[4]
count5=count.tolist()[1:]
count=dc.loc[5]
count6=count.tolist()[1:]
count=dc.loc[6]
count7=count.tolist()[1:]
count=dc.loc[7]
count8=count.tolist()[1:]
count=dc.loc[8]
count9=count.tolist()[1:]
count=dc.loc[9]
count10=count.tolist()[1:]
count=dc.loc[10]
count11=count.tolist()[1:]
count=dc.loc[11]
count12=count.tolist()[1:]
count=dc.loc[12]
count13=count.tolist()[1:]
count=dc.loc[13]
count14=count.tolist()[1:]
count=dc.loc[14]
count15=count.tolist()[1:]
count=dc.loc[15]
count16=count.tolist()[1:]
count=dc.loc[16]
count17=count.tolist()[1:]
count=dc.loc[17]
count18=count.tolist()[1:]
count=dc.loc[18]
count19=count.tolist()[1:]
count=dc.loc[19]
count20=count.tolist()[1:]
c={"feature": feature_list,"2012": count1,"2013":count2,"2007":count3,"2011":count4,"2015":count5,"2009":count6,"2004":count7,"1998":count8,"2010":count9,"2016":count10,"2006":count11,"2000":count12,"2008":count13,"2014":count14,"2005":count15,"2001":count16,"2003":count17,"1999":count18,"1997":count19,"2017":count20}
df1 = pd.DataFrame(c)
feature_filter=st.sidebar.multiselect('fearture selection',df1.feature.unique(),['GenreIsNonGame_count'])
df1=df1[df1.feature.isin(feature_filter)]
a=df1.iloc[0,1:]
#dc=dc.isin(feature_filter)
plt.rcParams['figure.figsize'] = (20.0, 8.0)
fig = plt.figure()
ax = fig.add_subplot(111)
#ax.set_ylim([0,25])
plt.xticks(list(dc.ReleaseDate))
#plt.figure(figsize=(20,50))
#ax.bar(list(dc.ReleaseDate),count1, alpha=0.7, color='Gray')
ax.set_ylabel(u'Number of games', fontsize='20')
ax.set_xlabel(u'Year', fontsize='20')
ax.tick_params(labelsize=15)
a.plot.bar(ax=ax)
st.pyplot(fig)