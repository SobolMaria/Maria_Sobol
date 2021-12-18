import http.client
import json

conn = http.client.HTTPSConnection("content.dropboxapi.com")
payload = ''
headers = {
  'Dropbox-API-Arg': '{"path": "/Homework/math/Matrices.txt","mode": "add","autorename": true,"mute": false,"strict_conflict": false}',
  'Content-Type': 'application/octet-stream',
  'Authorization': 'Bearer u4IQ1LQxtOoAAAAAAAAAARAUw_0F_0Ty_UfrMz4_cUGJCjResImPFz-DLRTrXwU9'
}
conn.request("POST", "/2/files/upload", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))

conn = http.client.HTTPSConnection("api.dropboxapi.com")
payload = json.dumps({
  "path": "/Homework/math",
  "include_media_info": False,
  "include_deleted": False,
  "include_has_explicit_shared_members": False
})
headers = {
  'Content-Type': 'application/json',
  'Authorization': 'Bearer u4IQ1LQxtOoAAAAAAAAAARAUw_0F_0Ty_UfrMz4_cUGJCjResImPFz-DLRTrXwU9'
}
conn.request("POST", "/2/files/get_metadata", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))

conn = http.client.HTTPSConnection("api.dropboxapi.com")
payload = json.dumps({
  "path": "/homework/math/matrices.txt"
})
headers = {
  'Content-Type': 'application/json',
  'Authorization': 'Bearer u4IQ1LQxtOoAAAAAAAAAARAUw_0F_0Ty_UfrMz4_cUGJCjResImPFz-DLRTrXwU9'
}
conn.request("POST", "/2/files/delete_v2", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))
