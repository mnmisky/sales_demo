class Config(object):
    SQLALCHEMY_TRACK_MODIFICATIONS= False

class Development(Config):
    DEBUG=True
      SQLALCHEMY_DATABASE_URI='postgresql://postgres:Miskitoo.1998@127.0.0.1:5432/sales_demo'
    # SQLALCHEMY_DATABASE_URI='postgres://gygwqrdwerdekx:3b24d6681e35a1c68211f7026e627708f43e92cb06f914303865b1636d4db1f7@ec2-18-210-51-239.compute-1.amazonaws.com:5432/de723tjimc0c7b'
    SECRET_KEY='MISKY'

class Production (Config):
    DEBUG=True
    SQLALCHEMY_DATABASE_URI='postgres://gygwqrdwerdekx:3b24d6681e35a1c68211f7026e627708f43e92cb06f914303865b1636d4db1f7@ec2-18-210-51-239.compute-1.amazonaws.com:5432/de723tjimc0c7b'
    SECRET_KEY='MISKY'

