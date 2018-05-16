import sys
# print 'script name is', sys.argv[0]
# tmp = len(sys.argv)

# for each in range(1, tmp) :
#     print 'arv', each, sys.argv[each]

file_object = open('activitynames.txt', 'rU')
i = 0
for line in file_object:
    if (line.replace(' ', '').replace('\r', '').replace('\n', '') == ''):
        continue
    i += 1
    print i
    print line