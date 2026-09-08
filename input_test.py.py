import streamlit as st

st.title("ავტორიზაციისა და რეგისტრაციის სისტემა")

st.write("===WELCOME===")
st.warning("WARNING: This program is for adults only.")
st.write("remember: naoya was right.")
st.write("=================")

st.write("Please fill in the following information:")

user_input = st.text_input("print your name: ")
age = st.number_input("print your age: ", min_value=0, max_value=120, value=18)

if age >= 18:
    st.success("You are an adult. You are eligible.")
    
    if user_input:
        st.write(f"Thank you for using our program! **{user_input}**, you are allowed to sign up for our service.")

    st.markdown("---")
    st.subheader("===REGISTRATION===")
    st.write("Please fill in the following information:")
    reg_username = st.text_input("create username: ")
    reg_password = st.text_input("create password: ", type="password")

    if reg_username and reg_password:
        st.info(f"Registration successful! Your username is: {reg_username}")

        st.markdown("---")
        st.subheader("===LOGIN===")
        login_username = st.text_input("Enter your username: ")
        login_password = st.text_input("Enter your password: ", type="password")

        if st.button("Login"):
            if login_username == reg_username and login_password == reg_password:
                st.balloons()
                st.success(f"Login successful! Welcome, {login_username}!")
            else:
                st.error("Login failed! Invalid username or password.")

else:
    st.error("You are not an adult. You are not eligible.")