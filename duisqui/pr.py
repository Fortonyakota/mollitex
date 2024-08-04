# config.py
class Config:
    DEBUG = False
    TESTING = False
    SECRET_KEY = 'supersecretkey'
    
class ProductionConfig(Config):
    ENABLE_DEBUG = False
    
class DevelopmentConfig(Config):
    DEBUG = True
    ENABLE_DEBUG = True
    
class TestingConfig(Config):
    TESTING = True
    ENABLE_DEBUG = True
