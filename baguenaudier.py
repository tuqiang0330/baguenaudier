#-*- encoding: utf-8 -*-

import sys
import os
import time

result = []

def up(n):
    result.append((n, 1))

def down(n):
    result.append((n, 0))

def up_all(n):
    # 安装n连环
    while n > 1:
        up_last(n - 1)
        up(n - 1)
        n -= 2
    if n == 1:
        up(0)

def down_all(n):
    # 卸载n连环
    if n == 1:
        down(0)
    elif n == 2:
        down(1)
        down(0)
    else:
        down_all(n - 2)
        down(n - 1)
        down_last(n - 1)

def up_last(n):
    # 在n连环没有任何环安装的情况下，安装最后一环
    if n == 1:
        up(0)
    else:
        up_last(n - 1)
        up(n - 1)
        down_last(n - 1)

def down_last(n):
    # 在n连环只有最后一环时，将最后一环卸载
    if n == 1:
        down(0)
    else:
        up_last(n - 1)
        down(n - 1)
        down_last(n - 1)

def string_result(n, init_char):
    result = []
    for i in range(0, n):
        result.append(init_char)
    def foo(x):
        if x[1] == 1:
            result[n - x[0] - 1] = '〇'
        else:
            result[n - x[0] - 1] = '——'
        return ''.join(result)
    return foo

def help():
    print('Usage: %s up/down n [-a]' % sys.argv[0])
    print('    up: 上n连环')
    print('    down: 下n连环')
    print('    n: n连环')
    print('    -a: 动画模式')


if __name__ == '__main__':
    if len(sys.argv) < 3:
        help()
        exit(1)
    if sys.argv[1] not in ['up', 'down']:
        help()
        exit(1)
    if not sys.argv[2].isdigit():
        help()
        exit(1)

    n = int(sys.argv[2])
    if (sys.argv[1] == 'up'):
        up_all(n)
        sr = string_result(n, '——')
    else:
        down_all(n)
        sr = string_result(n, '〇')

    if '-a' in sys.argv:
        line = ''.join(map(lambda x:'——', range(0, n)))
        for i in result:
            r = sr(i)
            os.system('clear')
            print(line)
            print(r.replace('——', '  '))
            print
            print
            print(r.replace('〇', '  ').replace('——', '〇'))
            print(line)
            time.sleep(0.7)
    else:
        for i in result:
            print(sr(i))
