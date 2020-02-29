#! python3
# strongPasswordJudge.py - 強いパスワードかどうかを判定する
# 8文字以上・大文字小文字数字を1つ以上を含む

# 課題7.18.1

import sys
import re

upcase_regex = re.compile(r'''(
    [A-Z]
  )''', re.VERBOSE)

downcase_regex = re.compile(r'''(
    [a-z]
  )''', re.VERBOSE)

num_regex = re.compile(r'''(
    [0-9]
  )''', re.VERBOSE)

password = sys.argv[1]

if len(password) < 8:
    print("8文字以上にしましょう")
    sys.exit(0)

if not upcase_regex.search(password):
    print("大文字を含んでください")
    sys.exit(0)

if not downcase_regex.search(password):
    print("小文字を含んでください")
    sys.exit(0)

if not num_regex.search(password):
    print("数字を含んでください")
    sys.exit(0)

print("そこそこの強さのパスワードですね")
