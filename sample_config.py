import os

class Config(object):

    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "1837150324:AAF8uzffjQnzBgwml_lLN20-qIN5fmFbsy0")

    APP_ID = int(os.environ.get("APP_ID", 4510400))

    API_HASH = os.environ.get("API_HASH", "b31f471625366d5d468e0617cb4dcf3d")
