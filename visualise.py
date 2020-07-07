import networkx as nx
import matplotlib.pyplot as plt

class Visualise():
	def	__init__(self):
		pass

	def	get_nodes(self, data):
		new_dict = {}
		for key in data.keys():
			if key in new_dict:
				new_dict[key] += 1
			else:
				new_dict.update({key : 1})
		for value in data.values():
			for x in value:
				if x in new_dict:
					new_dict[x] += 1
				else:
					new_dict.update({x : 1})
		return new_dict

	def	get_edges(self, data):
		new_list = []
		for key, value in data.items():
			for x in value:
				item = []
				item.append(key)
				item.append(x)
				new_list.append(item)
		return new_list


	def	visualise_data(self, data):
		nodes_lst = self.get_nodes(data)
		edges_lst = self.get_edges(data)
		G = nx.Graph()
		G.add_nodes_from(list(nodes_lst.keys()))
		G.add_edges_from(edges_lst)
		graph = nx.ego_graph(G, list(nodes_lst.keys())[1], radius=5)
		pos=nx.spring_layout(graph)
		nx.draw(graph, pos, node_color='b', node_size=50, with_labels=True)
		plt.show()