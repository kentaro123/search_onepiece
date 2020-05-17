# -*- coding: utf-8 -*-
#!/usr/bin/env python3
import sys
sys.path.append("..")
from conf import *
import os
from flask import Flask
from server.views import *

if __name__ == '__main__':
    args=get_args()
    print('\nhttp_host:{},http_port:{}'.format('192.168.1.29',args.http_port))
    """
    app.run(debug=True, host='192.168.100.101', port=args.http_port)
    """
    # app.run(debug=False,host=os.getenv('APP_ADDRESS', 'localhost'), port=8000)
    app.run(debug=False)

app = Flask(__name__)
