from app.home import home


@home.route("/")
def index():
    return "home"
