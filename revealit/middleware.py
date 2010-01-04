"""
Django middlewares used by Reveal IT.
"""
from django.utils.html import strip_spaces_between_tags


class SpacelessMiddleware(object):
    """
    Middleware to remove excess whitespace.

    By David Cramer - taken from:
        http://www.davidcramer.net/code/369/spaceless-html-in-django.html
    """
    def process_response(self, request, response):
        if 'text/html' in response['Content-Type']:
            response.content = strip_spaces_between_tags(response.content)
        return response


