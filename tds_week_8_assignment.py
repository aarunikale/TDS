import streamlit as st

st.title('Calculate the largest Number amongst the three!')

st.header('_Enter your numbers here:_ ')

number1 = st.number_input('Insert first number')
number2 = st.number_input('Insert second number')
number3 = st.number_input('Insert third number')

def maximum():
    lis = [number1 , number2 , number3]
    a = max(lis)
    st.success(f"Maximum = {a}")

if st.button("Calculate result"):
    maximum()
