from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    return "Hello, World"

@app.route('/template')
def template():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True, port=9000)

@app.route("/sign-service-anyflow/sign-docs", methods=['POST'])
def sign_docs():
    pass