import streamlit as st


st.title('OLOPSC CHATBOT!')

prompt=st.chat_input("Enter something: ")

st.write('# Hi, I am Olive, the OLOPSC Chat support! How can I help you?')

if "messages" not in st.session_state:
	st.session_state.messages = []

for message in st.session_state.messages:
	user_input = st.chat_message(message['role'])
	user_input.write(message['content'])

st.chat_message("user").write(prompt)

if prompt and prompt != '':

	st.session_state.messages.append({'role': 'user', 'content': prompt})

if prompt == 'hi':
	st.chat_message("assistant").write('How are you?')
	st.session_state.messages.append('hello, how are you?')

elif prompt == 'who are you?':
	st.chat_message("assistant").write('I am Olive, your assistant.')
	st.session_state.messages.append({'role':'assistant', 'content': "I am Olive, your assistant."})
elif prompt== 'i would like to make an account':
	st.chat_message("assistant").write('I cannot do that as of right now. Please wait for further updates on me!')
	st.session_state.messages.append({'role':'assistant', 'content': "I cannot do that as of right now. Please wait for further updates on me!"})

