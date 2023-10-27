from inspect import stack
from json import loads
from os import path
from re import findall, I
from time import time
from urllib import parse
from urllib.parse import parse_qs, urlparse

from jinja2 import Template


def url_args_get(curl_head: str) -> (str, dict):
    """url和请求参数的获取"""
    # 提取 URL
    url = findall('''curl\s*['"](.*?)['"]''', curl_head)[0]

    # 提取参数
    parsed_url = urlparse(url)  # url
    query_params = parse_qs(parsed_url.query)  # args

    # 格式化参数为字典
    data_dict = {key: value[0] for key, value in query_params.items()}
    url = f'{parsed_url.scheme}://{parsed_url.netloc}{parsed_url.path}'
    return url, data_dict


def headers_get(curl_head: str) -> (dict, dict):
    """headers cookies"""
    head_data = findall('''-H ['"](.*)['"] ''', curl_head)

    if not head_data:
        return {}, {}

    head_dict = {}
    cookies = {}
    for data in head_data:  # 将文本以行进行分割
        data: str = data.strip()
        if not data:  # 过滤掉空的数据
            continue
        if data.startswith(':'):  # 去重字符串的第一个冒号
            data = data.lstrip(':')

        key, value = data.split(':', maxsplit=1)
        if findall('cookie', key, flags=I):  # cookie 解析
            cookie_list = [str(c).strip().split('=', 1) for c in str(value).split(';')]
            cookies = {i[0]: i[1] for i in cookie_list if len(i) == 2}
        else:
            head_dict[key] = value.strip()

    return head_dict, cookies


def data_get(curl_head: str) -> (str, dict):
    """method and data"""

    data_list: list = findall('''--data-raw ['"](.*?)['"] ''', curl_head)
    if not data_list:
        return 'get', dict()

    data_str: str = data_list[0]
    if data_str.startswith('{') and data_str.endswith('}'):
        return 'json_post', loads(data_str)
    else:
        data = {key: value for key, value in (i.split('=') for i in data_str.split('&'))}
        return 'post', data


def code_generation(method: str, url: str,
                    data: dict, headers: dict, cookies: dict) -> str:
    """crawles 代码生成"""

    current_path = path.abspath(__file__)  # 绝对路径获取
    parent_dir = path.dirname(path.dirname(current_path))

    # 读取Jinja2模板
    with open(path.join(parent_dir, 'template', 'base_crawler.j2'),
              encoding='utf-8') as f:
        template = Template(f.read())

    args = 'data' if method == 'post' else 'params'

    return template.render(url=url, cookies=cookies,
                           headers=headers, args=args,
                           data=data, method=method, time=time())


def curl_analy(curl_str: str) -> str:
    """请求数据解析"""
    curl_str = curl_str.replace('^', '') \
        .replace('   -', ' \n   -') \
        .replace("'", '"')  # 预处理

    url, data = url_args_get(curl_str)  # 参数解析
    headers, cookies = headers_get(curl_str)
    method, data_dict = data_get(curl_str)

    data = {k: parse.unquote(v) for k, v in {**data, **data_dict}.items()}
    headers = {k: parse.unquote(v) for k, v in headers.items()}
    cookies = {k: parse.unquote(v) for k, v in cookies.items()}

    # 代码生成
    code_data = code_generation(method, url, data,
                                headers, cookies)
    return code_data


def curl_analysis(curl_str: str) -> None:
    """
    解析curl 直接转换为python代码
    @param curl_str:
    @return:
    """
    # 获取文件调用
    frame_info = stack()[1]
    filepath = frame_info[1]
    del frame_info

    filepath = path.abspath(filepath)

    # 数据解析
    code_data = curl_analy(curl_str)

    # 复写文件
    f = open(filepath, 'w+', encoding='utf-8')
    f.write(code_data)
    f.close()


if __name__ == '__main__':
    pass
    # curl_str = '...'  # 这里填入你的 curl 命令
    # code_dat = curl_analysis(curl_str)
    # print(code_dat)
