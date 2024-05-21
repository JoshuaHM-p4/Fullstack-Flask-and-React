import os

class Config:
    """
    Configuration class for the application.
    """
    SQLALCHEMY_DATABASE_URI = 'sqlite:///friends.db' or os.environ.get('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_TRAK_MODIFICATIONS = False
