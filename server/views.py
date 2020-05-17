# -*- coding: utf-8 -*-
# -------------------------------------------------------------------
#
#   hello.py
#
#                       Aug/07/2017
# -------------------------------------------------------------------
import os
from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("login.html")
#
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

# -------------------------------------------------------------------
