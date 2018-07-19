#coding:utf8
'''
Created on 2017年10月24日

@author: Administrator
'''
# eg. 7-20检查Word文档的连续重复字
filename = r'D:\Python\codes\python3\Test\Threading.doc'
word = client.Dispatch('Word.Application')
doc = word.Documents.Open(filename)
content = str(doc.Content)
doc.Close()
word.Quit()

repeatedWords = []

lens = len(content)
for i in range(lens-2):
    ch = content[i]
    ch1 = content[i+1]
    ch2 = content[i+2]
    if u'\u4e00' <= ch <= u'\u9fa5' or ch in (',', '.', '、'):
        if ch == ch1 and ch+ch1 not in repeatedWords:
            print(ch + ch1)
            repeatedWords.append(ch+ch1)
        elif ch == ch2 and ch+ch1+ch2 not in repeatedWords:
            print(ch+ch1+ch2)
            repeatedWords.append(ch+ch1+ch2)
print('\n')