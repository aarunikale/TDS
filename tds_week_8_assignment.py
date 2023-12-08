import streamlit as st

st.title('Calculate the largest Number amongst the three!')

st.header('_Enter your numbers here:_ ')

number1 = st.number_input('First Number')
number2 = st.number_input('Second Number')
number3 = st.number_input('Third Number')

def maximum():
    lis = [number1 , number2 , number3]
    a = max(lis)
    st.success(f"Maximum = {a}")

if st.button("Calculate"):
    maximum()
