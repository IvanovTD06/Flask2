class Config:
    TESTING = True

class ProductionCongfig(Config):
    DEBUG = False
    SERVER_NAME = "0.0.0.0.8888"

class DevelopmentConfig(Config):
    DEBUG = True
    PORT = 3333