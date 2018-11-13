from app.admin import admin


@admin.route("/")
def index():
    return "admin"
