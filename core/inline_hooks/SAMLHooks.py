class SAMLHook():

    def __init__(self):
        return

    def compile_response(sel, request_data):

        response_data = {
            "commands": [             
                {
                    "type": "com.okta.assertion.patch",
                    "value": [
                        {
                            "op": "replace",
                            "path": "/authentication/sessionIndex",
                            "value": "definitelyARealSession"
                        }
                    ]
                },
                {
                    "type": "com.okta.assertion.patch",
                    "value": [
                        {
                            "op": "add",
                            "path": "/claims/CUSTOM_CLAIM",
                            "value": {
                                "attributes": {
                                    "NameFormat": "urn:oasis:names:tc:SAML:2.0:attrname-format:basic"
                                },
                                "attributeValues":[
                                    {
                                        "attributes":{
                                            "xsi:type":"xs:string"
                                        },
                                        "value":"MY CUSTOM CLAIM"
                                    }
                                ]
                            }
                        }
                    ]
                }                
            ]
        }

        return response_data


