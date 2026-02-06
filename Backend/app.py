import os

from flask import Flask, jsonify
from flask_jwt_extended import JWTManager
from dotenv import load_dotenv

from config import Config
from db.mongo import client, db

from routes import (
    auth_bp,
    ngo_bp,
    shelter_bp,
    public_bp,
    emergency_bp,
)

from middleware.error_handler import register_error_handlers


# ---------------------------------------------------
# APP FACTORY
# ---------------------------------------------------

def create_app(testing=False):
    load_dotenv()

    app = Flask(__name__)

    # ----------------------------
    # Config
    # ----------------------------
    app.config.from_object(Config)

    if testing:
        app.config["TESTING"] = True

    # ----------------------------
    # Attach Mongo DB
    # ----------------------------
    app.mongo_client = client
    app.db = db

    # ----------------------------
    # VERIFY DB CONNECTION
    # ----------------------------
    try:
        client.admin.command("ping")
        print("\n===============================")
        print("✅ MongoDB Connected")
        print(f"📦 Database: {db.name}")
        print("📂 Collections:", db.list_collection_names())
        print("===============================\n")
    except Exception as e:
        print("\n===============================")
        print("❌ MongoDB Connection Failed")
        print(str(e))
        print("===============================\n")

    # ----------------------------
    # JWT
    # ----------------------------
    JWTManager(app)

    # ----------------------------
    # Blueprints
    # ----------------------------
    app.register_blueprint(auth_bp, url_prefix="/api/auth")
    app.register_blueprint(ngo_bp, url_prefix="/api/ngo")
    app.register_blueprint(shelter_bp, url_prefix="/api/shelters")
    app.register_blueprint(public_bp, url_prefix="/api")
    app.register_blueprint(emergency_bp, url_prefix="/api")

    # ----------------------------
    # PRINT ROUTES
    # ----------------------------
    print("\n========== REGISTERED ROUTES ==========")

    for rule in app.url_map.iter_rules():
        methods = ",".join(sorted(rule.methods - {"HEAD", "OPTIONS"}))
        print(f"{methods:20s} {rule.rule}")

    print("======================================\n")

    # ----------------------------
    # Health Check
    # ----------------------------
    @app.route("/health", methods=["GET"])
    def health():
        return jsonify({"status": "ok"}), 200

    # ----------------------------
    # Error Handling
    # ----------------------------
    register_error_handlers(app)

    return app


# ---------------------------------------------------
# RUN LOCALLY
# ---------------------------------------------------

if __name__ == "__main__":
    app = create_app()
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug= False)
