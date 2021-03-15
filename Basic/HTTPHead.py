import http.client
c = http.client.HTTPConnection("www.python.org", 80)
c.putrequest("HEAD", "/index.html")
c.putheader("User-agent", "pythonclass")
c.endheaders()

r = c.getresponse()
r.status
r.reason
r.getheaders()
c.close()