import urllib.parse

file = open('iRealJazz.txt', 'r')

jazz = urllib.parse.unquote(file.read()).split('===')



# Ain't Misbehavin'=Waller Fats
# Medium Swing=C
# 1r34LbKcu77-DZL4C6 A6CZL6-F 6FZLE/C7 6CZL7G 7-DZL7/E A74T{A*[B*] N1E7 ZL6-F 6C2NZL QXyQyX} 7G 7DZL7AC6 E7ZL7G G 7DZ|F7XyGZL7D 7-AZL7E G6|QyX7A|QyX7D|Q6 A7LQyX-A7-DZL[C6 A6CZL6-F 6FZLE/C7 6CZL7G 7-DZL7/E A7A*] 7 G7LZC6 A-7LZD-7 G7 Z
#                 C6                                                                                                                                                                                                 G7  C6 A-7  D-7 G7
# 0=0

# C6 A7 | D-7 F7 | C6/E A7 | D-7 G7



for standard in jazz:
    print(standard)