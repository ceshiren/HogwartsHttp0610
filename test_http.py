import requests

def test_get():
    r=requests.get("http://httpbin.ceshiren.com/get", params={"a": 1})
    print(r.text)
    assert r.status_code == 200
    assert r.json()['args']['a'] == '1'

def test_post():
    r=requests.post("http://httpbin.ceshiren.com/post", data={"custname": "seveniruby"})
    print(r.text)
    assert r.status_code == 200
    assert r.json()['form']['custname'] == 'seveniruby'
