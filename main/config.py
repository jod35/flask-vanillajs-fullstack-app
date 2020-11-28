import os

BASE_DIR=os.path.dirname(os.path.realpath(__file__))


class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    SECRET_KEY='508302f8e29fdbd7076d'
    SQLALCHEMY_DATABASE_URI='sqlite:///'+os.path.join(BASE_DIR,'site.db')
