from d2l import mxnet as d2l
from mxnet import gluon, np
import os
import pandas as pd

#@save
# d2l.DATA_HUB['ml-100k'] = (
#     'http://files.grouplens.org/datasets/movielens/ml-100k.zip',
#     'cd4dcac4241c8a4ad7badc7ca635da8a69dddb83')

#@read information data of u.data
def read_data_ml100k():
    data_dir = "/home/datdinh/Desktop/thuctap/Recommendation-System/data/ml-100k"
    names = ['user_id', 'item_id', 'rating', 'timestamp']
    data = pd.read_csv(os.path.join(data_dir, 'u.data'), '\t', names=names,
                       engine='python')
    num_users = data.user_id.unique().shape[0]
    num_items = data.item_id.unique().shape[0]
    return data, num_users, num_items

data, num_users, num_items = read_data_ml100k()
sparsity = 1 - len(data) / (num_users * num_items)
print(f'number of users: {num_users}, number of items: {num_items}')
print(f'matrix sparsity: {sparsity:f}')
print(data.head(5))

d2l.plt.hist(data['rating'], bins=5, ec='black')
d2l.plt.xlabel('Rating')
d2l.plt.ylabel('Count')
d2l.plt.title('Distribution of Ratings in MovieLens 100K')
d2l.plt.show()