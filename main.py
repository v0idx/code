import os
import sys
import requests

sys.path.insert(0, os.path.dirname(__file__))

def getCode(subPath):
    if subPath != '/':
        file = "/home/********/code.v0idx.com/files"
        file += subPath
        
        with open(file,'r') as f:
            content = f.readlines()
            f.close()
    else:
        content = [""]
    return ''.join(content).replace('<','&lt').replace('>','&gt')


def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    resp = []
    resp.append("<!DOCTYPE HTML>")
    resp.append("<html><head>")
    resp.append("<title>")
    resp.append(environ['PATH_INFO'][1::])
    resp.append("</title>")
    resp.append("<link rel='stylesheet' href='https://code.v0idx.com/styling/materialdark.css'>")
    resp.append("<script src='https://cdnjs.cloudflare.com/ajax/libs/highlight.js/10.1.2/highlight.min.js'></script>")
    resp.append("<script>hljs.initHighlightingOnLoad();</script>")
    resp.append("</head>")
    resp.append("<body>")
    resp.append("<pre>")
    resp.append("<code>")
    resp.append(getCode(environ['PATH_INFO']))
    resp.append("</code>")
    resp.append("</pre>")
    resp.append("</body>")
    resp.append("</html>")
    
    text = ''.join(resp)
    
    return [text.encode()]
