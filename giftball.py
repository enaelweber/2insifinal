from enum import Enum, auto

class GiftBall:
	def __init__(self, ball_count):
		self.current_state = State.NO_TOKEN
		self.__ball_count = ball_count

	def insert_token(self):
		if self.current_state == State.NO_TOKEN:
			self.current_state = State.ONE_TOKEN
	
	def eject_token(self):
		if self.current_state == State.ONE_TOKEN:
			self.current_state = State.NO_TOKEN
	
	def turn_crank(self):
		if self.current_state == State.ONE_TOKEN:
			self.current_state = State.BALL_SOLD
			self.dispense()
	
	def dispense(self):
		if self.current_state == State.BALL_SOLD:
			print("Voici une boule surprise !")
			self.__ball_count -= 1
			if self.__ball_count == 0:
				print("Plus de boules.")
				self.current_state = State.NO_BALLS
			else:
				self.current_state = State.NO_TOKEN

class State(Enum):
	NO_TOKEN = auto()
	ONE_TOKEN = auto()
	BALL_SOLD = auto()
	NO_BALLS = auto()

if __name__ == '__main__':
	ball_machine = GiftBall(5)
	for i in range(7):
		ball_machine.insert_token()
		ball_machine.turn_crank()