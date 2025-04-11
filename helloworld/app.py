from bottle import Bottle, run

app = Bottle()

@app.route('/')
def hello():
    return "Hello, world!"

if __name__ == "__main__":
    run(app, host="0.0.0.0", port=8081)