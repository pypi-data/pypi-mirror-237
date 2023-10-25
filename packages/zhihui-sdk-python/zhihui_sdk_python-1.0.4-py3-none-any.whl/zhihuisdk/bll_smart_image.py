class BllSmartImage:
    def __init__(self, token):
        self.token = token

    def render_apollo(self):
        print("renderApollo")
        return "renderApollo"


def new_bll_smart_image(token):
    return BllSmartImage(token)