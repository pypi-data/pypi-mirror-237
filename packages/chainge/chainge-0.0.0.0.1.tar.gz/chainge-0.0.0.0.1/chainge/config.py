import os
from dotenv import load_dotenv

#Retrieve the API key for the Chainge API 
load_dotenv()

CHAINGE_API_KEY = os.getenv("CHAINGE_API_KEY")

#API Related Constants 
VERSION = "v1"
CHAINGE_API_ENDPOINT = f"https://finchain.p.rapidapi.com/api/{VERSION}"