from app.database import db

class Link(db.Model):
    __tablename__ = 'Link'

    LinkId = db.Column(db.Integer, primary_key=True)
    Text = db.Column(db.String())
    URL = db.Column(db.String())

    def __init__(self, LinkId, Text, URL):
        self.LinkId = LinkId
        self.Text = Text
        self.URL = URL

    def __repr__(self):
        return f'<id {self.LinkId}>'
