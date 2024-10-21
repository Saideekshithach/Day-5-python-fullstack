Python 3.11.9 (tags/v3.11.9:de54cf5, Apr  2 2024, 10:12:12) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a="I am learning python"
a[-15:-10]
'learn'
a[-18:-16]
'am'
a[-6:]
'python'
a="Now i am in class"
a[:-14]
'Now'
a[-5:]
'class'
a="Time is very precious"
a[-13:-9]
'very'
a[-21:-17]
'Time'
a[-8:]
'precious'
#striding
a="Data Science"
a[::]
'Data Science'
a[::1]
'Data Science'
a[::2]
'Dt cec'
a[::3]
'Dacn'
a="Machine learning"
a[::7]
'M n'
a[::9]
'Me'
a[::6]
'Men'
a[3:9]
'hine l'
a[5:]
'ne learning'
a[:9]
'Machine l'
a[7:12]
' lear'
a="Python course"
>>> a[1:9:4]
'yn'
>>> a[1:9:3]
'yoc'
>>> a[2:12:4]
't r'
>>> a[4:10:1]
'on cou'
>>> a[3:9:2]
'hnc'
>>> a="Data Science"
>>> a[-3:-14:-3]
'ncaD'
>>> a="Data Structure"
>>> a[-3:-14:-3]
'uuSt'
>>> a[-4:-12:-4]
'tt'
>>> a[-2:-11:-6]
'rt'
>>> a[-1:-7:-3]
'et'
>>> a="Python course"
>>> a[5:3:2]
''
>>> a[::-1]
'esruoc nohtyP'
>>> a[-8:-5:-2]
''
>>> a[5:3]
''
>>> #here in positive striding highest to lowest is not possible.so if we do it gives empty string
>>> #here in negative striding lowest to highest is not possible.so if we do it gives empty string.
