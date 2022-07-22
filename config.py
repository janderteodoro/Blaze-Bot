import os 
from dotenv import load_dotenv

load_dotenv()

config = {
    'TOKEN': os.environ.get('TOKEN')
}