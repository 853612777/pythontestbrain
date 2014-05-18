

SelectorNode=1
ActionNode=2
ConditionNode=3
ParallelNode=4
SequenceNode=5

all=[]
inst={'name':'root','type':SelectorNode,'callback':[]}
all.append(inst)
inst={'name':'hunting','type':ActionNode,'callback':[]}
all.append(inst)

print all


class BTNode(object):
	def __init__(self,data=-1,childs=None):
		self.data=data
		self.childs=childs



class BT(object):
	def __init__(self):
		self.root=BTNode()

	def add(self,data):
		node=BTNode(data)
		if self.root.data == -1:
			self.root=node
		else:
			if self.root.childs is not None:
				self.root.childs.append(node)
			else:
				self.root.childs=[node]


	def start(self):
		action = self.root.findNextAction()
		if action is not None:
			action.excute()
		else:
			print 'no action'
			raise 'no action'


	def findNextAction(self):
		pass