from .middle_samrt_api import new_middle_smart_api
from .bll_smart_image import new_bll_smart_image


class API:
    def __init__(self, token):
        self.bll_smart_image = new_bll_smart_image(token)
        self.middle_smart_api = new_middle_smart_api(token)


def new_api(token):
    return API(token)