import base64

#Converts string to base64

class Encoder:
    def encod3(self):
        user_creds = base64.b64encode(bytes(input("Enter your credentials: "), 'utf-8'))
        decodesw2 = user_creds.decode('utf-8')
        
        print(decodesw2)
        return decodesw2, user_creds

ewan = Encoder()
ewan.encod3()