import os
import openai
import streamlit as st
import warnings

openai.organization = "org-eptWwJzwl8LLZVNyAH1xBxbF"
openai.api_key = st.secrets['api_key']



st.title('R <---> Python Re-Writer')


mode = st.selectbox('Mode',['R to Python','Python to R'])


prepend = 'R code in Python'
if mode == 'Python to R':
    prepend = 'Python code in R'

code = st.text_area('Code to rewrite')
response = ''

if st.button('Re-write'):
    response = passions_response = openai.Completion.create(
                          model="text-davinci-003",
                          prompt = 'Rewrite the following ' + prepend + ' with good comments:\n'+code+'\n',
                          temperature = 0.15,
                          top_p = 1,
                          max_tokens = 500
                        )["choices"][0]["text"]
    warnings.warn(str(code) + '\n' + str(response))
st.text(response)


