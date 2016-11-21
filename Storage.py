import pymongo
import datetime


class Storage:
    def __init__(self, configs):
        db_configs = configs.get_db()

        self.db_name = db_configs['name']
        self.db_connection_string = db_configs['connection_string']
        self.db_url_collection = db_configs['url_collection']

        # connect do DB
        self.connect()


    def connect(self):
        try:
            mongo_client = pymongo.MongoClient(self.db_connection_string)
            self.db = mongo_client[self.db_name]

            print 'Connected to DB'
        except Exception as exc:
            print 'Error connecting to DB: ' + str(exc)


    def save_new_url(self, url, category):
        try:
            self.db[self.db_url_collection].insert({
                'create_on': datetime.datetime.now(),
                'url': url,
                'category': category,
            })
            print 'URL marked as used.'

        except Exception as exc:
            print 'Error saving new url: ' + str(exc)


    def url_already_exists(self, url, category):
        try:
            db_url = self.db[self.db_url_collection].find({
                'url': url,
                'category': category
            })

            return db_url.count() > 0
        except Exception as exc:
            print 'Error check if url already exists: ' + str(exc)

        return False
