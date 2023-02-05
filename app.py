import streamlit as st
from translate import translate, meanings


st.set_page_config("Mivetran Dictionary", "📘", "wide")

english_txt = st.text_input("Text")


if (english_txt):
    result = translate(english_txt)

    if type(result) == str:
        st.text(result)
        st.info("Noun: "+meanings(result).Noun())
        st.info("Verb: "+meanings(result).Verb())
        st.info("Ajective: "+meanings(result).Adjective())
    elif type(result) == list:
        col1, col2, col3, col4, col5 = st.columns(5)
        with col1:
            button = st.button(result[0])
            if button:
                st.text(translate(result[0]))
                st.info("Noun: "+meanings(result[0]).Noun())
                st.info("Verb: "+meanings(result[0]).Verb())
                st.info("Ajective: "+meanings(result[0]).Adjective())
        with col2:
            if len(result) > 2:
                button = st.button(result[1])
                if button:
                    st.text(translate(result[1]))
                    st.info("Noun: "+meanings(result[1]).Noun())
                    st.info("Verb: "+meanings(result[1]).Verb())
                    st.info("Ajective: "+meanings(result[1]).Adjective())
        with col3:
            if len(result) > 3:
                button = st.button(result[2])
                if button:
                    st.text(translate(result[2]))
                    st.info("Noun: "+meanings(result[2]).Noun())
                    st.info("Verb: "+meanings(result[2]).Verb())
                    st.info("Ajective: "+meanings(result[2]).Adjective())
        with col4:
            if len(result) > 4:
                button = st.button(result[3])
                if button:
                    st.text(translate(result[3]))
                    st.info("Noun: "+meanings(result[3]).Noun())
                    st.info("Verb: "+meanings(result[3]).Verb())
                    st.info("Ajective: "+meanings(result[3]).Adjective())
        with col5:
            if len(result) > 5:
                button = st.button(result[4])
                if button:
                    st.text(translate(result[4]))
                    st.info("Noun:"+meanings(result[4]).Noun())
                    st.info("Verb: "+meanings(result[4]).Verb())
                    st.info("Ajective: "+meanings(result[4]).Adjective())
