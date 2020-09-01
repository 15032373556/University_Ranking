import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as sci
import pandas_profiling as pp
from pylab import mpl
from sklearn.preprocessing import OneHotEncoder

mpl.rcParams['font.sans-serif'] = ['SimHei']  # 作图显示汉字
plt.rcParams['axes.unicode_minus'] = False    # 作图显示负号

# 不发出警告
import warnings
warnings.filterwarnings('ignore')

data = pd.read_csv(r'C:\Users\刘邦国\PycharmProjects\study\data_visual\csdn\2015年中国大学排名.csv')
data1 = data.drop(['人才培养得分','科学研究得分'],axis=1)  # 删除重复列
data2 = pd.read_csv(r'C:\Users\刘邦国\PycharmProjects\study\data_visual\csdn\2016年中国大学排名.csv')
data3 = pd.read_csv(r'C:\Users\刘邦国\PycharmProjects\study\data_visual\csdn\2017年中国大学排名.csv')
data4 = pd.read_csv(r'C:\Users\刘邦国\PycharmProjects\study\data_visual\csdn\2018年中国大学排名.csv')
data5 = pd.read_csv(r'C:\Users\刘邦国\PycharmProjects\study\data_visual\csdn\2019年中国大学排名.csv')
data6 = pd.read_csv(r'C:\Users\刘邦国\PycharmProjects\study\data_visual\csdn\2020年中国大学排名.csv')

# 2015年
'''
report1 = pp.ProfileReport(data1)  # 生成分析报告
report1.to_file('report1.html')
prov_score_mean = data1.groupby('省市')['总分'].mean().sort_values(ascending=False).to_frame().reset_index()
prov_university_count = data1.groupby('省市')['学校名称'].count().sort_values(ascending=False).to_frame().reset_index()

f, [ax1,ax2] = plt.subplots(2,1,figsize=(16,16))
sns.barplot(x='省市', y='总分', palette="Blues_d", data=prov_score_mean, ax=ax1)
ax1.set_title('各省市分数均值对比',fontsize=15)
ax1.set_xlabel('省市')
ax1.set_ylabel('分数均值')

sns.barplot(x='省市', y='学校名称', palette="Greens_d", data=prov_university_count, ax=ax2)
ax2.set_title('各省市学校数量对比',fontsize=15)
ax2.set_xlabel('省市')
ax2.set_ylabel('学校数量')

plt.savefig("2015.png",dpi=500,bbox_inches='tight')
plt.show()
'''
# 2016年
'''
# report2 = pp.ProfileReport(data2)
# report2.to_file('report2.html')
prov_score_mean = data2.groupby('省市')['总分'].mean().sort_values(ascending=False).to_frame().reset_index()
prov_university_count = data2.groupby('省市')['学校名称'].count().sort_values(ascending=False).to_frame().reset_index()

f, [ax1,ax2] = plt.subplots(2,1,figsize=(16,16))
sns.barplot(x='省市', y='总分', palette="Blues_d", data=prov_score_mean, ax=ax1)
ax1.set_title('各省市分数均值对比',fontsize=15)
ax1.set_xlabel('省市')
ax1.set_ylabel('分数均值')

sns.barplot(x='省市', y='学校名称', palette="Greens_d", data=prov_university_count, ax=ax2)
ax2.set_title('各省市学校数量对比',fontsize=15)
ax2.set_xlabel('省市')
ax2.set_ylabel('学校数量')

plt.savefig("2016.png",dpi=500,bbox_inches='tight')
plt.show()
'''

# 2017年
'''
# report3 = pp.ProfileReport(data3)
# report3.to_file('report3.html')
prov_score_mean = data3.groupby('省市')['总分'].mean().sort_values(ascending=False).to_frame().reset_index()
prov_university_count = data3.groupby('省市')['学校名称'].count().sort_values(ascending=False).to_frame().reset_index()

f1, [ax1,ax2] = plt.subplots(2,1,figsize=(16,16))
sns.barplot(x='省市', y='总分', palette="Blues_d", data=prov_score_mean, ax=ax1)
ax1.set_title('各省市分数均值对比',fontsize=15)
ax1.set_xlabel('省市')
ax1.set_ylabel('分数均值')

sns.barplot(x='省市', y='学校名称', palette="Greens_d", data=prov_university_count, ax=ax2)
ax2.set_title('各省市学校数量对比',fontsize=15)
ax2.set_xlabel('省市')
ax2.set_ylabel('学校数量')

plt.savefig("2017.png",dpi=500,bbox_inches='tight')
plt.show()
'''

