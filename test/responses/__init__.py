import os

from scrapy.http import HtmlResponse, Request

def fake_response_from_file(file_name, url=None):
    if not url:
        url = 'http://www.example.com'

    request = Request(url=url)

    if not file_name[0] == '/':
        responses_dir = os.path.dirname((os.path.realpath(__file__)))
        file_path = os.path.join(responses_dir + file_name)
    else:
        file_path = 'test/responses' + file_name

    file_content = open(file_path, 'r', encoding='utf-8').read()
    response = HtmlResponse(url=url, request=request, body=file_content, encoding='utf-8')
    return response
