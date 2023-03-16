def getText(text):
    text=text.lower()
    for ch in ",.;?-:\'":
        text=text.replace(ch,' ')
    return text

def wordFreq(text,topn):
    word=text.split()
    counts={}
    for word in word:
        counts[word]=counts.get(word,0)+1
    excludes={'the','and','to','of','a','be','it','is','not','but'}
    for word in excludes:
        del(counts[word])
    items=list(counts.items())
    items=sorted(items,key=lambda x:x[1],reverse=True)
    return items[:topn]

try:
    with open(r'hamlet.txt','r') as file:
        text=file.read()
        text=getText(text)
        freqs=wordFreq(text,10)

except IOError:
    print("文件不存在，请确认！\n")
else:
    try:
        with open("hamlet_词频统计.txt",'w') as fileFreq:
            items=[word+'\t'+str(freqs)+'\n' for word,freqs in freqs]
            fileFreq.writelines(items)
    except IOError:
        print("写入文件出错")
for word,freq in freqs:
    print("{:<10} {:>}".format(word,freq))