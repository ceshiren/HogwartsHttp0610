import requests


class Wework:
    def __init__(self):
        self.token = None

    def token_get(self):
        if self.token is None:
            r = requests.get(
                "https://qyapi.weixin.qq.com/cgi-bin/gettoken",
                params={
                    'corpid': 'wwd6da61649bd66fea',
                    'corpsecret': 'heLiPlmyblHRiKAgGWZky4-KdWqu1V22FeoFex8RfM0'
                }
            )

            print(r.text)
            self.token = r.json()['access_token']

        return self.token

    def tag_list(self):
        r = requests.post(
            'https://qyapi.weixin.qq.com/cgi-bin/externalcontact/get_corp_tag_list',
            params={"access_token": self.token_get()},
            json={"tag_id": []}
        )

        return r

    def tag_add(self, group_name, tag_name):
        return requests.post(
            'https://qyapi.weixin.qq.com/cgi-bin/externalcontact/add_corp_tag',
            params={"access_token": self.token_get()},
            json={
                'group_name': group_name,
                'tag': [{'name': tag_name}]
            }
        )

    def tag_find(self, name):
        r = self.tag_list()
        print(r.text)
        assert r.status_code == 200
        assert r.json()['errcode'] == 0
        tag_id = [tag for group in r.json()['tag_group'] for tag in group['tag'] if tag['name'] == name][0]['id']
        return tag_id

    def tag_delete(self, tag_id):
        return requests.post(
            'https://qyapi.weixin.qq.com/cgi-bin/externalcontact/del_corp_tag',
            params={"access_token": self.token},
            json={
                # 'group_name': '0610',
                'tag_id': [tag_id]
            }

        )
