import streamlit as st
from langchain.chat_models import ChatOpenAI
from langchain import PromptTemplate

st.set_page_config(page_title="🦜🔗 Blog Outline Generator App")
st.title('🦜🔗 Blog Outline Generator App')
openai_api_key = st.sidebar.text_input('OpenAI API Key', type='password')

def generate_response(topic):
    llm = ChatOpenAI(model_name='gpt-4', openai_api_key=openai_api_key)
    # Prompt
    template = '経験豊富なデータサイエンティストであり、技術ライターとして、{topic}についてのブログの概要を作成してください。'
    prompt = PromptTemplate(input_variables=['topic'], template=template)
    prompt_query = prompt.format(topic=topic)
    # Run LLM model and print out response
    response = llm(prompt_query)
    return st.info(response)

with st.form('myform'):
    topic_text = st.text_input('Enter keyword:', '')
    submitted = st.form_submit_button('Submit')
    if not openai_api_key.startswith('sk-'):
        st.warning('Please enter your OpenAI API key!', icon='⚠')
    if submitted and openai_api_key.startswith('sk-'):
        generate_response(topic_text)

