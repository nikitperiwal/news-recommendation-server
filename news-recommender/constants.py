from secret_keys import mongo_username, mongo_password

# MongoDB Constants
MONGO_URL = f"mongodb+srv://{mongo_username}:{mongo_password}@shortly.autde.mongodb.net/?retryWrites=true&w=majority"
NEWS_DB = "news_db"

CURATED_TABLE = "curated_news"
PROCESSED_TABLE = "processed_news"
