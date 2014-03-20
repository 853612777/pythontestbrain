

SelectorNode=1
ActionNode=2
ConditionNode=3
ParallelNode=4
SequenceNode=5

class BT(object):
	def __init__(self):
		super(BT, self).__init__()

	def start(self):
		action = self.root.findNextAction()
		if action is not None:
			action.excute()
		else:
			print 'no action'
			raise 'no action'


		