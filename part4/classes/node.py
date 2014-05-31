class Node:
	def __init__(self):
		self.id = None
		self.name = None
		self.parents = []
		self.probability_list = []
		self.pre_probability = None

	def set_id(self, id):
		self.id = id

	def set_name(self, name):
		self.name = name

	def set_parent(self, id):
		self.parents.append(id)

	def set_probability(self, attr, prob):
		if len(attr) == 0:
			self.pre_probability = float(prob)
		else:
			given = attr['given'].replace(' ', '').split(',')
			prob_dict = {}
			current = prob_dict
			for idx, condition in enumerate(given):
				if condition not in current:
					if idx == len(given)-1:
						current[condition] = float(prob)
					else:
						current[condition] = {}
				current = current[condition]
			self.probability_list.append(prob_dict)


	def get_probability(self, state, *args):		
		if len(args) == 0:
			if len(self.parents) == 0:
				if state is True:
					return self.pre_probability
				else:
					return 1.0 - self.pre_probability
			else:
				return None
		else:
			given = args[0]
			ret_val = None
			for probs in self.probability_list:
				for idx, condition in enumerate(given):
					if ret_val is None and idx == 0:
						ret_val = probs.get(condition)
							# print ret_val
					elif ret_val is not None:
						ret_val = ret_val.get(condition)
							
				if ret_val is not None:
					if state is False:
						ret_val = 1.0 - ret_val
					return ret_val
			
			return ret_val

	def has_parents(self):
		if len(self.parents) > 0:
			return True
		else:
			return False

	def is_evidence(self, e):
		if self.id in e:
			return True, True
		else:
			n_id = "".join(['-', self.id])
			if n_id in e:
				return True, False
			else:
				return False, None

	def negated_id(self):
		return "".join(['-', self.id])








