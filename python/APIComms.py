
import json
import requests

def SubmitURL():
  host = '192.168.0.10'
  port = 80
  endpoint = 'printer/command'
  data = json.dumps({
        'command': 'M114',
     })
  key = '8A1AF666EE3848A4845E7401E8A0E786'  # type: str

  headers = {
     'Content-type': 'application/json',
      'X-Api-Key': key,
   }  # type: Dict[str, str]
  r = requests.post(
      url="http://{host}:{port}/api/{endpoint}".format(
       host=host,
       port=port,
       endpoint=endpoint
         ),
    data=data,
    headers=headers
    )

def OneLiner():
    parameters = {"command": "M114"}
    #headers = {"X-Api-Key": "8A1AF666EE3848A4845E7401E8A0E786"}

    r = requests.get("http://192.168.0.10/api/printer/command", params=parameters, headers={"X-Api-Key": "8A1AF666EE3848A4845E7401E8A0E786"})

#print(r)
#print(r.headers)
#print(r.content)
#print(r.text)
#print(data)

SubmitURL()

#OneLiner()