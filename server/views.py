from flask import jsonify
from conf import *
from flask import Flask, render_template
from flask import request
from server.run_server import app
from server.module import KnowGraph
import json
import os


@app.route("/")
def index():
    return render_template("login.html")


@app.route('/result',methods=["POST","GET"])
def look_up():
    kg = KnowGraph()
    client_params = request.form
    server_param = {}
    cont = kg.lookup_entry(client_params,server_param)
    """
    server_param['id']=client_params['id']
    server_param['jsonrpc']=client_params['jsonrpc']
    server_param['method']=client_params['method']
    """
    return render_template("result.html",cont=cont)
