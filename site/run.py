from werkzeug.contrib.fixers import ProxyFix
from flask import Flask, request

app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app)


@app.route("/")
def hello():
    res = ""
    for header in request.headers:
        res += "{}<br />".format(header)
    return res


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
