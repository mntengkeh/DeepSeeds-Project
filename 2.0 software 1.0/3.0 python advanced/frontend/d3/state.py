import streamlit as st


# no state/session tracking

# count = 0
# if st.button("Incrememt"):
#     count += 1
# st.write(f"Count: {count}")


# if "count" not in st.session_state:
#     st.session_state.count = 0

# if st.button("Incrememt"):
#     st.session_state.count += 1

# if st.button("Decrement"):
#     st.session_state.count -= 1

# st.write(f"Count: {st.session_state.count}")

# xperiment

# import time

# if "page" not in st.session_state:
#     st.session_state.page = "pinfo"
#     st.session_state.info = {}

# def switch_to_pinfo():
#     st.session_state.page = "pinfo"

# def switch_to_confir():
#     st.session_state.page = "confirm"


# with st.sidebar:
#     if st.button("Personal Info"):
#         switch_to_pinfo()
#     if st.button("Confirmation"):
#         switch_to_confir()

# if st.session_state.page == "pinfo":
#     with st.form(key="a"):
#         name = st.text_input("Name:")
#         email = st.text_input("Email:")
#         st.session_state.info["name"] = name
#         st.session_state.info["email"] = email

#         submit = st.form_submit_button("Confirm info")
#         if submit:
#             switch_to_confir()


# elif st.session_state.page == "confirm":
#     st.write(st.session_state.info)
#     opinion = st.checkbox("I confirm this information is correct")

#     if opinion:
#         with st.spinner("Please give us a moment..."):
#             time.sleep(4)
#         st.success("Info confirmed!")



# if "step" not in st.session_state:
#     st.session_state.step = 1
# if "info" not in st.session_state:
#     st.session_state.info = {}

# def go_next(username, email, date_of_birth, more_info):
#     st.session_state.step = 2
#     st.session_state.info["name"] = username
#     st.session_state.info["email"] = email
#     st.session_state.info["dob"] = date_of_birth
#     st.session_state.info["more_info"] = more_info
#     st.write(st.session_state.info)

# if st.session_state.step == 1:
#     st.write("Please enter your information")
#     username = st.text_input("Enter your username", value=st.session_state.info.get("name"))
#     email = st.text_input("enter email", value=st.session_state.info.get("email"))
#     date_of_birth = st.date_input("Enter your date of birth", value=st.session_state.info.get("dob"))
#     more_info = st.text_area("Tell us more about yourself", value=st.session_state.info.get("more_info"))
#     agree_to_terms = st.checkbox("I agree to the terms and conditions")

#     st.button("Next page", on_click=go_next, args=(username, email, date_of_birth, more_info))
            

# elif st.session_state.step == 2:
#     st.header("Review your information")
#     st.write("Please reiew your information")
#     st.write(f"**Username:** {st.session_state.info["name"]}")
#     st.write(f"**Email:** {st.session_state.info["email"]}")
#     st.write(f"**DOB:** {st.session_state.info["dob"]}")
#     st.write(f"**More info:** {st.session_state.info["more_info"]}")

#     confirmation = st.checkbox("I confirm the info")

#     if st.button("Previous"):
#         st.session_state.step = 1




# expensive querry


import time

# def expensive_search(query):
#     time.sleep(2)
#     return f"Results for '{query}"

# query = st.text_input("Search for something")

# if query:
#     st.write(expensive_search(query))


def expensive_search():
    query = st.session_state.query
    with st.spinner("Loading..."):
        time.sleep(2) # simulate heavy work
    st.session_state.results = f"Results for '{query}'"

st.text_input("Search for something", key="query")
st.button("Run Search", on_click=expensive_search)

if "results" in st.session_state:
    st.write(st.session_state.results)



