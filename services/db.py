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

    def get_company_record_for_id(self, id: str):
        query_string = f"""
            SELECT c.mailchimp_api_key, c.ometria_api_key, c.mailchimp_members_list_id, c.last_import_date
            FROM company AS c
            WHERE c.id = :id
        """

        query_args = {"id": id}

        company_row = self.select(query_string, query_args)[0]

        return company_row


db = DB()
