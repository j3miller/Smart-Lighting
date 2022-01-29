from app.run import app


# Generic Endpoints
@app.route('/')
def home():
    return '<p> hello world </p>'
