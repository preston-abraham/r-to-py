import os
import openai
import streamlit as st
import warnings

openai.organization = "org-eptWwJzwl8LLZVNyAH1xBxbF"
openai.api_key = st.secrets['api_key']


st.title('R to Pyhton Re-writer')

code = st.text_area('Code to rewrite')
response = ''

if st.button('Re-write'):
    response = passions_response = openai.Completion.create(
                          model="text-davinci-003",
                          prompt = 'Rewrite the following R code in Python with good comments:\n'+code+'\n',
                          temperature = 0.15,
                          top_p = 1,
                          max_tokens = 500
                        )["choices"][0]["text"]
st.text(response)
