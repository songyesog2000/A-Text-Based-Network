import textdistance
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import json
from itertools import combinations
from pyvis.network import Network


if __name__ == '__main__':
    # reading the data
    with open('profile_list.json') as json_file:
        profile_list = json.load(json_file)

    tics = list(profile_list.keys())

    G = Network(height="750px", width="100%", bgcolor="#222222", font_color="white")
    G.barnes_hut()
    G.add_nodes(tics)

    tics_comb = combinations(tics, 2)

    # pandas dataframe for the similarity matrix
    M = pd.DataFrame(index=tics, columns=tics)
    W = pd.DataFrame(index=tics, columns=tics)
    for _ in tics_comb:
        d = textdistance.jaro.distance(profile_list[_[0]],
                                        profile_list[_[1]])
        M[_[1]][_[0]] = M[_[0]][_[1]] = d
        if d > 0.25:
            s = 0.0
        else:
            s = np.log(d) / np.log(1 - d)
            G.add_edge(_[0], _[1], weight=s)

        W[_[1]][_[0]] = W[_[0]][_[1]] = s

    for _ in tics:
        W[_][_]=0.0

    G.show("G.html")
    print('done')


