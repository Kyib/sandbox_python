#! python3
# phoneAndEmail.py - クリップボードから電話番号とメアドを検索する

import sys
import re
import pyperclip

# 電話番号の正規表現
phone_regex = re.compile(r'''(
  (\d{1,4}|\(\d{1,4}\))           # 市外局番 ()付きまでサポート
  (\s|-)                          # 区切り
  (\d{1,4})                       # 市内局番
  (\s|-)                          # 区切り
  (\d{3,4})                       # 加入者番号
  (\s*(ext|x|ext.)\s*(\d{2,5}))?  # あれば内線番号 判定は ext か x か ext.
  )''', re.VERBOSE)

# メールアドレスの正規表現
email_regex = re.compile(r'''(
  [a-zA-Z0-9._%+-]+             # ユーザ名
  @                             # 区切り
  [a-zA-Z0-9.-]+                # ドメイン名（.前）
  (\.[a-zA-Z]{2,4})             # ドメイン名（.後）
  )''', re.VERBOSE)

# クリップボードのテキストを取得する
text = str(pyperclip.paste())

matches = []  # 一致した電話番号とメアドを格納

# テキストを正規表現で検索する
for groups in phone_regex.findall(text):
    phone_num = '-'.join([groups[1], groups[3], groups[5]])  # セパレータを切って統一
    if groups[8] != '':
        phone_num += ' x' + groups[8]
    matches.append(phone_num)

for groups in email_regex.findall(text):
    matches.append(groups[0])

# 検索結果をクリップボードに貼り付ける
if len(matches) <= 0:
    print('電話番号やメールアドレスは見つかりませんでした')
    sys.exit(0)

pyperclip.copy('/n'.join(matches))
print('クリップボードにコピーしました')
print('/n'.join(matches))
