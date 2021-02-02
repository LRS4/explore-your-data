import app.models as context
import time


def get_useful_links() -> list:
    """ 
    Returns useful links for the help section of
    the home page.
    """
    retry_flag = True
    retry_count = 0
    while retry_flag and retry_count < 5:
        try:
            return [{'text': link.Text, 'href': link.URL}
                    for link in context.Link.query.all()]
            retry_flag = False
        except:
            print("Retry after 1 sec")
            retry_count = retry_count + 1
            time.sleep(1)
