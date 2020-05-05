import os

from config import Config
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class DB:

    def __init__(self):
        self.session = None

    def get_session(self):
        if not self.session:
            query_debug = False if os.environ.get('ENV') in ['prod', 'stage'] else True

            engine = create_engine(Config.SQLALCHEMY_DATABASE_URI, echo=query_debug)

            Session = sessionmaker(bind=engine)
            self.session = Session()

        return self.session

    def commit(self):
        self.get_session().commit()

    def rollback(self):
        self.get_session().rollback()

    def select(self, query, args=None):
        return self.get_session().execute(query, args).fetchall()

    def execute(self, query, args=None):
        return self.get_session().execute(query, args)

    def add(self, obj):
        self.get_session().add(obj)

    def add_image_record(self, image_id: str, name: str, image_url: str):
        query_string = f"""
            INSERT INTO image (id, name, image_url)
            VALUES(:id, :name, :image_url)
        """

        query_args = {"id": image_id, "name": name, "image_url": image_url}

        self.execute(query_string, query_args)
        self.commit()

    def get_image_record(self, image_id: str):
        query_string = f"""
            SELECT i.name, i.image_url
            FROM image AS i
            WHERE i.id = :image_id
        """

        query_args = {"image_id": image_id}

        image_row = self.select(query_string, query_args)[0]

        return image_row


db = DB()
