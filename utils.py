import cgi
import codecs


def escape_html(s):
    return cgi.escape(s,quote="True")

def rot13(text):
    return codecs.encode(text, 'rot_13')
