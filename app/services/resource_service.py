import app.models as context


def get_useful_links() -> list:
    """ 
    Returns useful links for the help section of
    the home page.
    """
    return [{'text': link.Text, 'href': link.URL}
            for link in context.Link.query.all()]
