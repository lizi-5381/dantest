#案例一：查询快递
#coding:utf-8

import unittest
import requests

class Test_kuaidi(unittest.TestCase):
    def setUp(self):
        pass
        self.headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'}
        self.s=requests.session()
    def test_yunda(self):
        u'测试快递查询用例'
        danhao='4314154524842'
        kd='yunda'
        self.url='http://www.kuaidi.com/index-ajaxselectcourierinfo-%s-%s-KUAIDI1620357666814.html'%(danhao,kd)
        print(self.url)
        #第一步，发送请求
        r=self.s.post(self.url,headers=self.headers,verify=False)
        result=r.json()
        #第二步，获取结果
        print(result['company'])
        data=result['data']
        print(data[0])
        get_result=data[0]['context']
        print(get_result)
        # 断言：测试结果与期望结果对比
        self.assertEqual(u'韵达快递',result['company'])
        self.assertIn(u'已签收',get_result)
if __name__ =='__main__':
    unittest.main()