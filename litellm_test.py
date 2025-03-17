import litellm
import os
from dotenv import load_dotenv

load_dotenv()

response = litellm.completion(
    model=os.getenv("COMPATIE_MODEL"),              
    api_key=os.getenv("COMPATIE_API_KEY"),                  
    api_base=os.getenv("COMPATIE_API_BASE"),     
    messages=[
                {
                    "role": "user",
                    "content": "Hey, how's it going?",
                }
    ],
)
print(response)
