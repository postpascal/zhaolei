import jieba
from wordcloud import WordCloud
import image
import pandas
import numpy as np
import matplotlib.pyplot as plt
from wordcloud import WordCloud,ImageColorGenerator
from os import listdir
from os.path import isfile, join

lyrics = [f for f in listdir("lyric") if isfile(join("lyric", f))]
content=[]
for lyric in lyrics:
    for line in open("lyric/"+lyric,'r'):
        content.append(line)

text=""
for i in content:
    text=text+i
segs=jieba.cut(text)
segment = []
for seg in segs:
    if len(seg) > 1 and seg!='\r\n' and seg not in ["我会","没有","一样","何必","只有","一切","知道","北京","我们","一个","妈妈","已经","如果","什么","那些","只是","不会","无法","小屋"]:
        segment.append(seg)
# print(segment)
print(len(segment))
#去停用词
words_df=pandas.DataFrame({'segment':segment})
words_df.head()

words_stat=words_df.groupby(by=['segment'])['segment'].agg({"number":np.size})
words_stat=words_stat.reset_index().sort_values(by="number",ascending=False)


from scipy.misc import imread
import matplotlib.pyplot as plt
from wordcloud import WordCloud,ImageColorGenerator
bimg=imread('caihong.jpg')
wordcloud=WordCloud(background_color="black",mask=bimg,font_path='msyh.ttf')
wordcloud=wordcloud.fit_words(words_stat.head(39769).itertuples(index=False))
bimgColors=ImageColorGenerator(bimg)
plt.figure(figsize=(20,15))
plt.axis("off")
plt.imshow(wordcloud.recolor(color_func=bimgColors))
plt.show()
