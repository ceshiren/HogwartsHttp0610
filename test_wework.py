import requests

from wework import Wework


class TestWework:
    def setup_class(self):
        #清理所有的测试用的tag
        pass

    def setup(self):
        self.wework = Wework()
        self.token = self.wework.token_get()

    def test_tags_list(self):
        r = self.wework.tag_list()
        print(r.text)
        assert r.status_code == 200
        assert r.json()['errcode'] == 0

    def test_tag_add(self):
        r = self.wework.tag_add("0610", '0610')
        print(r.text)
        assert r.json()['errcode'] == 0

    def test_tag_delete(self):
        # 解除顺序依赖
        self.wework.tag_add('0610', '0611')
        tag_id = self.wework.tag_find("0611")
        r = self.wework.tag_delete(tag_id)
        print(r.text)
        assert r.json()['errcode'] == 0