# 2018年
'''
# report4 = pp.ProfileReport(data4)
# report4.to_file('report4.html')
prov_score_mean = data4.groupby('省市')['总分'].mean().sort_values(ascending=False).to_frame().reset_index()
prov_university_count = data4.groupby('省市')['学校名称'].count().sort_values(ascending=False).to_frame().reset_index()

f2, [ax1,ax2] = plt.subplots(2,1,figsize=(16,16))
sns.barplot(x='省市', y='总分', palette="Blues_d", data=prov_score_mean, ax=ax1)
ax1.set_title('各省市分数均值对比',fontsize=15)
ax1.set_xlabel('省市')
ax1.set_ylabel('分数均值')

sns.barplot(x='省市', y='学校名称', palette="Greens_d", data=prov_university_count, ax=ax2)
ax2.set_title('各省市学校数量对比',fontsize=15)
ax2.set_xlabel('省市')
ax2.set_ylabel('学校数量')

plt.savefig("2018.png",dpi=500,bbox_inches='tight')
plt.show()
'''

# 2019年
'''
# report5 = pp.ProfileReport(data5)
# report5.to_file('report5.html')
prov_score_mean = data5.groupby('省市')['总分'].mean().sort_values(ascending=False).to_frame().reset_index()
prov_university_count = data5.groupby('省市')['学校名称'].count().sort_values(ascending=False).to_frame().reset_index()

f3, [ax1,ax2] = plt.subplots(2,1,figsize=(16,16))
sns.barplot(x='省市', y='总分', palette="Blues_d", data=prov_score_mean, ax=ax1)
ax1.set_title('各省市分数均值对比',fontsize=15)
ax1.set_xlabel('省市')
ax1.set_ylabel('分数均值')

sns.barplot(x='省市', y='学校名称', palette="Greens_d", data=prov_university_count, ax=ax2)
ax2.set_title('各省市学校数量对比',fontsize=15)
ax2.set_xlabel('省市')
ax2.set_ylabel('学校数量')

plt.savefig("2019.png",dpi=500,bbox_inches='tight')
plt.show()
'''

# 2020年
'''
# report6 = pp.ProfileReport(data6)
# report6.to_file('report6.html')
prov_score_mean = data6.groupby('省市')['总分'].mean().sort_values(ascending=False).to_frame().reset_index()
prov_university_count = data6.groupby('省市')['学校名称'].count().sort_values(ascending=False).to_frame().reset_index()

f4, [ax1,ax2] = plt.subplots(2,1,figsize=(16,16))
sns.barplot(x='省市', y='总分', palette="Blues_d", data=prov_score_mean, ax=ax1)
ax1.set_title('各省市分数均值对比',fontsize=15)
ax1.set_xlabel('省市')
ax1.set_ylabel('分数均值')

sns.barplot(x='省市', y='学校名称', palette="Greens_d", data=prov_university_count, ax=ax2)
ax2.set_title('各省市学校数量对比',fontsize=15)
ax2.set_xlabel('省市')
ax2.set_ylabel('学校数量')

plt.savefig("2020.png",dpi=500,bbox_inches='tight')
plt.show()
'''

