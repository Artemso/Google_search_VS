import networkx as nx
from bokeh.io import show
from bokeh.models import Plot, Range1d, MultiLine, Circle, HoverTool, TapTool, BoxSelectTool, PanTool, WheelZoomTool, ResetTool
from bokeh.plotting import from_networkx

class Visualise():
	def	__init__(self):
		pass

	def	add_nodes(self, graph, dictionary):
		for key in dictionary:
			graph.add_node(key)
			for value in dictionary[key]:
				graph.add_node(value)

	def	add_edges(self, graph, dictionary):
		for key in dictionary:
			for value in dictionary[key]:
				graph.add_edge(key, value)

	def visualise_graph(self, dictionary):
		graph = nx.Graph()
		self.add_nodes(graph, dictionary)
		self.add_edges(graph, dictionary)
		plot = Plot(
			plot_width=1140,
			plot_height=720,
			x_range=Range1d(-1.1,1.1),
			y_range=Range1d(-1.1,1.1))
		plot.add_tools(
			TapTool(),
			BoxSelectTool(),
			PanTool(),
			WheelZoomTool(),
			ResetTool())
		graph_render = from_networkx(graph, nx.spring_layout, scale=2.5, center=(0,0))
		plot.renderers.append(graph_render)
		show(plot)