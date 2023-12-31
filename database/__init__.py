from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URI = 'sqlite:///pay_test.db'
# connect_args={'check_same_thread': False} - только для sqlite3
engine = create_engine(SQLALCHEMY_DATABASE_URI, connect_args={'check_same_thread': False})

# Сессии для базы данных
SessionLocal = sessionmaker(bind=engine)

#  общий класс для создания моделей данных
Base = declarative_base()

# Генерация подключений к базе
def get_db():
    session = SessionLocal()
    try:
        yield session
    except:
        session.rollback()
        raise
    finally:
        session.close()



# Импорт функционала для ДБ
from database.userservice import *
from database.cardservice import *
from database.businesservice import *
from database.paymentservice import *