# 根据2020年数据分析学校类型
'''
style_score_mean = data6.groupby('学校类型')['总分'].mean().sort_values(ascending=False).to_frame().reset_index()

f4, [ax1,ax2] = plt.subplots(1,2,figsize=(20,10))

sns.barplot(x='学校类型', y='总分', data=style_score_mean, ax=ax1)
ax1.set_title('各类学校分数均值对比',fontsize=20)
ax1.set_xlabel('学校类型',fontsize=18)
ax1.set_ylabel('分数均值',fontsize=18)

sns.countplot(x='学校类型',data=data6, palette='magma',ax=ax2)
ax2.set_title('各类学校数量对比',fontsize=20)
ax2.set_xlabel('学校类型',fontsize=18)
ax2.set_ylabel('学校数量',fontsize=18)
plt.tight_layout(pad=1)
plt.savefig("style.png",dpi=500,bbox_inches='tight')
plt.show()

# sns.boxplot(x='学校类型', y='总分', data=data6,width=0.8,palette='hls',
#             order={'综合','理工','师范','农业','林业'},  # 筛选类别
#             )
# sns.swarmplot(x='学校类型', y='总分', data=data6, color='k',size=3, alpha=0.8)
# plt.title('各类学校分布',fontsize=20)
# plt.show()

data6.sort_values(by='总分',inplace=True,ascending=False)
data6_1 = data6[['学校名称','省市','学校类型','总分']]
data6_2 = data6_1[(data6_1['学校类型']=='综合')][['学校名称','省市','总分']][:5]
# print(data6_2)
data6_3 = data6_1[(data6_1['学校类型']=='理工')][['学校名称','省市','总分']][:5]
# print(data6_3)
data6_4 = data6_1[(data6_1['学校类型']=='师范')][['学校名称','省市','总分']][:5]
# print(data6_4)
data6_5 = data6_1[(data6_1['学校类型']=='农业')][['学校名称','省市','总分']][:5]
# print(data6_5)
data6_6 = data6_1[(data6_1['学校类型']=='林业')][['学校名称','省市','总分']][:5]
# print(data6_6)

def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        plt.text(rect.get_x()+rect.get_width()/2.- 0.2, 1.03*height, '%s' % int(height))

plt.figure()
plt.subplot(3,2,1)
autolabel(plt.bar(range(len(data6_2['学校名称'])), data6_2['总分'], color='rgbcm', tick_label=data6_2['学校名称']))
plt.title('综合',fontsize=14)
plt.xticks(rotation=30)
plt.subplot(3,2,2)
autolabel(plt.bar(range(len(data6_3['学校名称'])), data6_3['总分'], color='rgbcm', tick_label=data6_3['学校名称']))
plt.title('理工',fontsize=14)
plt.xticks(rotation=30)
plt.subplot(3,2,3)
autolabel(plt.bar(range(len(data6_4['学校名称'])), data6_4['总分'], color='rgbcm', tick_label=data6_4['学校名称']))
plt.title('师范',fontsize=14)
plt.xticks(rotation=30)
plt.subplot(3,2,4)
autolabel(plt.bar(range(len(data6_5['学校名称'])), data6_5['总分'], color='rgbcm', tick_label=data6_5['学校名称']))
plt.title('农业',fontsize=14)
plt.xticks(rotation=30)
plt.subplot(3,2,5)
autolabel(plt.bar(range(len(data6_6['学校名称'])), data6_6['总分'], color='rgbcm', tick_label=data6_6['学校名称']))
plt.title('林业',fontsize=14)
plt.xticks(rotation=30)
plt.show()
'''

# 国际竞争力排名前十学校
'''
data6.sort_values(by='国际竞争力得分',inplace=True,ascending=False)
data6_1 = data6[:10]
print(data6_1)


def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        plt.text(rect.get_x()+rect.get_width()/2.- 0.2, 1.03*height, '%s' % int(height))

plt.figure()
autolabel(plt.bar(range(len(data6_1['学校名称'])), data6_1['国际竞争力得分'], color='rgbcm', tick_label=data6_1['学校名称']))
plt.title('国际竞争力得分排名前十的学校',fontsize=14)
plt.xticks(rotation=30)
plt.show()

'''

# 科研质量排名前十学校
'''
data6.sort_values(by='科学研究得分',inplace=True,ascending=False)
data6_1 = data6[:10]
print(data6_1)


def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        plt.text(rect.get_x()+rect.get_width()/2.- 0.2, 1.03*height, '%s' % int(height))

plt.figure()
autolabel(plt.bar(range(len(data6_1['学校名称'])), data6_1['科学研究得分'], color='rgbcm', tick_label=data6_1['学校名称']))
plt.title('科学研究得分排名前十的学校',fontsize=14)
plt.xticks(rotation=30)
plt.show()
'''

# 人才培养得分排名前十学校
'''
data6.sort_values(by='人才培养得分',inplace=True,ascending=False)
data6_1 = data6[:10]
print(data6_1)


def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        plt.text(rect.get_x()+rect.get_width()/2.- 0.2, 1.03*height, '%s' % int(height))

plt.figure()
autolabel(plt.bar(range(len(data6_1['学校名称'])), data6_1['人才培养得分'], color='rgbcm', tick_label=data6_1['学校名称']))
plt.title('人才培养得分排名前十的学校',fontsize=14)
plt.xticks(rotation=30)
plt.show()
'''
# 学科水平得分排名前十学校
data6.sort_values(by='学科水平得分',inplace=True,ascending=False)
data6_1 = data6[:10]
print(data6_1)


def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        plt.text(rect.get_x()+rect.get_width()/2.- 0.2, 1.03*height, '%s' % int(height))

plt.figure()
autolabel(plt.bar(range(len(data6_1['学校名称'])), data6_1['学科水平得分'], color='rgbcm', tick_label=data6_1['学校名称']))
plt.title('学科水平得分排名前十的学校',fontsize=14)
plt.xticks(rotation=30)
plt.show()