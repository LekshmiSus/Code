import streamlit as st

st.title("Find the Largest Number")

# Input three numbers
num_1 = st.number_input("Enter the first number")
num_2 = st.number_input("Enter the second number")
num_3 = st.number_input("Enter the third number")

# Find the largest number
largest = max(num_1, num_2, num_3)

# Display the result
st.write("The largest number is:", largest)
