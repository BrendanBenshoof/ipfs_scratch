import requests, json, time
import StringIO


class IPFSclient(object):
    def __init__(self,uri):
        """
            Initalize the IPFS client with the path to the running IPFS http-api instance.
        """
        self.uri = uri

    def add_string(self,src):
        """
            add a string as a nameless file to IPFS
            returns hashid of file on network
        """
        cmd = "/api/v0/add?stream-channels=true"
        fp = StringIO.StringIO(src)
        files = {'file': ("", fp,"application/octet-stream")}
        r = requests.post(self.uri+cmd,files=files)
        return r.json()["Hash"]

    def add_file(self,fp):
        """
            add a file as a nameless file to IPFS
            fp = file-like object
            returns hashid of file on network
        """
        cmd = "/api/v0/add?stream-channels=true"
        files = {'file': (fp.name, fp,"application/octet-stream")}
        r = requests.post(self.uri+cmd,files=files)
        return r.json()["Hash"]

    def cat(self,hashid):
        cmd = "/api/v0/cat/%s"%hashid
        r = requests.get(self.uri+cmd)
        return r.text


if __name__ == "__main__":

    c = IPFSclient("http://127.0.0.1:5001")
    hashid =  c.add_string("the time is now %s"%str(time.time()))
    print c.cat(hashid)
    print hashid
