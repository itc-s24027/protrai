# s24027
# 現在の時刻と2024年6月のカレンダーを表示するプログラム

import calendar
import datetime

import calendar as cal
print(cal.month(2024,6))

now = datetime.datetime.now()
print(now.strftime("%Y年%m月%d日 %H:%H:%S"))
