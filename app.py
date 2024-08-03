import streamlit as st
import pickle
import requests
import webbrowser

# Load the data
movies = pickle.load(open('movies.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

# CSS for background image
page_bg_img = """
<style>
[data-testid="stAppViewContainer"] > .main {
    background-image: url("https://qph.cf2.quoracdn.net/main-qimg-e38b8ceaa9ee71fd2b435681135e7da6-lq");
    background-size: 100vw 100vh;  # This sets the size to cover 100% of the viewport width and height
    background-position: center;  
    background-repeat: no-repeat;
}
</style>
"""

# Apply background image
st.markdown(page_bg_img, unsafe_allow_html=True)


# Recommendation function
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommend_movies = []
    for i in movies_list:
        recommend_movies.append(movies.iloc[i[0]].title)
    return recommend_movies


# Title of the app
st.title('Movie Recommender System')

# Dropdown for movie selection
mov = movies['title'].values
option = st.selectbox("Select a movie to get recommendations:", mov)

# Recommend button
if st.button('Recommend'):
    names = recommend(option)

    # Display recommendations in columns
    col1, col2, col3, col4, col5 = st.columns(5)
    columns = [col1, col2, col3, col4, col5]

    for idx, col in enumerate(columns):
        with col:
            st.header(names[idx])
            new=2
            s=names[idx].replace(" ","")

            tab_url = f"https://en.wikipedia.org/wiki/{s}_(film)"
            st.write(tab_url,new=new)
