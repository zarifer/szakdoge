import sys
import angr
import networkx as nx
import numpy as np
import pandas as pd
import os

files = os.listdir('/root/kitkat/kitti-additional-samples/benign/')
exceptions = os.listdir('/root/kitkat/szakdoge/benign_sol')

for file in files:
	if file in exceptions:
		continue
		
	os.mkdir(f'/root/kitkat/szakdoge/benign_sol/{file}')
	
	try:
		p = angr.Project('/root/kitkat/kitti-additional-samples/benign/'+file, load_options={'auto_load_libs':False})
		cfg = p.analyses.CFGFast()
		G = cfg.graph
		os.mkdir(f'/root/kitkat/szakdoge/benign_sol/{file}')

		with open(f'/root/kitkat/szakdoge/benign_sol/{file}/running_error.txt', 'w') as fe:
			with open(f'/root/kitkat/szakdoge/benign_sol/{file}/feature_vector.txt', 'w') as f:
				sys.stdout = fe

				#Number of edges in the graph
				f.write(str(nx.number_of_edges(G))+"\n")

				#Number of nodes in the graph
				f.write(str(nx.number_of_nodes(G))+"\n")

				#The density of a graph
				f.write(str(nx.density(G))+"\n")
				
				#The number of components
				f.write(str(nx.number_strongly_connected_components(G))+"\n")

				#The shortest path length
				sp = dict(nx.all_pairs_shortest_path_length(G))
				#f.write(str(sp))

				#The minimum of shortest path
				df =  [np.min(list(spl.values())) for spl in sp.values()]
				f.write(str(np.min(df))+"\n")

				#The maximum of shortest path
				df = [np.max(list(spl.values())) for spl in sp.values()]
				f.write(str(np.max(df))+"\n")

				#The median of shortest path
				df = []
				for spl in sp.values():
					df += spl.values()
				f.write(str(np.median(df))+"\n")

				#The mean of shortest path
				df = []
				for spl in sp.values():
					df += spl.values()
				f.write(str(np.mean(df))+"\n")

				#The standard deviation of shortest path
				df = []
				for spl in sp.values():
					df += spl.values()
				f.write(str(np.std(df))+"\n")
				
				#The Betweenness Centrality of the graph
				bc = nx.centrality.betweenness_centrality(G)
				
				#The minimum of BC
				f.write(str(np.min(list(bc.values())))+"\n")

				#The maximum of BC
				f.write(str(np.max(list(bc.values())))+"\n")

				#The median of BC
				f.write(str(np.median(list(bc.values())))+"\n")

				#The mean of BC
				f.write(str(np.mean(list(bc.values())))+"\n")

				#The standard deviation of BC
				f.write(str(np.std(list(bc.values())))+"\n")

				#The Closeness Centrality of the graph
				cc = nx.centrality.closeness_centrality(G)
				
				#The minimum of CC
				f.write(str(np.min(list(cc.values())))+"\n")

				#The maximum of CC
				f.write(str(np.max(list(cc.values())))+"\n")

				#The median of CC
				f.write(str(np.median(list(cc.values())))+"\n")

				#The mean of CC
				f.write(str(np.mean(list(cc.values())))+"\n")

				#The standard deviation of CC
				f.write(str(np.std(list(cc.values())))+"\n")
		
				#The Degree Centrality of the graph
				dc = nx.centrality.degree_centrality(G)
				
				#The minimum of DC
				f.write(str(np.min(list(dc.values())))+"\n")

				#The maximum of DC
				f.write(str(np.max(list(dc.values())))+"\n")

				#The median of DC
				f.write(str(np.median(list(dc.values())))+"\n")

				#The mean of DC
				f.write(str(np.mean(list(dc.values())))+"\n")

				#The standard deviation of DC
				f.write(str(np.std(list(dc.values())))+"\n")

	except Exception as e:
		with open(f'/root/kitkat/szakdoge/benign_sol/{file}/exception.txt', 'w') as fem:
			fem.write(str(e))
		continue
