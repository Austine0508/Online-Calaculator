import streamlit as st

st.title("ONLINE CALCULATOR")

col1,s1,col2,s2,col3,col4=st.columns([1,0.1,1,0.1,1,1])

if 'result' not in st.session_state:
    st.session_state.result = ''
with col1:
    if (st.button('7')):
        st.session_state.result+="7"
    if (st.button('4')):
        st.session_state.result+="4"
    if (st.button('1')):
        st.session_state.result+="1"
    if (st.button('<--')):
        st.session_state.result=st.session_state.result[:-1]
with col2:
    if (st.button('8')):
        st.session_state.result+="8"
    if (st.button('5')):
        st.session_state.result+="5"
    if (st.button('2')):
        st.session_state.result+="2"
    if (st.button('Clear')):
        st.session_state.result=''
with col3:
    if (st.button('9')):
        st.session_state.result+="9"
    if (st.button('6')):
        st.session_state.result+="6"
    if (st.button('3')):
        st.session_state.result+="3"
    if (st.button('÷')):
        st.session_state.result+="/"
with col4:
    if (st.button('**+**')):
        st.session_state.result+="+"
    if (st.button('**-**')):
        st.session_state.result+="-"
    if (st.button('X')):
        st.session_state.result+="*"
    if (st.button('=')):
        try:
            output=eval(st.session_state.result)
        except:
            output="Error"
        st.text("RESULT: {}".format(output))
st.text(st.session_state.result)
