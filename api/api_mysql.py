from api import app


@app.route("/")
def query():
    return "hello world"
