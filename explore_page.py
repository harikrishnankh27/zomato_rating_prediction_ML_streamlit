import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud

import re
def load_data():
    df = pd.read_csv('/home/user/project_web/zomato_project.csv')
    df.drop(['phone'], axis=1, inplace=True)  
    df.duplicated().sum()
    df.drop_duplicates(inplace=True)
    df.dropna(how='any', inplace=True)
    df = df.rename(columns={'approx_cost(for two people)': 'cost', 'listed_in(type)': 'type',
                            'listed_in(city)': 'city'})
    df = df.loc[df.rate != 'NEW']
    df['rate'] = df['rate'].apply(lambda x: x.replace('/5', ''))
    df['rate']=df['rate'].astype(float)

    
    return df

df= load_data()

def show_explore_page():
    st.title("Explore EDA evaluation")
    


    st.write("<h1 style='font-size:36px;'>Most Famous Restaurant In bangalore</h1>", unsafe_allow_html=True)

    plt.figure(figsize=(17, 10))
    chains = df['name'].value_counts()[:20]
    sns.barplot(x=chains, y=chains.index, palette='viridis')
    plt.title("Most famous restaurants chains in Bangalore")
    plt.xlabel("Number of outlets")
    plt.ylabel("Restaurant Chain")
    st.pyplot()
    
    st.write("<h1 style='font-size:36px;'>Whether Restaurants deliver online or Not</h1>", unsafe_allow_html=True)
    plt.figure(figsize=(8, 5))
    sns.countplot(x='online_order', data=df, palette='viridis')
    plt.title('Whether Restaurants deliver online or Not')
    st.pyplot()

    st.write("<h1 style='font-size:36px;'>Most oF People Searched words </h1>", unsafe_allow_html=True)
    h1 = []
    df['dish_liked'].apply(lambda x: h1.extend(x.split("','")))
    h1 = pd.Series(h1)
    h1_str = ""
    for i in h1:
        h1_str += str(i) + " "
    wordcloud = WordCloud(width=1080, height=500, background_color='black', min_font_size=10, max_words=30).generate(h1_str)
    plt.figure(figsize=(8, 8), facecolor=None)
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.tight_layout(pad=0)
    plt.show()
    st.pyplot()

    
    st.write("<h1 style='font-size:36px;'>Percentage of Restaurants according to their ratings</h1>", unsafe_allow_html=True)
    slices = [((df['rate'] >= 1) & (df['rate'] < 2)).sum(),
          ((df['rate'] >= 2) & (df['rate'] < 3)).sum(),
          ((df['rate'] >= 3) & (df['rate'] < 4)).sum(),
          (df['rate'] >= 4).sum()]

    labels = ['1-2', '2-3', '3-4', '4+']  # Labels for the slices

# Define colors using Viridis colormap
    colors = plt.cm.viridis(np.linspace(0, 1, len(slices)))

    plt.pie(slices, labels=labels, autopct='%1.0f%%', pctdistance=.5, labeldistance=1.2, shadow=True, colors=colors)
    fig = plt.gcf()
    plt.title("Percentage of Restaurants according to their ratings")
    fig.set_size_inches(10, 10)
    plt.show()
    st.pyplot()

    st.write("<h1 style='font-size:36px;'>Type of Service</h1>", unsafe_allow_html=True)
    sns.countplot(data=df, x='type', palette='viridis')

    fig = plt.gcf()
    fig.set_size_inches(12,12)
    plt.title('Type of Service')
    st.pyplot()

    
    st.write("<h1 style='font-size:36px;'>Top 30 Favourite Food counts</h1>", unsafe_allow_html=True)
    df.index=range(df.shape[0])
    likes=[]
    for i in range(df.shape[0]):
        array_split=re.split(',',df['dish_liked'][i])
        for item in array_split:
            likes.append(item)
    df.index=range(df.shape[0])

    favourite_food = pd.Series(likes).value_counts()

    sns.set_palette('viridis')

    ax = favourite_food.nlargest(n=20, keep='first').plot(
    kind='bar',
    figsize=(18,10),
    title='Top 30 Favourite Food counts'
    )

    for i in ax.patches:
        ax.annotate(str(i.get_height()), (i.get_x() * 1.005, i.get_height() * 1.005))
        
    st.pyplot()   
    
st.set_option('deprecation.showPyplotGlobalUse', False)

