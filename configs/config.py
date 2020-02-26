class Config(object):
    SQLALCHEMY_TRACK_MODIFICATIONS= False

class Development(Config):
    DEBUG=True
    SQLALCHEMY_DATABASE_URI='postgresql://postgres:Miskitoo.1998@127.0.0.1:5432/sales_demo'
    SECRET_KEY='MISKY'

class Development(Config):
    DEBUG=True
    SQLALCHEMY_DATABASE_URI='postgresql://postgres:Miskitoo.1998@127.0.0.1:5432/sales_demo'
    SECRET_KEY='MISKY'

