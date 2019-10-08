from flask import Flask, render_template, request, Markup, Response
from core.event_hooks.EventHooks import EventHook
from core.inline_hooks.ImportHooks import ImportHook
from core.inline_hooks.TokenHooks import TokenHook
from core.inline_hooks.RegistrationHooks import RegistrationHook
from core.inline_hooks.SAMLHooks import SAMLHook
from datetime import datetime

from core.APISchema import API
import json, time


app = Flask(__name__)

@app.route('/')
def index(name=None):
    return render_template('index.html', name=index)

@app.route("/api/v1", methods = ["GET", "OPTIONS"])
def apis():
    api = API()
    res = api.build_api()
    response = app.response_class(
        response=json.dumps(res),
        status = 200,
        #headers = ("Content-Type: application/json", "X-Adrian-Custom: Adrian-Lazar-Custom-Header")
        mimetype = "application/json"
    )
    return response

@app.route('/api/v1/eventHooks/Okta', methods=["GET", "POST", "OPTIONS"])
def eventHooks():

    request_headers = request.headers

    if request.method == "GET":
        
        if request.headers.get('User-Agent') == 'Okta-Integrations':
            hook = EventHook(request_headers)
            response = hook.one_time_verification(request_headers)
            verify = app.response_class(
                response=json.dumps(response), 
                status=200, 
                mimetype='application/json'
                )
            return verify

        else:
            return "Hello World!"    
    
    if request.method == "POST":
        
        data = request.data
        if data:
            request_data = json.loads(data)
        response = app.response_class(
            response = '',
            status = 204,
            mimetype= 'application/json'
        )
        return response



@app.route('/api/v1/inlineHooks/Okta/importHooks', methods=["GET", "POST", "OPTIONS"])
def importHooks():
    request_headers = request.headers

    if request.method == "POST":
        
        request_data = json.loads(request.data)
        import_hook = ImportHook()
        res = import_hook.compile_response(request_data)
        response = app.response_class(
            response = json.dumps(res),
            status = 200,
            mimetype = "application/json"
        )
        return response

    if request.method == "GET":
        
        return "Hello World!"

@app.route('/api/v1/inlineHooks/Okta/tokenHooks', methods=["GET", "POST", "OPTIONS"])
def tokenHooks():
    request_headers = request.headers

    if request.method == "POST":

        request_data = json.loads(request.data)
        token_hook = TokenHook(request_data)
        res = token_hook.compile_response()
        response = app.response_class(
            response = json.dumps(res),
            status = 200,
            mimetype = 'application/json'
        )
        return response
    
    if request.method == "GET":
        
        return "Hello World!"

@app.route('/api/v1/inlineHooks/Okta/samlHooks', methods=["GET", "POST", "OPTIONS"])
def samlHooks():
    request_headers = request.headers

    if request.method == "POST":

        request_data = json.loads(request.data)
        saml_hook = SAMLHook()
        res = saml_hook.compile_response(request_data)
        response = app.response_class(
            response = json.dumps(res),
            status = 200,
            mimetype = "application/json" 
        )
        return response

    if request.method == "GET":
        
        return "Hello World!"

@app.route('/api/v1/inlineHooks/Okta/registrationHooks', methods=["GET", "POST", "OPTIONS"])
def registrationHooks():
    request_headers = request.headers

    if request.method == "POST":

        request_data = json.loads(request.data)
        reg_hook = RegistrationHook()
        res = reg_hook.compile_response(request_data)
        response = app.response_class(
            response = json.dumps(res),
            status = 200,
            mimetype = 'application/json'
        )
        return response
    
    if request.method == "GET":
        
        return "Hello World!"

if __name__ == '__main__':

    app.run(port=4000, debug=True)