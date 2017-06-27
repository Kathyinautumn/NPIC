# read file
import os
import struct


# from ctypes import *
# import numpy as np

    filepath = os.path.abspath('/Users/zhangqiushui/Desktop/1号机历史数据文件20170417/ANAHIST0.dat[SUCCESS]')
    f = open(filepath, 'rb')

    # search for certain bytes
    k = int(input("测点索引: "))
    f.seek(342368 + 600 * 5 * k)
    fs = f.read(600 * 5)

    f.close()

    data = bytearray(fs)

    desktop_path = '/Users/zhangqiushui/Desktop/'
    full_path = desktop_path + 'data' + str(k) + '.txt'
    file = open(full_path, 'w')

    file.writelines(str(k) + '\n')

    # reshape the data
    output = []
    for i in range(0, len(data), 5):
        b = data[i:i + 5]
        c = b[0:4]
        d = struct.unpack('f', c)[0]
        e = str(d)
        # output.append(e)
        # final_output = str(output)
        file.writelines(e + '\n')

    file.close()

# # create a txt file
# def txt_create(name, msg):
#     desktop_path = '/Users/zhangqiushui/Desktop/'
#     full_path = desktop_path + name + '.txt'
#     file = open(full_path, 'w')
#     file.writelines(msg)
#     file.close()

# txt_create('data' + str(k), str(k) + '\r\n' + final_output)
