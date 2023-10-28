import requests


def shorten(long_url: str, custom_short_url: str = None):
    """Shortens a URL using the is.gd API.
    
    Parameters:
    
        long_url: The URL to be shortened.

        custom_short_url: The custom short URL to be used. (Optional)
    """

    if custom_short_url is not None:
        parameters = {
            "url": long_url,
            "shorturl": custom_short_url,
            "format": "json"
        }
        shortened_url = requests.get("https://is.gd/create.php", params=parameters)

    else:
        parameters = {
            "url": long_url,
            "format": "json"
        }
        shortened_url = requests.get("https://is.gd/create.php", params=parameters)

    shortened_url = shortened_url.json()

    if "errorcode" in shortened_url:

        if shortened_url["errorcode"] == 1:
            raise LongUrlError(shortened_url["errormessage"])

        elif shortened_url["errorcode"] == 2:
            raise ShortUrlError(shortened_url["errormessage"])

        elif shortened_url["errorcode"] == 3:
            raise RateLimitError(shortened_url["errormessage"])

        else:
            raise GenericError(shortened_url["errormessage"])

    else:
        return shortened_url["shorturl"]


def expand(short_url: str):
    """Expands a shortened URL using the is.gd API.
    
    Parameters:

        short_url: The shortened URL to be expanded.
    """

    parameters = {
        "shorturl": short_url,
        "format": "json"
    }
    expanded_url = requests.get("https://is.gd/forward.php", params=parameters)
    expanded_url = expanded_url.json()

    if "errorcode" in expanded_url:

        if expanded_url["errorcode"] == 1:
            raise LongUrlError(expanded_url["errormessage"])

        elif expanded_url["errorcode"] == 2:
            raise ShortUrlError(expanded_url["errormessage"])

        elif expanded_url["errorcode"] == 3:
            raise RateLimitError(expanded_url["errormessage"])

        else:
            raise GenericError(expanded_url["errormessage"])

    else:
        return expanded_url["url"]


class LongUrlError(Exception):
    pass


class ShortUrlError(Exception):
    pass


class RateLimitError(Exception):
    pass


class GenericError(Exception):
    pass
