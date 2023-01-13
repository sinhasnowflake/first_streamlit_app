import streamlit
import pandas
streamlit.title('My parents healthy diner');
streamlit.header('Breakfast Menu');
fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)
streamlit.text('almond flour pancake');
streamlit.text('almond flour waffle with kale and almond');
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")



streamlit.dataframe(my_fruit_list)



