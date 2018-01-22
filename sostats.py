import stackexchange
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
import matplotlib.cm as cm
#from matplotlib import rcParams

import numpy as np
import math
import seaborn as sns

# Set default Seaborn style
sns.set()

#Connect to SO site
so = stackexchange.Site(stackexchange.StackOverflow)

#Initialize lists to hold  values
tag_num = 10
tag_name = list()
tag_count = list()
tag_rank = list()

#get required values from SO object
for  idx, tag in enumerate(so.tags()):
    if idx >= tag_num:
        break    
    tag_rank.append(idx+1)
    tag_name.append(tag.name)
    tag_count.append(tag.count)
    
#Choose some random colors
colors=cm.rainbow(np.random.rand(2 * tag_num))

#Set bubble size
bubble_size = [int(i / np.std(tag_count)*500) for i in tag_count]


def millions(x, pos):
    'The two args are the value and tick position'
    if len(str(x)) <=8 :
        return '%1.1fK' % (x*1e-3)
    
    return '%1.1fM' % (x*1e-6)

formatter = FuncFormatter(millions)

#create scatter plot

fig, ax = plt.subplots()
ax.yaxis.set_major_formatter(formatter)
ax.scatter(tag_rank,tag_count,s=bubble_size,marker='o', color=colors)

#label each bubble
for n,c,r,s in zip(tag_name,tag_count,tag_rank,bubble_size):
    plt.annotate("#{}".format(r),xy=(r, c), ha="center", va="center")
    plt.annotate(n ,xy=(r, c), xytext=(0,np.sqrt(s)/2.+5), 
                textcoords="offset points", ha="center", va="bottom")

#increase x, y axis limit 10% more
ymin = ax.get_ylim()[0]
ymax = ax.get_ylim()[1]
plt.ylim(ymin, 1.10 * ymax)

# Setfont dictionaries for plot title and axis titles
title_font = {'fontname':'Arial', 'size':'16', 'color':'black', 'weight':'normal',
              'verticalalignment':'bottom'} 
axis_font = {'fontname':'Arial', 'size':'14'}


#Label axis
plt.ylabel('Tag Count', **axis_font)
plt.xlabel('Tag Rank', **axis_font)
plt.title('Top Ten Tags By Counts', **title_font)
plt.show()
