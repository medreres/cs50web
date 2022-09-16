import re

from requests import head


def head1(line: str):
    pattern = re.compile(r'^\#\s(.*?)$\n', re.MULTILINE)
    replacement = r'<h1>\1</h1>\n'
    result = re.sub(pattern, replacement, line)
    return result


def head2(line: str):
    pattern = re.compile(r'^\#{2}\s(.*?)$', re.MULTILINE)
    replacement = r'<h2>\1</h2>'
    result = re.sub(pattern, replacement, line)
    return result


def head3(line: str):
    pattern = re.compile(r'^\#{3}\s(.*?)$', re.MULTILINE)
    replacement = r'<h3>\1</h3>'
    result = re.sub(pattern, replacement, line)
    return result


def heading(line: str):
    result = head1(line)
    result = head2(result)
    result = head3(result)
    return result


def bold(line: str):
    pattern = r'\*{2}(.*?)\*{2}'
    replacement = r'<strong>\1</strong>'
    result = re.sub(pattern, replacement, line)
    return result


def ul(line: str):
    # main list
    pattern = re.compile(r'^\*\s(.*?)$|^\-\s(.*?)$', re.MULTILINE)
    replacement = r'<li>\1</li>'
    result = re.sub(pattern, replacement, line)
    
    pattern = re.compile(r'\<li>([^\$]+)</li>', re.MULTILINE)
    replacement = r'<ul><li>\1</li></ul>'
    result = re.sub(pattern, replacement, result)
    print(result)

    # sub list
    pattern = re.compile(r'^\s{4}\*(.*?)\n|^\-\s(.*?)\n', re.MULTILINE)
    replacement = r'    <li>\1</li>'
    result = re.sub(pattern, replacement, result)
    print("NEW \n\n")
    print(result)


    # pattern = r'^\s{4}\<li>([^\s]+)</li>'
    # replacement = r'<ul><li>\1</li></ul>'
    # result = re.sub(pattern, replacement, result)
    return result


def link_tagged(line: str):
    pattern = r'\[(.*?)\]\((.*?)\)'
    replace = r'<a href=\2">\1</a>'
    result = re.sub(pattern, replace, line)
    return result


def link(line: str):
    pattern = r'\<(.*?)\>'
    replace = r'<a href=\1">\1</a>'
    result = re.sub(pattern, replace, line)
    return result


def paragraphs(line: str):
    pattern = re.compile(r'^\w(.*?)$\n')
    replace = r'<p>\1</p>'
    result = re.sub(pattern, replace, line)
    return result


def italic(line: str):
    pattern = re.compile(r'\*(.*?)\*')
    replace = r'<em>\1</em>'
    result = re.sub(pattern, replace, line)
    return result


def convert(result: str):
    # result = link(result)
    result = heading(result)
    result = bold(result)
    result = ul(result)
    result = link_tagged(result)
    result = paragraphs(result)
    result = italic(result)
    print(result)
    return result
