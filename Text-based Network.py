import textdistance
import pandas as pd
import numpy as np
import json
from itertools import combinations
from pyvis.network import Network
from colour import Color


if __name__ == '__main__':
    # reading the data
    with open('profile_list.json') as json_file:
        profile_list = json.load(json_file)

    tics = list(profile_list.keys())
    n_tics = len(tics)

    red = Color("red")
    colors = list(red.range_to(Color("green"), n_tics))
    G = Network()
    G.add_nodes(tics, color =[_.hex_l for _ in colors])

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
            G.add_edge(_[0],_[1], value=s)

        W[_[1]][_[0]] = W[_[0]][_[1]] = s

    for _ in tics:
        W[_][_]=0.0

    #G.show_buttons(filter_=['nodes', 'edges', 'layout', 'interaction', 'manipulation', 'physics', 'selection', 'renderer'])
    G.set_edge_smooth('continuous')
    G.show_buttons()
    G.show("G.html")
    print('done')


