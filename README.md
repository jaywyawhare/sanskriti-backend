# SanskritiBench Backend

This is the backend for the [SanskritiBench project](https://discord.com/invite/BK8UmK3xZC). It is a FastAPI-based REST API that serves data for the frontend and includes CRUD operations.

## Installation

1. Clone the repository

2. Install dependencies using `pip install -r requirements.txt`.

3. Create a `.env` file in the root directory using the `.env.example` file as a template. Populate it with appropriate values for `SECRET_KEY`, `ALGORITHM`, and `DATABASE_URL`.

4. Set up the database by running the following commands:
   ```bash
   python3 scripts/inital_data.py
   ```

5. Run the server:
   ```bash
   uvicorn main:app --reload
   ```

