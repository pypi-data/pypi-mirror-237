from pygdshort import link
import sys
import argparse

def shorten(url, custom=None):
    
    try:
        short_link = link.shorten(long_url=url, custom_short_url=custom)
        print(short_link)
        sys.exit(0)
    
    except link.LongUrlError as e:
        print(e)
        sys.exit(1)

    except link.ShortUrlError as e:
        print(e)
        sys.exit(1)
    
    except link.RateLimitError as e:
        print(e)
        sys.exit(1)
    
    except link.GenericError as e:
        print(e)
        sys.exit(1)
    


def expand(url):
    
    try:
        long_link = link.expand(short_url=url)
        print(long_link)
        sys.exit(0)
    
    except link.LongUrlError as e:
        print(e)
        sys.exit(1)

    except link.ShortUrlError as e:
        print(e)
        sys.exit(1)
    
    except link.RateLimitError as e:
        print(e)
        sys.exit(1)
    
    except link.GenericError as e:
        print(e)
        sys.exit(1)

if __name__ == 'pygdshort.cli':
    parser = argparse.ArgumentParser(prog='pygdshort', description='Shorten URLs using the is.gd API')
    parser.add_argument('url', help='The URL to shorten or expand', type=str)
    parser.add_argument('-c', '--custom', help='The custom short URL to be used (Optional)', type=str)
    parser.add_argument('-e', '--expand', help='Expand a shortened URL', action='store_true')
    args = parser.parse_args()
    
    if args.expand == True:
        expand(args.url)
    
    else:
        shorten(args.url, args.custom)

sys.exit(0)
