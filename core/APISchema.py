class API():
    
    def __init__(self):
        pass

    def build_api(self, request_url):

        api_schema = {
            "author":"Adrian Lazar",
            "schema":"API/V1, HTTP 1.1",
            "endpoints": {
                "event_hooks":{
                    "master_link":f"{request_url}hooks/api/v1/eventHooks",
                    "implementations":[
                        {
                            "source": "Okta",
                            "link":f"{request_url}hooks/api/v1/eventHooks/Okta"
                        }
                    ]
                },
                "inline_hooks":{
                    "master_link":f"{request_url}hooks/api/v1/inlineHooks",
                    "implementations":{
                        "import_hooks":[
                            {
                                "source":"Okta",
                                "link":f"{request_url}hooks/api/v1/inlineHooks/Okta/importHooks"
                            }
                        ],
                        "token_hooks":[
                            {
                                "source":"Okta",
                                "link":f"{request_url}hooks/api/v1/inlineHooks/Okta/tokenHooks"
                            }
                        ],
                        "saml_hooks":[
                            {
                                "source":"Okta",
                                "link":f"{request_url}hooks/api/v1/inlineHooks/Okta/samlHooks"
                            }
                        ],
                        "registration_hooks":[
                            {
                                "source":"Okta",
                                "link":f"{request_url}hooks/api/v1/inlineHooks/Okta/registrationHooks"
                            }
                        ]
                    }
                }
            }
        }    
        return api_schema



