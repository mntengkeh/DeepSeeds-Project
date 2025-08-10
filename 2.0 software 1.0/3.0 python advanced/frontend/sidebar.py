import streamlit as st

# with st.sidebar:
#     selct = st.selectbox(
#         "Which program will you enroll in?",
#         ("Frontend", "Backend", "Mobile","ML","Cybersecurity")
# )

# with st.sidebar:
#     add_radio = st.radio(
#         "Select gender",
#         ("Male", "Felmale", "Bi", "Other")
#     )


# # import time

# # with st.sidebar:
# #     with st.echo():
#         st.write("This code will be printed to the sidebar.")

#     with st.spinner("Loading..."):
#         time.sleep(5)
#     st.success("Done!")

# st.sidebar.title("Settings")
# temperature = st.sidebar.slider("Creativity", 0.0, 1.0, 0.7)
# modal_choice = st.sidebar.selectbox("Model", ["GPT-4", "Claude", "Gemini"])


# 2 tabs
# separate ocntent into multiple pages without navigationg 

# tab1, tab2, tab3, tab4 = st.tabs(["Prompt", "Output", "About", "Error"])

# with tab1:
#     st.text_area("Enter your prompt")
# with tab2:
#     st.write("Generated result appears here")
# with tab3:
#     st.write("Tab3 active")
# with tab4:
#     st.write("Tab4 active")

# 3 columns
# place elements side by side(e.g, inputs on the left, results on the riht)

# col1, col2 = st.columns(2)
# with col1:
#     st.text_input("Enter prompt")
# with col2:
#     st.write("Ai result goes here")


# 4 container
# group related elements and allow for dynamic updates inside the group

# container = st.container()
# container.write("Generated text area")
# btn = container.button("Generate text")


#5. Expander
# Hide/show details on demand -- useful or advanced settings or explanations

# with st.expander("Advancedd Options"):
#     st.slider("Max lokens", 100, 1000)
#     st.checkbox("Stream Output")

# Empty
# Reserve a space for content that updates later (e.g., dynamic result areas).

placeholder = st.empty()
if st.button("Generate"):
    placeholder.write("Generating...")
    #simulate generation
    placeholder.write("Done! Here's the result")

# combine layouts for a GenAi App