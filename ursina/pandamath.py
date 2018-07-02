
import operator
# from math import cos, sin, sqrt, hypot
from panda3d.core import NodePath, Point3
# from ursina.entity import Entity

def distance(a, b):
    p0 = NodePath('p0')
    p1 = NodePath('p1')
    # if str(type(a).__name__) == 'Entity':
    p0.setPos(Point3(a.x, a.y, a.z))
    p1.setPos(Point3(b.x, b.y, b.z))
    dist = p0.getDistance(p1)
    # print('DISTACNE:.....', dist)
    return dist


def lerp(a, b, t):
    return a + (b - a) * t

def inverselerp(a, b, t) :
    return (a - b) / (t - b)

def clamp(value, floor, ceiling):
    return max(min(value, ceiling), floor)

def count_lines(file):
    all_lines = 0
    blank_lines = 0
    comment_lines = 0
    used_lines = 0

    with open(file) as f:
        for line in f:
            all_lines += 1

            if len(line.strip()) == 0:
                blank_lines += 1

            if line.strip().startswith('#'):
                comment_lines += 1
    print('all_lines:', all_lines)
    print('blank_lines:', blank_lines)
    print('comment_lines:', comment_lines)
    print('used_lines:', all_lines - blank_lines - comment_lines)
    return all_lines

def chunk_list(l, chunk_size):
    # yield successive chunks from list
    for i in range(0, len(l), chunk_size):
        yield l[i:i + chunk_size]

def size_list():
    #return a list of current python objects sorted by size
    globals_list = list()
    globals_list.clear()
    for e in globals():
        # object, size
        globals_list.append([e, sys.getsizeof(e)])
    globals_list.sort(key=operator.itemgetter(1), reverse=True)
    print('scene size:', globals_list)