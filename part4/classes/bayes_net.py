from node import Node
import xml.etree.ElementTree as ET
import random

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
			self.nodes.append(newNode)
		
	# Calculate the P(X|e) based on N samples
	def likelihood_weighting(self, X, e, N):
		samples = {}
		for i in range(0, N):
			x, w = self.weighted_sample(e)
			samples[i] = {'x': x, 'w': w}

		weight_sum = 0
		for key in samples:
			if X in samples[key]['x']:
				weight_sum += 1

		return float(weight_sum)/float(N)

	def weighted_sample(self, e):
		x = []
		w = 1.0

		for node in self.nodes:

			# check this node is evidence or not
			is_evidence, node_state = node.is_evidence(e)

			if is_evidence:
				# w = wp(currentNode | parents of currentNode)
				if node.has_parents():
					w = w * node.get_probability(node_state, node.parents)
				else:
					w = w * node.get_probability(node_state)

				# x <- x_i
				if node_state:
					x.append(node.id)
				else:
					x.append(node.negated_id())
			else:
				# not evidence, so we take a random sample
				if node.has_parents():
					# check set is parents are in x
					given_parents = []
					for parent in node.parents:
						if parent in x:
							given_parents.append(parent)
						else:
							neg = "".join(['-', parent])
							if neg in x:
								given_parents.append(neg)

					# sample P(this| parents(this))
					p_true = node.get_probability(True, given_parents)

					random.seed()
					rng = random.uniform(0, 1.0)

					if rng <= p_true:
						x.append(node.id)
					else:
						x.append(node.negated_id())
					
				else:
					p_true = node.get_probability(True)

					random.seed()
					rng = random.uniform(0, 1.0)

					if rng <= p_true:
						x.append(node.id)
					else:
						x.append(node.negated_id())

		return x, w







