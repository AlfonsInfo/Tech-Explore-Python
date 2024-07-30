from flask import Flask
# from eureka_client import EurekaClient
from config import Config


def create_app():
    app = Flask(__name__)
    # eureka_client = EurekaClient(
    #     eureka_server=Config.EUREKA_SERVER,
    #     app_name=Config.APP_NAME,
    #     instance_port=Config.INSTANCE_PORT,
    #     instance_ip=Config.INSTANCE_IP,
    #     instance_host_name=Config.INSTANCE_HOST_NAME
    # )
    # app.config.from_object(Config)
    from app.routes import main
    app.register_blueprint(main)
    return app
