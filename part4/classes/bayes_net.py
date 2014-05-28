from node import Node
import xml.etree.ElementTree as ET

class BayesNet:
	def __init__(self, source):
		self.nodes = []
		
		root = source.getroot()

		for node in root:
			newNode = Node()
			for field in node:
				if field.tag == 'id':
					newNode.set_id(field.text)
				elif field.tag == 'name':
					newNode.set_name(field.text)
				elif field.tag == 'parent':
					newNode.set_parent(field.text)
				elif field.tag == 'probability':
					newNode.set_probability(field.attrib, field.text)
			
			# print newNode.id, newNode.name, newNode.parents, newNode.probability_list
			given = ['-C']
			print newNode.get_probability(given)
			# print newNode.name, newNode.get_probability(given)
		

	# M is the number of times
	# N is the number of samples
	def likelihood_weighting(M, N):
		pass


