import os
import sys
import requests

sys.path.insert(0, os.path.dirname(__file__))

def readFile(environ):
    link = "https://code.v0idx.com/files" + environ['PATH_INFO']
    text = requests.get(link)
    ret = text.text.replace('<','&lt').replace('>','&gt')
    return ret

def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    text = []
    text.append("<!DOCTYPE HTML><html><head>")
    text.append("<link rel='stylesheet' href='https://code.v0idx.com/styling/dracula.css'><title>code</title> <script src='https://cdnjs.cloudflare.com/ajax/libs/highlight.js/10.1.2/highlight.min.js'></script><script>hljs.initHighlightingOnLoad();</script>")
    text.append("</head><pre><code>")
    if environ['PATH_INFO'] != '/':
        text.append(readFile(environ))
    text.append("</code></pre></html>")

    response = ''.join(text)
    
    return [response.encode()]
