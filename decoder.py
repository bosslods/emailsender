import base64

class decoded_creds:
    def __init__(self, encoded_user, encoded_pass):
        self.user_pass = encoded_user
        self.user_user = encoded_pass
    def decod3_user(self):
        decoded_user = base64.b64decode(self.user_user).decode('utf-8')
        return decoded_user
    def decod3_pass(self):
        decoded_pass = base64.b64decode(self.user_pass).decode('utf-8')
        return decoded_pass
    
Z = decoded_creds("'WXFoUjFYT2F5UmIwQTZOZQ=='", "'a291c2VAa3JhemllbWFpbC5tbA=='")

    