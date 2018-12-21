import json
import datetime
import pandas as pd
import matplotlib.pyplot as plt

### change the target filename to analyze ###
# filename = 'Facebook_analysis.txt'
### ------------------------------------- ###

# read target file name from the parameter.txt
with open('parameters.txt') as f:
    read_data = f.readline()
    read_data = f.readline()
    read_data = f.readline()
    filename = f.readline()

# open file and change it to json format
with open(filename) as f:
    read_data = f.read()
    str1 = read_data.replace("\'", "\"")
    j_data = json.loads(str1)

# use df_dict to store the result
df_dict = {'comments': [0, 0, 0], 'likes': [0, 0, 0]}

# calculate the total comments and likes at morning(0-8), afternoon(8-16), evening(16-24)
for article in j_data:
    # print(article)

    art_time = datetime.datetime.strptime( article['created_time'], '%Y-%m-%dT%H:%M:%S+%f')
    if art_time <= art_time.replace(hour=8, minute=0, second=0, microsecond=0):
        df_dict['comments'][0] += article['comments_count']
        df_dict['likes'][0] += article['likes_count']
    elif art_time > art_time.replace(hour=16, minute=0, second=0, microsecond=0):
        df_dict['comments'][2] += article['comments_count']
        df_dict['likes'][2] += article['likes_count']
    else:
        df_dict['comments'][1] += article['comments_count']
        df_dict['likes'][1] += article['likes_count']

# change type df_dict from dictionary to DataFrame
df = pd.DataFrame(df_dict, index=['morning', 'afternoon', 'evening'])
# plot the result
plot = df.plot(kind='barh')
# plt.show()
fig = plot.get_figure()
fig.savefig("Plot/output.png")
