import streamlit as st

st.title('Semantic Similarity')
sentences1 = st.text_input('Insert sentences1:')
sentences2 = st.text_input('Insert sentences2:')

if st.button('Submit'):
    st.write('Sentences1 is:', sentences1)
    st.write('Sentences2 is:', sentences2)
