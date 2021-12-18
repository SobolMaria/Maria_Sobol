import http.client
import json
import unittest

class Drop(unittest.TestCase):

    def upload(self):
        self.conn = http.client.HTTPSConnection("content.dropboxapi.com")
        self.payload = ''
        self.headers = {
        'Dropbox-API-Arg': '{"path": "/Homework/math/Matrices.txt","mode": "add","autorename": true,"mute": false,"strict_conflict": false}',
        'Content-Type': 'application/octet-stream',
        'Authorization': 'Bearer u4IQ1LQxtOoAAAAAAAAAARAUw_0F_0Ty_UfrMz4_cUGJCjResImPFz-DLRTrXwU9'
        }
        self.conn.request("POST", "/2/files/upload", payload, headers)
        self.res = conn.getresponse()
        self.data = res.read()
        print(data.decode("utf-8"))

    def get_metadata(self):
        self.conn1 = http.client.HTTPSConnection("api.dropboxapi.com")
        self.payload = json.dumps({
            "path": "/Homework/math",
            "include_media_info": False,
            "include_deleted": False,
            "include_has_explicit_shared_members": False
        })
        self.headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer u4IQ1LQxtOoAAAAAAAAAARAUw_0F_0Ty_UfrMz4_cUGJCjResImPFz-DLRTrXwU9'
        }
        self.conn1.request("POST", "/2/files/get_metadata", payload, headers)
        self.res = conn1.getresponse()
        self.data = res.read()
        print(data.decode("utf-8"))

    def delete(self):
        self.conn1 = http.client.HTTPSConnection("api.dropboxapi.com")
        self.payload = json.dumps({
            "path": "/homework/math/matrices.txt"
        })
        self.headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer u4IQ1LQxtOoAAAAAAAAAARAUw_0F_0Ty_UfrMz4_cUGJCjResImPFz-DLRTrXwU9'
        }
        self.conn1.request("POST", "/2/files/delete_v2", payload, headers)
        self.res = conn1.getresponse()
        self.data = res.read()
        print(data.decode("utf-8"))

if __name__ == '__main__':
    unittest.main()
