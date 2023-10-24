class MiddleSmartApi:
    def __init__(self, token):
        self.token = token

    def get_pip(self):
        print(self.token)
        print("MiddleSmartApi getPip")
        return "pip"


def new_middle_smart_api(token):
    return MiddleSmartApi(token)