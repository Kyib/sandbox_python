#! python3
# ownStripe.py - str.stripe メソッドを自作する

# 課題7.18.2

import sys
import re


def own_strip(string, sep_seq=''):
    if sep_seq == '':
        return re.sub(r'^\s+(.*)\s+$', r'\1', string)

    erase_group = '[' + sep_seq + ']'

    return re.sub(rf'^{erase_group}+(.*){erase_group}+$', r'\1', string)


print(own_strip("   asdgagwe    "))
print(own_strip("asdgagwe"))
print(own_strip("asdgagwe", "ase"))
