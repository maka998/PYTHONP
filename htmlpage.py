class HTMLpage():
    # name
    # path
    # content

    def __init__(self, name, path, content, links):
        self.name = name
        self.content = content
        self.links = links
        #self.rang = 0

    def __str__(self):
        return self.name

#dobijamo informaciju o imenu,sadrzaj ,i linkovima