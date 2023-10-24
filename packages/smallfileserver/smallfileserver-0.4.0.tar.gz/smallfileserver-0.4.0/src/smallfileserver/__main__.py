#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys
import argparse

from .fileserver import runserver

from .versions import version


if __name__ == '__main__':

    # 创建解析器
    parser = argparse.ArgumentParser(description='这是一个简单的文件服务器，支持文件下载与文件上传')

    # 添加命令行参数
    parser.add_argument('-p', '--port', type=int, required=False, default="8001", help='默认服务的端口')
    parser.add_argument('-ip', '--ip', type=str, required=False, default="0.0.0.0", help='默认的服务的IP')
    parser.add_argument('-v', '--verbose', action='store_true', help='当前软件的版本')

    # 解析命令行参数
    args = parser.parse_args()

    if args.verbose:
        print("Version is", version)
        exit(0)

    runserver(args.ip, args.port)
