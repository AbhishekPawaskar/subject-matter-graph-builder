import os
from openai import OpenAI

#Singleton class implementation
class OpenAIConnection:
    """
    How to use:

    assistant = OpenAIConnection()

    assistant.client.beta.assistant.create(name="Content Compliance Checker",
                                            instructions=detailed_instruction,
                                            model="gpt-4-1106-preview")

    to close connection,
    
    assitant.client.close()

    """
    _instance = None
    
    def __init__(self):
        self.client = establish_remote_connection()
        
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(OpenAIConnection, cls).__new__(cls) 
            cls._instance.__init__()
        else:
            if cls._instance.client is None or cls._instance.client.is_closed(): 
                cls._instance.client = establish_remote_connection()
                
        return cls._instance
    

def establish_remote_connection():
    client = OpenAI(api_key=os.environ.get('OPEN_AI_API_KEY'))
    return client