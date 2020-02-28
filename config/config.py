import os


class BaseConfig:
    """
    配置基类，用于存放共用的配置
    """
    SECRET_KEY = os.environ.get('SECRET_KEY') or os.urandom(16)
    DEBUG = False
    TESTING = False


class ProductionConfig(BaseConfig):
    """
    生产环境配置类，用于存放生产环境的配置
    """
    pass


class DevelopmentConfig(BaseConfig):
    """
    开发环境配置类，用于存放开发环境的配置
    """
    DEBUG = True


class TestingConfig(BaseConfig):
    """
    测试环境配置类，用于存放开发环境的配置
    """
    DEBUG = True
    TESTING = True


registered_app = [
    'app'
]

config_map = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig
}
