from time import sleep
class ImportHook():

    def __init__(self):
        return

    def compile_response(self, request_data):
        if(request_data["data"]["appUser"]["profile"]["lastName"] == "User1"):
            response_data = {
                "commands":[
                    {
                        "type":"com.okta.action.update",
                        "value":{
                            "result":"CREATE_USER"
                        }
                    } 
                ]
            }
            return response_data
        return None


"""         request_userName = request_data["data"]["appUser"]["profile"]["userName"]
        conflict = request_data["data"]["context"]["conflicts"]
        added_value = "1" """

"""         if conflict != []:
            new_userName = request_userName + added_value
            response_data = {
                "commands":
                    [
                        {
                            "type":"com.okta.appUser.profile.update",
                            "value":{
                                "userName":new_userName
                            }
                        }
                    ]
            }
        else:
            if added_value in request_userName:
                len_added_value = int(len(added_value))
                len_request_userName = int(len(request_userName))
                total = len_request_userName - len_added_value
                new_userName = request_userName[0:total]
                response_data = {
                    "commands":[
                        {
                            "type":"com.okta.user.profile.update",
                            "value":{
                                "lastName":new_userName
                            }
                        }
                    ]
                }
            else:
                response_data = {
                    "commands":[
                        {
                            "type":"com.okta.action.update",
                            "value":{
                                "result":"CREATE_USER"
                            }
                        } 
                    ]
                }
        #sleep(10) """
