import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(layout="wide")
st.title("Analyse des prix des logements en Californie")


@st.cache_data
def load_data():
    url = "https://raw.githubusercontent.com/ageron/handson-ml/master/datasets/housing/housing.csv"
    return pd.read_csv(url)

df = load_data()

st.header("Aperçu des données")
st.dataframe(df.head())

st.header("Statistiques descriptives")
st.write(df.describe())

st.header("Distribution des prix des logements")
fig1, ax1 = plt.subplots()
sns.histplot(df['median_house_value'], bins=50, kde=False, ax=ax1)
st.pyplot(fig1)

st.header("Corrélations avec le prix")
fig2, ax2 = plt.subplots(figsize=(10, 8))
numeric_df = df.select_dtypes(include=['number'])  
sns.heatmap(numeric_df.corr(), annot=True, cmap='coolwarm', ax=ax2)
st.pyplot(fig2)

st.header("Prix selon la proximité à l’océan")
fig3, ax3 = plt.subplots()
sns.boxplot(x='ocean_proximity', y='median_house_value', data=df, ax=ax3)
plt.xticks(rotation=45)
st.pyplot(fig3)

st.header("Carte géographique des maisons")
st.map(df[['latitude', 'longitude']])


