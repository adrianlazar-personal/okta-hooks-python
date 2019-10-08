class ErrorGenerator():

    def __init__(self):
        pass

    def error(self, error_message, status_code):
        
        error_dict = {
            "error":{
                "errorSummarry":error_message,
                "satatus":status_code
            }
        }
        response = app.response_class(
            response = json.dumps(error_dict),
            status = status_code,
            mimetype = 'application/json'
        )
        return response

        

