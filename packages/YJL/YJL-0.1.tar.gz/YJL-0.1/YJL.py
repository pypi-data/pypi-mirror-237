# coding: utf-8
# -*- coding: utf-8 -*-
import base64


def print_yjl():
    print("LiMeng Love YangJiaLing (2023/10/24)")

def encode_base64(string):
    byte = string.encode('utf-8')
    b64 = base64.b64encode(byte)
    result = b64.decode('utf-8')
    return result


def decode_base64(string):
    byte = string.encode('utf-8')
    b64 = base64.b64decode(byte)
    result = b64.decode('utf-8')
    return result


print_yjl()
