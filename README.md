# FastAPI-demo

this a demo of me playing around and enjoying FastAPI.

## Installation

```bash
# Clone the repository
git clone https://github.com/0xAlMo3geZ/FastAPI-demo.git

# Change directory to the project folder
cd FastAPI-demo

# Create a virtual environment (optional but recommended)
python3 -m venv venv

# Activate the virtual environment
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

## Usage

```bash
# Start the FastAPI application
uvicorn main:app --reload

or

# Start from module(blog)
uvicorn blog.main:app --reload
```

## API Documentation

- API documentation is available at [http://localhost:8000/docs](http://localhost:8000/docs)
- Alternatively, you can view the API documentation at [http://localhost:8000/redoc](http://localhost:8000/redoc)
