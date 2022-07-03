import constants
from pymongo import MongoClient

client = MongoClient(constants.MONGO_URL)


def persist_to_mongo(items: list, collection_name: str, db_name: str = constants.NEWS_DB):
    """
    Stores the curated news articles into the MongoDB.

    Parameters
    ----------
    items           : The list of news articles to be stored.
    collection_name : Name of the collection to store the articles in.
    db_name         : Name of the MongoDB database to store the articles in.
    """

    db = client[db_name]
    collection = db[collection_name]
    try:
        collection.insert_many(items, ordered=False)
    except Exception as e:
        print("An exception occurred :", e)


def read_from_mongo(collection_name: str, query=None, columns=None, db_name: str = constants.NEWS_DB):
    """
    Retrieves the stored news articles into the MongoDB.

    Parameters
    ----------
    collection_name : Name of the collection to read the articles from.
    query           : Query to filter data while getting data.
    columns         : Columns to return.
    db_name         : Name of the MongoDB database to read the articles from.

    Returns
    -------
    cursor: the cursor to the selected collection.
    """

    db = client[db_name]
    cursor = db[collection_name].find(query, columns)
    return cursor


def drop_from_mongo(collection_name: str, db_name: str = constants.NEWS_DB):
    """
    Drops collection from database in MongoDB.

    Parameters
    ----------
    collection_name : Name of the collection to drop.
    db_name         : Name of the MongoDB database to drop from.
    """

    db = client[db_name]
    db[collection_name].drop()


def remove_from_collection(id_list: list, collection_name: str, db_name: str = constants.NEWS_DB):
    """
    Removes all objects in id_list from the passed collection.

    Parameters
    ----------
    id_list         : List of ids to remove from collection.
    collection_name : Name of the collection to remove from.
    db_name         : Name of the MongoDB database to drop from.
    """

    db = client[db_name]
    db[collection_name].delete_many({"_id": {"$in": id_list}})
