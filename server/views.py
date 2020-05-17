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

@app.route('/result',methods=["POST","GET"])
def look_up():
    kg = KnowGraph()
    client_params = request.form
    server_param = {}
    cont = kg.lookup_entry(client_params,server_param)
    return render_template("result.html",cont=cont)
#
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

# -------------------------------------------------------------------
