import json


# json 是字符串 json中的key不论是数字还是字符串都要用双引号括起来
# dict 是 python 一种数据格式
# json.dumps把一个Python对象编码转换成json字符串
# json.loads把json格式字符串解码转换成Python对象

def test_json():
    strs = '{"name": "gzj", "age": "23", "sex": "man"}'
    data = json.loads(strs)
    print(type(data))
    print(data['name'])


def test_dump():
    dicts = {'name': "张三", 'age': 18}
    print(dicts['name'])
    print(json.dumps(dicts))


if __name__ == '__main__':
    test_dump()
