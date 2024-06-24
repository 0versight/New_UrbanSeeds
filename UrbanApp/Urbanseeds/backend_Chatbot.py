import os 
from langchain.llms.bedrock import Bedrock
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain

import boto3

# Set environment variable (for this session)
os.environ['AWS_DEFAULT_REGION'] = 'us-east-1'

# Create a Bedrock client
bedrock_client = boto3.client('bedrock', region_name=os.getenv('AWS_DEFAULT_REGION'))

# Perform an action to ensure the client is working
try:
    response = bedrock_client.some_action()  # Replace 'some_action' with a valid method call for the Bedrock service
    print(response)
except Exception as e:
    print(f"Error: {e}")

def demo_chatbot():
    demo_llm = Bedrock(
        credentials_profile_name='AAN',
        model_id='meta.llama2-70b-chat-v1',
        model_kwargs= {
            "temperature": 0.5,
            "top_p": 0.9,
            "max_gen_len": 512})
    return demo_llm

    #return demo_llm.predict(input_text)
    #response =demo_chatbot('hi, what is your name?')
    #print (response)

def demo_memory():
    llm_data=demo_chatbot()
    memory = ConversationBufferMemory(llm=llm_data, max_token_limit= 512)
    return memory

def demo_conversation(input_text,memory):
    llm_chain_data = demo_chatbot()
    llm_conversation= ConversationChain(llm=llm_chain_data, memory= memory, verbose=True)
    
    chat_reply = llm_conversation.predict(input=input_text)
    return chat_reply