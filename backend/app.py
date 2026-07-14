from flask import Flask
from flask_cors import CORS

from config import Config

from extensions import (
    db,
    migrate,
    bcrypt,
    jwt,
    cache
)

import models

from routes.auth import auth_bp
from routes.admin import admin_bp
from routes.company import company_bp
from routes.student import student_bp

from seeds.admin_seed import create_default_admin


def create_app():

    app = Flask(__name__)

    app.config.from_object(Config)

    CORS(
        app,
        resources={
            r"/api/*": {
                "origins": "http://localhost:5173"
            }
        }
    )

    # =====================================
    # Initialize Extensions
    # =====================================

    db.init_app(app)

    migrate.init_app(app, db)

    bcrypt.init_app(app)

    jwt.init_app(app)
    
    
    from flask import jsonify

    @jwt.invalid_token_loader
    def invalid_token(reason):
        print("INVALID TOKEN:", reason)
        return jsonify({"message": reason}), 401


    @jwt.unauthorized_loader
    def unauthorized(reason):
        print("UNAUTHORIZED:", reason)
        return jsonify({"message": reason}), 401


    @jwt.expired_token_loader
    def expired_token(jwt_header, jwt_payload):
        print("TOKEN EXPIRED")
        return jsonify({"message": "Token expired"}), 401

    cache.init_app(app)

    # =====================================
    # Register Blueprints
    # =====================================

    app.register_blueprint(auth_bp)

    app.register_blueprint(admin_bp)

    app.register_blueprint(company_bp)

    app.register_blueprint(student_bp)

    # =====================================
    # Create Default Admin
    # =====================================

    with app.app_context():

        db.create_all()

        create_default_admin()
        
        
        
        
    @app.route("/health")
    def health():

        return {
            "status":"running",
            "redis":"connected",
            "celery":"active"
        }

    # =====================================
    # Home Route
    # =====================================

    @app.route("/")
    def index():

        return {
            "status": "success",
            "message": "Placement Portal Backend Running"
        }

    return app


if __name__ == "__main__":

    app = create_app()

    app.run(debug=True)

