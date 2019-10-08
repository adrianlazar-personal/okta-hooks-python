class TokenHook():

    def __init__(self):
        return

    def compile_response(self, request_data):

        response_data = {
            "commands":[
                {
                    "type":"com.okta.identity.patch",
                    "value":[
                        {
                            "op":"add",
                            "path":"/claims/custom_claim",
                            "value":"This is my custom id_token claim."
                        }
                    ]
                }
            ]
        }

        return response_data        
'''
{
    "type": "com.okta.access.patch",
    "value":
    {
        "op":"add",
        "path":"/claims/my-flask-access-token-claim",
        "value":"This is my custom access_token claim."
    }
}
'''
        