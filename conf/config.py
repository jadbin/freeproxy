# coding=utf-8

proxy_pages = {
    'xicidaili': ['http://www.xicidaili.com/wt/{}'.format(i) for i in range(1, 11)],
    '89ip': 'http://www.89ip.cn/tqdl.html?num=1000',
    '66ip': 'http://www.66ip.cn/mo.php?tqsl=1000',
    'kuaidaili': ['https://www.kuaidaili.com/free/inha/{}/'.format(i) for i in range(1, 6)]
                 + ['https://www.kuaidaili.com/free/intr/{}/'.format(i) for i in range(1, 6)],
    'cn-proxy': 'http://cn-proxy.com/',
    'data5u': ['http://www.data5u.com/free/gngn/index.shtml',
               'http://www.data5u.com/free/gnpt/index.shtml',
               'http://www.data5u.com/free/gwgn/index.shtml',
               'http://www.data5u.com/free/gwpt/index.shtml'],
    'crossin': ['http://lab.crossincode.com/proxy/', 'http://lab.crossincode.com/proxy/get/?num=20'],
    # 'baibianip': 'https://www.baibianip.com/home/free.html'
}
