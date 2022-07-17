import os
from dotenv import load_dotenv

load_dotenv()

mongo_username = os.environ["MONGO_USERNAME"]
mongo_password = os.environ["MONGO_PASSWORD"]
TEST_MODE = os.environ["TEST_MODE"]

NEWS_CATEGORIES = ['BUSINESS', 'DINING', 'ENTERTAINMENT', 'FASHION', 'PARENTING', 'POLITICS',
                   'SPORTS', 'TRAVEL', 'HEALTH', 'WORLD']

# MongoDB Constants
MONGO_URL = f"mongodb+srv://{mongo_username}:{mongo_password}@shortly.autde.mongodb.net/?retryWrites=true&w=majority"
NEWS_DB = "news_db"

CURATED_TABLE = "curated_news"
PROCESSED_TABLE = "processed_news"
