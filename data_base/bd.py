from sqlalchemy import create_engine, inspect
from sqlalchemy.orm import declarative_base, Session


class DataBase:
    DATA_BASE_ADDRESS = 'sqlite:///investments.db'
    Base = declarative_base()
    engine = create_engine(DATA_BASE_ADDRESS)

    def __init__(self):
        self.inspector = inspect(self.engine)
        self.session = Session(self.engine)

        self._create_db()

    def _create_db(self):
        if not self.inspector.get_table_names():
            self.Base.metadata.create_all(self.engine)
            print("Таблицы созданы.")
        else:
            print("Таблицы уже существуют.")

    def drop_tables(self):
        self.Base.metadata.drop_all(self.engine)

        print("Таблицы удалены.")

    def close_db(self):
        self.session.close()
