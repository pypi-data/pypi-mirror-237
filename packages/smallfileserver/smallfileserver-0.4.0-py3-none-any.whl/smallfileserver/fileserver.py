#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""Simple HTTP Server With Upload.
This module builds on BaseHTTPServer by implementing the standard GET
and HEAD requests in a fairly straightforward manner.
"""

__version__ = "0.4.0"
__author__ = "whghcyx@outlook.com"
__all__ = ["SimpleHTTPRequestHandler"]

import os
import sys
import argparse
import posixpath
try:
    from html import escape
except ImportError:
    from cgi import escape
import shutil
import mimetypes
import re
import signal
from io import StringIO, BytesIO

if sys.version_info.major == 3:
    # Python3
    from urllib.parse import quote
    from urllib.parse import unquote
    from http.server import HTTPServer
    from http.server import BaseHTTPRequestHandler
else:
    # Python2
    reload(sys)
    sys.setdefaultencoding('utf-8')
    from urllib import quote
    from urllib import unquote
    from BaseHTTPServer import HTTPServer
    from BaseHTTPServer import BaseHTTPRequestHandler


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    """Simple HTTP request handler with GET/HEAD/POST commands.
    This serves files from the current directory and any of its
    subdirectories.  The MIME type for files is determined by
    calling the .guess_type() method. And can receive file uploaded
    by client.
    The GET/HEAD/POST requests are identical except that the HEAD
    request omits the actual contents of the file.
    """

    server_version = "simple_http_server/" + __version__

    def do_GET(self):
        """提供GET请求"""
        fd = self.send_head()
        if fd:
            shutil.copyfileobj(fd, self.wfile)
            fd.close()

    def do_HEAD(self):
        """提供HEAD请求"""
        fd = self.send_head()
        if fd:
            fd.close()

    def do_POST(self):
        """提供POST请求"""
        r, info = self.deal_post_data()
        print(r, info, "by: ", self.client_address)
        f = BytesIO()
        message = ""
        message += """
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
<html>
    <head>
        <title>上传结果</title>
        <style>
            <style>
                *{
                    color: #6e5ed9
                }
                hr {
                    color: #555555;
                    background-color: #555555;
                    height: 2px;
                    border: none;
                }
                body {
                    font-size:120%;
                    background-color: #E6E6F5
                    
                }
                input {
                    font-size:120%;
                    background-color: #E6E6F5
                    color: #6e5ed9
                }
                input[type="file"] {
                    font-size:120%;
                    background-color: #E6E6F5
                    color: #6e5ed9
                }
                button {
                    font-size:120%;
                    background-color: #4B637F
                }
                a{
                    color: #d96e5e
                }
            </style>
        </style>
    </head>
    <body>
        <h2>上传结果：</h2>
        <hr>
        """
        f.write(bytes(message, "utf-8"))
        # f.write(b'')
        # f.write(b"<html>\n<title>Upload Result Page</title>\n")
        # f.write(b"<body>\n<h2>Upload Result Page</h2>\n")
        # f.write(b"<hr>\n")
        if r:
            f.write(bytes("<strong>成功: </strong>", "utf-8"))
        else:
            f.write(bytes("<strong>失败: </strong>", "utf-8"))
        f.write(info.encode('utf-8'))
        f.write(bytes("<br><br><a href=\".\">返回</a><br>", "utf-8"))
        f.write(b"<hr><small>Powered By: OSmile, check new version at ")
        f.write(b"<a href=\"https://github.com/WHG555/smallfileserver\">")
        f.write(b"here</a>.</small></body>\n</html>\n")
        length = f.tell()
        f.seek(0)
        self.send_response(200)
        self.send_header("Content-type", "text/html;charset=utf-8")
        self.send_header("Content-Length", str(length))
        self.end_headers()
        if f:
            shutil.copyfileobj(f, self.wfile)
            f.close()

    def deal_post_data(self):
        boundary = self.headers["Content-Type"].split("=")[1].encode('utf-8')
        remain_bytes = int(self.headers['content-length'])
        line = self.rfile.readline()
        remain_bytes -= len(line)
        if boundary not in line:
            return False, "Content NOT begin with boundary"
        line = self.rfile.readline()
        remain_bytes -= len(line)
        fn = re.findall(r'Content-Disposition.*name="file"; filename="(.*)"', line.decode('utf-8'))
        if not fn:
            return False, "Can't find out file name..."
        path = translate_path(self.path)
        fn = os.path.join(path, fn[0])
        while os.path.exists(fn):
            fn += "_"
        line = self.rfile.readline()
        remain_bytes -= len(line)
        line = self.rfile.readline()
        remain_bytes -= len(line)
        try:
            out = open(fn, 'wb')
        except IOError:
            return False, "无法创建要写入的文件，您有写入权限吗？"

        pre_line = self.rfile.readline()
        remain_bytes -= len(pre_line)
        while remain_bytes > 0:
            line = self.rfile.readline()
            remain_bytes -= len(line)
            if boundary in line:
                pre_line = pre_line[0:-1]
                if pre_line.endswith(b'\r'):
                    pre_line = pre_line[0:-1]
                out.write(pre_line)
                out.close()
                return True, "File '%s' 上传成功！！！" % fn
            else:
                out.write(pre_line)
                pre_line = line
        return False, "Unexpect Ends of data."

    def send_head(self):
        """GET 和 HEAD 命令的通用代码。

        这会发送响应代码和 MIME 标头。

        返回值是一个文件对象（必须复制
        除非命令是 HEAD，否则由调用者发送到输出文件，
        并且在任何情况下都必须由调用者关闭），或者
        无，在这种情况下调用者无需执行任何操作。
        """
        path = translate_path(self.path)
        if os.path.isdir(path):
            if not self.path.endswith('/'):
                # 重定向浏览器-基本上和apache一样
                self.send_response(301)
                self.send_header("Location", self.path + "/")
                self.end_headers()
                return None
            for index in "index.html", "index.htm":
                index = os.path.join(path, index)
                if os.path.exists(index):
                    path = index
                    break
            else:
                return self.list_directory(path)
        content_type = self.guess_type(path)
        try:
            # 始终以二进制模式读取。以文本模式打开文件可能会导致
            # 换行翻译，使内容的实际大小
            # 传输的内容*小于*内容长度！
            f = open(path, 'rb')
        except IOError:
            self.send_error(404, "File not found")
            return None
        self.send_response(200)
        self.send_header("Content-type", content_type)
        fs = os.fstat(f.fileno())
        self.send_header("Content-Length", str(fs[6]))
        self.send_header("Last-Modified", self.date_time_string(fs.st_mtime))
        self.end_headers()
        return f

    def list_directory(self, path):
        """帮助生成目录列表（缺少index.html）。

        返回值可以是文件对象，也可以是 None（表示
        错误）。无论哪种情况，都会发送标头，从而使
        接口与 send_head() 相同。
        """
        try:
            list_dir = os.listdir(path)
        except os.error:
            self.send_error(404, "No permission to list directory")
            return None
        list_dir.sort(key=lambda a: a.lower())
        f = BytesIO()
        display_path = escape(unquote(self.path))
        message = ""
        message += """
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
<html>
    <head>
        <meta charset="UTF-8">
        <title>文件分享</title>
            <style>
                *{
                    color: #6e5ed9
                }
                hr {
                    color: #555555;
                    background-color: #555555;
                    height: 2px;
                    border: none;
                }
                body {
                    font-size:120%;
                    background-color: #E6E6F5
                    
                }
                input {
                    font-size:120%;
                    background-color: #E6E6F5
                    color: #6e5ed9
                }
                input[type="file"] {
                    font-size:120%;
                    background-color: #E6E6F5
                    color: #6e5ed9
                }
                button {
                    font-size:120%;
                    background-color: #4B637F
                }
                a{
                    color: #d96e5e
                }
            </style>

    </head>
    <body>
        <h2>文件上传</h2>
        <form ENCTYPE="multipart/form-data" method="post">
            <input name="file" type="file"/>
            <input type="submit" value="上传"/>
        </form>
        <hr>
        <h2>文件下载</h2>
        <ul>
        <p><a href=\".\">主目录</a></p>
        """
        f.write(bytes(message, "utf-8"))
        f.write(bytes("<body>\n<h3>当前目录： %s</h3>\n" % display_path, "utf-8"))

        # f.write(b'')
        # f.write(b"\n" % display_path.encode('utf-8'))
        # f.write(bytes("<body>\n<h2>当前目录： %s</h2>\n" % display_path, "utf-8"))
        # f.write(b"<hr>\n")
        # f.write(b"<form ENCTYPE=\"multipart/form-data\" method=\"post\">")
        # f.write(b"<input name=\"file\" type=\"file\"/>")
        # f.write(b"<input type=\"submit\" value=\"upload\"/></form>\n")
        # f.write(b"<hr>\n<ul>\n")
        for name in list_dir:
            fullname = os.path.join(path, name)
            display_name = linkname = name
            # Append / for directories or @ for symbolic links
            if os.path.isdir(fullname):
                display_name = name + "/"
                linkname = name + "/"
            if os.path.islink(fullname):
                display_name = name + "@"
                # Note: a link to a directory displays with @ and links with /
            f.write(b'<li><a href="%s">%s</a>\n' % (quote(linkname).encode('utf-8'), escape(display_name).encode('utf-8')))
        f.write(b"</ul>\n<hr>\n</body>\n</html>\n")
        length = f.tell()
        f.seek(0)
        self.send_response(200)
        self.send_header("Content-type", "text/html;charset=utf-8")
        self.send_header("Content-Length", str(length))
        self.end_headers()
        return f

    def guess_type(self, path):
        """猜测文件的类型。

        参数是 PATH（文件名）。

        返回值是类型/子类型形式的字符串，
        可用于 MIME 内容类型标头。

        默认实现查看文件的扩展名
        在表 self.extensions_map 中，使用 application/octet-stream
        作为默认值；但是这是允许的（如果
        慢）查看数据内部以做出更好的猜测。

        """

        base, ext = posixpath.splitext(path)
        if ext in self.extensions_map:
            return self.extensions_map[ext]
        ext = ext.lower()
        if ext in self.extensions_map:
            return self.extensions_map[ext]
        else:
            return self.extensions_map['']

    if not mimetypes.inited:
        mimetypes.init()  # try to read system mime.types
    extensions_map = mimetypes.types_map.copy()
    extensions_map.update({
        '': 'application/octet-stream',  # Default
        '.py': 'text/plain',
        '.c': 'text/plain',
        '.h': 'text/plain',
    })


def translate_path(path):
    """Translate a /-separated PATH to the local filename syntax.
    Components that mean special things to the local file system
    (e.g. drive or directory names) are ignored.  (XXX They should
    probably be diagnosed.)
    """
    # abandon query parameters
    path = path.split('?', 1)[0]
    path = path.split('#', 1)[0]
    path = posixpath.normpath(unquote(path))
    words = path.split('/')
    words = filter(None, words)
    path = os.getcwd()
    for word in words:
        drive, word = os.path.splitdrive(word)
        head, word = os.path.split(word)
        if word in (os.curdir, os.pardir):
            continue
        path = os.path.join(path, word)
    return path


def signal_handler(signal, frame):
    print("You choose to stop me.")
    exit()


def runserver(ip="", port=8000):
    server_address = (ip, port)
    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)
    httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
    server = httpd.socket.getsockname()
    print("server_version: " + SimpleHTTPRequestHandler.server_version + ", python_version: " + SimpleHTTPRequestHandler.sys_version)
    print("sys encoding: " + sys.getdefaultencoding())
    print("Serving http on: " + str(server[0]) + ", port: " + str(server[1]) + " ... (http://" + server[0] + ":" + str(server[1]) + "/)")
    httpd.serve_forever()

if __name__ == '__main__':
    runserver()
