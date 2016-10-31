#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import urllib
from utils import escape_html, rot13

form = """
<!DOCTYPE HTML>
<html>
<head>
    <title>Unit2 ROT13</title>
</head>
<body>
    <h2>Enter some text to ROT13:</h2>
    <form method="post">
        <textarea name="text" style="height: 100px; width: 400px;">%(text)s</textarea>
        <br>
        <input type="submit">
    </form>
    </body>
</html>"""


class MainHandler(webapp2.RequestHandler):
    def write_form(self,text=""):
        self.response.write(form % {"text":escape_html(text)})

    def get(self):
        self.write_form()

    def post(self):
        #newurl = '/rot13?' + urllib.urlencode(self.request.params)
        text_to_rot13 = self.request.get("text")
        result = rot13(text_to_rot13)
        return self.write_form(result)
        #return self.redirect(newurl)

#class Rot13Handler(webapp2.RequestHandler):
#    def get(self):
#        text_to_rot13 = self.request.get("text")
#        result = rot13(text_to_rot13)
#        return self.response.write(form % {"text":escape_html(result)})

#    def post(self):
#        return self.redirect('/')


app = webapp2.WSGIApplication([
    ('/', MainHandler)
    #('/rot13',Rot13Handler)
], debug=True)
