import web

urls = (
    "/", "home"
)
render = web.template.render("Views/Templates", base="MainLayout")
app = web.application(urls, globals())


# Classes/routes

class home:
    def GET(self):
        return render.Home()


if __name__ == "__main__":
    app.run()