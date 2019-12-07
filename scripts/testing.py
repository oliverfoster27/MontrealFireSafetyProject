import networkx as nx
import multiprocessing
import pandas as pd

Z = []
G = nx.read_gpickle(r"full_graph_time2fs.gpickle")
fs_nodes = [x for x, y in G.nodes(data=True) if y['FIRE_STATION'] == True]
junction_nodes = [x for x in G.nodes if len(list(G.edges(x))) > 2]


def chunker_list(seq, size):
    return [seq[i::size] for i in range(size)]


def shortest_to_fs(fs_chunk, node, return_list):
    min_dist = 1000
    for fs in fs_chunk:
        try:
            dist = nx.shortest_path_length(G, source=fs, target=node, weight='time')
        except nx.NetworkXNoPath:
            continue
        if dist < min_dist:
            min_dist = dist
    return_list.append(min_dist)

if __name__ == '__main__':

    for n1, n2, packet in list(G.edges(data=True)):
        if packet['length'] / packet['time'] < 10:
            G[n1][n2]['time'] = packet['length'] / 10

    chunks = chunker_list(fs_nodes, 4)

    idx = 0
    for node in junction_nodes:

        idx += 1
        print(idx, '/', len(junction_nodes))
        processes = []

        manager = multiprocessing.Manager()
        return_list = manager.list()
        for i in range(0, 4):
            p = multiprocessing.Process(target=shortest_to_fs, args=(chunks[i], node, return_list))
            processes.append(p)
            p.start()

        for process in processes:
            process.join()

        nx.set_node_attributes(G, {node: {'TIME_TO_FS': min(return_list)}})

    data = []
    for node in G.nodes(data=True):
        data.append({'Longitude': node[0][0], 'Latitude': node[0][1], **node[1]})
    res = pd.DataFrame(data)
    res.to_csv(r"node_data_time2.csv")

    nx.write_gpickle(G, "full_graph_time2fs2.gpickle")