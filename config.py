import os

class Config:
    # ── SQLite (default — no setup needed) ─────────────────────────────────
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{os.path.join(BASE_DIR, 'transport.db')}"

    # ── MySQL (uncomment when ready) ────────────────────────────────────────
    # SQLALCHEMY_DATABASE_URI = (
    #     "mysql+pymysql://root:YOUR_PASSWORD@localhost/kkg_transport"
    # )

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'kkg-transport-secret-2026'
