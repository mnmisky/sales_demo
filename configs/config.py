class Config(object):
    SQLALCHEMY_TRACK_MODIFICATIONS= False

class Development(Config):
    DEBUG=True
    # SQLALCHEMY_DATABASE_URI='postgresql://postgres:Miskitoo.1998@127.0.0.1:5432/sales_demo'
    SQLALCHEMY_DATABASE_URI='postgres://gygwqrdwerdekx:3b24d6681e35a1c68211f7026e627708f43e92cb06f914303865b1636d4db1f7@ec2-18-210-51-239.compute-1.amazonaws.com:5432/de723tjimc0c7b'
    SECRET_KEY='MISKY'

class Production (Config):
    DEBUG=True
    SQLALCHEMY_DATABASE_URI='postgres://ccvbizveqagakt:24bc8be95dec135f012d2b6db50df39ef522eee8ee10338e8dcedb40090c8b0d@ec2-35-171-31-33.compute-1.amazonaws.com:5432/d92mal5kb87d46'
    SECRET_KEY='MISKY'

