import streamlit as st

# Here: TODO
# TO have palm function loaded
# you'll need API key
# palm_api_key = st.secrets["PALM_API_KEY"]
# you'll have to define the function
# def call_palm()
# HERE
# import google.generativeai as palm
# def call_palm(prompt: str, palm_api_key: str) -> str:
#     palm.configure(api_key=palm_api_key)
#     completion = palm.generate_text(
#         model="models/text-bison-001",
#         prompt=prompt,
#         temperature=0,
#         max_output_tokens=800,
#     )
#     return completion.result

st.title("Echo Bot")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# React to user input
if prompt := st.chat_input("What is up?"):
    # Display user message in chat message container
    st.chat_message("user").markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    # TODO
    # You have to update the following line of code
    # to add the function that you want. Say you want to add 
    # call_palm() function. Then you need to define in the script
    # and call it here. 
    # You'll have response = call_palm(f"{prompt}")
    response = f"Echo: {prompt}"
    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        st.markdown(response)
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})
