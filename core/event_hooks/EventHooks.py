from core.ErrorGenerator import ErrorGenerator
import json

e = ErrorGenerator()

class EventHook():

    def  __init__(self, request_headers=None, request_data=None):

        return
    
    def one_time_verification(self, request_headers=None):

        try:
            if request_headers['X-Okta-Verification-Challenge'] != '':
                response = {
                    "verification": request_headers['X-Okta-Verification-Challenge']
                }
                return response
        except KeyError:
            return e.error("Not sure what happend here", 502)
