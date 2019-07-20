import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'ecommercecentratenunpringgasela'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'mysql+pymysql://root:@localhost/db_pringgos'
    SQLALCHEMY_TRACK_MODIFICATION = False