import streamlit as st

def validate_input():
    with st.form(key="my_key", clear_on_submit=True):
        user_name = st.text_input(label="Username")
        email = st.text_input(label="Email")
        about = st.text_input(label="Mind talking about yourself?")
        prompt = st.text_area(label="Ask AI anything", help="Like anything anything!", value="some value", label_visibility="visible")

        submit = st.form_submit_button("Sumit Data")

        if submit:
            if user_name and email and about and prompt:
                st.write("Thank you for submitting")
                values = {
                    "Name": user_name,
                    "Email": email,
                    "About": about,
                    "Prompt": prompt
                }
                user_name = ""
                email = ""
                about = ""
                prompt = ""
                return values
            else:
                st.write("Please fill all the forms")
    


result = validate_input()
if result:
    st.write(result)
    print(result)