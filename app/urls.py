from app import indexBlueprint

from app.views.index import indexView

indexBlueprint.add_url_rule('/', None, indexView, methods=["POST", "GET"])
