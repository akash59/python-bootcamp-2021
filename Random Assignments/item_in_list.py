ll = ['From Data Source and Snapshot', 'From Data Sourc e only']
a = all(x in ll for x in ['From Data Source and Snapshot', 'From Data Source only'])
print(a)


lst = ['a', 'b', 'c', 'd', 'e', 'f']
d ={}
fd = []

# for index, l in enumerate(lst):
#     print(str(index) + " - " + l)
#     d['1']=lst[index]
#     d['2']=lst[index + 1]
#     d['3']=lst[index + 2]
#     print(d)

# print(d)

file_names = ['FEB~ITF@REPORT.docx', 'a.txt', 'b.txt', 'c.txt', 'FEB~ITF@REPORT.docx', 'FEB~ITF@REPORT.docx']
file_sizes = ['11KB', '12KB', '30MB', '40MB', '50MB', '40MB']
for index, file in enumerate(file_names):
    d = {}
    d['File Name'] = file
    d['File Size'] = file_sizes[index]
    fd.append(d)
    d = {}
print(fd)


res = None
for sub in fd:
    if sub['File Name'] == 'c.txt':
        res = sub
        break

print(res)


