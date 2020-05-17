# -*- coding: utf-8 -*-
# -------------------------------------------------------------------
#
#   hello.py
#
#                       Aug/07/2017
# -------------------------------------------------------------------
import os
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    str_out = ""
    str_out += "<h2>Hello from Python!</h2>"
    str_out += "<blockquote>"
    str_out += "こんにちは<p />"
    str_out += "</blockquote>"
    str_out += "Aug/07/2017 PM 12:49<br />"
#
    return str_out
#
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

# -------------------------------------------------------------------
