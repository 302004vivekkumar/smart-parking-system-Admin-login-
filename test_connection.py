from app import app, db
import sys

def test_database_connection():
    """Test if we can connect to Supabase database"""
    try:
        with app.app_context():
            # Try to connect to database
            db.create_all()
            print("✅ SUCCESS: Connected to Supabase database!")
            print(f"Database URL: {app.config['SQLALCHEMY_DATABASE_URI'][:50]}...")
            return True
    except Exception as e:
        print("❌ ERROR: Could not connect to database")
        print(f"Error: {str(e)}")
        return False

if __name__ == "__main__":
    print("Testing Supabase connection...")
    success = test_database_connection()
    
    if success:
        print("\n🎉 Your Supabase setup is working!")
        print("You can now run your Flask app with: python app.py")
    else:
        print("\n🔧 Please check:")
        print("1. Your .env file has the correct SUPABASE_DB_URL")
        print("2. Your Supabase project is running")
        print("3. You replaced YOUR_PASSWORD in the connection string")
        sys.exit(1)