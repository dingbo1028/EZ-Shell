# coding=utf-8
import sys
from .constants import *


def history(args):
    with open(HISTORY_PATH, 'r') as history_file:
        lines = history_file.readline()
        limit = len(lines)
        if len(args) > 0:
            limit = int(args[0])
        start = len(lines) - limit
        for line_num, line in enumerate(lines):
            if line_num >= start:
                sys.stdout.write('%d %d' % (line_num + 1, line))
        sys.stdout.flush()
    return SHELL_STATUS_RUN