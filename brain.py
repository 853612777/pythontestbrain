from state import State

class brain(object):
	def __init__(self):
		self.states={}
		self.active_state=None

	def add_state(self,State):
		self.states[State.name]=State

	def think(self):
		if self.active_state is None:
			return

		self.active_state.do_actions()
		new_state_name=self.active_state.check_conditions()
		if new_state_name is not None:
			self.set_state(new_state_name)

	def set_state(self,new_state_name):
		if self.active_state is not None:
			self.active_state.exit_actions()
		self.active_state = self.states[new_state_name]
		self.active_state.entry_actions()