import streamlit as st

st.title("Find the Largest Number")

# Input three numbers
num1 = st.number_input("Enter the 1st number")
num2 = st.number_input("Enter the 2nd number")
num3 = st.number_input("Enter the 3rd number")

# Find the largest number
largest = max(num1, num2, num3)

# Display the result
st.write("The largest number is:", largest)
