# ParkEase 🚗

A Flask-based parking management system with Supabase database integration.

## Features

- User authentication and session management
- Secure password hashing
- Database integration with Supabase PostgreSQL
- Environment-based configuration
- Connection testing utilities

## Tech Stack

- **Backend**: Flask (Python)
- **Database**: Supabase (PostgreSQL)
- **ORM**: SQLAlchemy
- **Authentication**: Werkzeug Security
- **Environment Management**: python-dotenv

## Prerequisites

- Python 3.7+
- Supabase account and project
- Git

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Surajkeshri95/parkease.git
   cd parkease
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   
   Create a `.env` file in the root directory:
   ```env
   SECRET_KEY=your-super-secret-key-here
   SUPABASE_DB_URL=postgresql://postgres.your-project-ref:YOUR_PASSWORD@aws-0-region.pooler.supabase.com:6543/postgres
   ```

   **To get your Supabase database URL:**
   - Go to your Supabase project dashboard
   - Navigate to Settings → Database
   - Copy the connection string from "Connection string" section
   - Replace `YOUR_PASSWORD` with your actual database password

## Configuration

The application uses environment-based configuration through `config.py`:

- `SECRET_KEY`: Used for session management and security
- `SUPABASE_DB_URL`: PostgreSQL connection string for Supabase
- Database connection pooling is pre-configured for optimal performance

## Usage

1. **Test database connection first**
   ```bash
   python test_connection.py
   ```

2. **Run the application**
   ```bash
   python app.py
   ```

3. **Access the application**
   
   Open your browser and navigate to `http://localhost:5000`

## Database Setup

The application automatically creates database tables on first run. If you need to manually initialize:

```python
from app import app, db

with app.app_context():
    db.create_all()
```

## Project Structure

```
parkease/
├── app.py              # Main Flask application
├── config.py           # Configuration settings
├── requirements.txt    # Python dependencies
├── test_connection.py  # Database connection tester
├── .env               # Environment variables (create this)
└── README.md          # Project documentation
```

## Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `SECRET_KEY` | Flask secret key for sessions | Yes |
| `SUPABASE_DB_URL` | Supabase PostgreSQL connection string | Yes |

## Troubleshooting

### Database Connection Issues

If you encounter database connection problems:

1. **Verify your Supabase URL format:**
   ```
   postgresql://postgres.PROJECT_REF:PASSWORD@HOST:5432/postgres
   ```

2. **Check your database password**
   - Ensure you've replaced `YOUR_PASSWORD` with your actual password
   - Verify the password in your Supabase dashboard

3. **Test connection:**
   ```bash
   python test_connection.py
   ```

### Common Error Messages

- **"Could not connect to database"**: Check your `.env` file and database credentials
- **"No module named 'psycopg2'"**: Run `pip install psycopg2-binary`
- **"Secret key not found"**: Ensure your `.env` file contains `SECRET_KEY`

## Security Notes

- Never commit your `.env` file to version control
- Use strong, unique passwords for your database
- Change the default `SECRET_KEY` in production
- Enable SSL in production environments

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

**Suraj Keshri** - [@SurajKeshri95](https://github.com/SurajKeshri95)

## Team member

**vivek kumar** - [@Vivek kumar]( https://github.com/302004vivekkumar ).
## Acknowledgments

- Flask community for the excellent web framework
- Supabase for providing an excellent database solution
- SQLAlchemy for the powerful ORM

---

⭐ Don't forget to star this repository if you found it helpful!
