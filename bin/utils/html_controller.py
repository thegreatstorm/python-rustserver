import http.client as client


def url_exists(site, path):
    conn = client.HTTPConnection(site)
    conn.request('HEAD', path)
    response = conn.getresponse()
    conn.close()
    if response.status == 200:
        return True
    else:
        return False