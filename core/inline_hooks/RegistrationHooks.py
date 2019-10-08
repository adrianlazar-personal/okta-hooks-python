class RegistrationHook():

    global request_data

    def __init__(self):
        return

    def compile_response(self, request_data):

        response_data = {
            "commands":[
                {
                    "type":"com.okta.action.update",
                    "value":{
                        "registration":"ALLOW"
                    }
                },
                {
                    "type":"com.okta.user.profile.update",
                    "value":{
                        "login":""
                    }
                }
            ]
        }
        old_login = request_data["data"]["userProfile"]["login"]
        find_at = int(old_login.find("@"))
        removed_at = old_login[0:find_at]
        new_login = removed_at + "@myflaskapp.com"  
        response_data["commands"][1]["value"]["login"] = new_login

        return response_data
        