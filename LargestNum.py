import streamlit as st

st.title("Largest Number")

# Create the first text box
text_1 = st.text_input("Enter first number")

# Create the second text box
text_2 = st.text_input("Enter second number")

# Create the third text box
text_3 = st.text_input("Enter third number")

# Display the contents of the text boxes
st.write("Sun", text_1+text_2+text_3)

