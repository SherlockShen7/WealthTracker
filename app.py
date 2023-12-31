from flask import Flask

app = Flask(__name__)
def make_bold(function):
    def wrap_function():
        text = "<b>" + function() + "</b>"
        return text
    return wrap_function

@app.route("/")
@make_bold
def hello():
    return "Hello"

if __name__ == "__main__":
    app.run(debug=True)