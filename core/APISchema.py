class API():
    
    global api_schema

    api_schema = {
        "author":"Adrian Lazar",
        "schema":"API/V1, HTTP 1.1",
        "endpoints": {
            "event_hooks":{
                "master_link":"http://localhost:4000/api/v1/eventHooks",
                "implementations":[
                    {
                        "source": "Okta",
                        "link":"http://localhost:4000/api/v1/eventHooks/Okta"
                    }
                ]
            },
            "inline_hooks":{
                "master_link":"http://localhost:4000/api/v1/inlineHooks",
                "implementations":{
                    "import_hooks":[
                        {
                            "source":"Okta",
                            "link":"http://localhost:4000/api/v1/inlineHooks/Okta/importHooks"
                        }
                    ],
                    "token_hooks":[
                        {
                            "source":"Okta",
                            "link":"http://localhost:4000/api/v1/inlineHooks/Okta/tokenHooks"
                        }
                    ],
                    "saml_hooks":[
                        {
                            "source":"Okta",
                            "link":"http://localhost:4000/api/v1/inlineHooks/Okta/samlHooks"
                        }
                    ],
                    "registration_hooks":[
                        {
                            "source":"Okta",
                            "link":"http://localhost:4000/api/v1/inlineHooks/Okta/registrationHooks"
                        }
                    ]
                }
            }
        }
    }    
    def __init__(self):
        return 

    def build_api(self):
        return api_schema



