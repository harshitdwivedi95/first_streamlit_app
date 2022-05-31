import streamlit

streamlit.title('My parents new healthy dinner')

streamlit.header('Breakfast menu')
streamlit.text('Omega 3 & blueberry oatmeal')
streamlit.text('Kale, Spinach and Rocket Smoothie')
streamlit.text('Hard-Boiled Free-Ranged eggs')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)



streamlit.title("My mom's new healthy dinner")

streamlit.header('Breakfast favorites')
streamlit.text('Omega 3 & blueberry oatmeal')
streamlit.text('Kale, Spinach and Rocket Smoothie')
streamlit.text('Hard-Boiled Free-Ranged eggs')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')                
                
#Let's put a pick list here so they can pick the fruit they want to include  -- SELECTING INDEX NUMBERS
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))

#Let's put a pick list here so they can pick the fruit they want to include  -- SELECTING FRUITS NAME
my_fruit_list = my_fruit_list.set_index('Fruit') 

#Display the table on the page
streamlit.dataframe(my_fruit_list)

