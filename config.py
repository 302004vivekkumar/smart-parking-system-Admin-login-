import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Config:
    # Secret key for sessions (keep this secret!)
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your-secret-key-change-this-in-production'
    
    # Supabase database connection
    SQLALCHEMY_DATABASE_URI = os.environ.get('SUPABASE_DB_URL') or 'sqlite:///parkease.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # Optional: Add more config as needed
    SQLALCHEMY_ENGINE_OPTIONS = {
        'pool_timeout': 20,
        'pool_recycle': -1,
        'pool_pre_ping': True
    }