# string to hold the acceptable format for a url.
url_format = "https://quizlet.com/"


# Function to check if the url is a quizlet valid url in the proper format.
def quizlet_valid_url(url):
    if len(url) < len(url_format):
        return False
    else:
        for a in range(len(url_format)):
            if not url[a] == url_format[a]:
                return False
        return True

