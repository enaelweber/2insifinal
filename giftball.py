from abc import ABC, abstractmethod
import random

class State(ABC):

	@abstractmethod
	def insert_token(self, machine):
		pass

	@abstractmethod
	def eject_token(self, machine):
		pass
		
	@abstractmethod
	def turn_crank(self, machine):
		pass

	@abstractmethod
	def dispense(self, machine):
		pass

class NoTokenState(State):
	def insert_token(self, machine):
		machine.set_state(machine.one_token_state)
	
	def eject_token(self, machine):
		pass

	def turn_crank(self, machine):
		pass

	def dispense(self, machine):
		pass

class OneTokenState(State):
	def insert_token(self, machine):
		pass
	
	def eject_token(self, machine):
		machine.set_state(machine.no_token_state)

	def turn_crank(self, machine):
		if random.random() < 0.20 and machine.ball_count() >= 2:
			print("Coup de chance !")
			machine.set_state(machine.surprise_win)
		else:
			machine.set_state(machine.ball_sold_state)
		machine.dispense()

	def dispense(self, machine):
		pass

class BallSoldState(State):
	def insert_token(self, machine):
		pass
	
	def eject_token(self, machine):
		pass

	def turn_crank(self, machine):
		pass

	def dispense(self, machine):
		machine.release_ball()
		if machine.ball_count() == 0:
			print("Plus de boules.")
			machine
		else:
			machine.set_state(machine.no_token_state)

class NoBallsState(State):
	def insert_token(self, machine):
		pass
	
	def eject_token(self, machine):
		pass

	def turn_crank(self, machine):
		pass

	def dispense(self, machine):
		pass

class SurpriseWin(State):
	def insert_token(self, machine):
		pass
	
	def eject_token(self, machine):
		pass

	def turn_crank(self, machine):
		pass

	def dispense(self, machine):
		machine.release_ball()
		if machine.ball_count() == 0:
			print("Plus de boules.")
			machine
		else:
			machine.set_state(machine.no_token_state)

class GiftBall:
	def __init__(self, ball_count):
		self.no_token_state = NoTokenState()
		self.one_token_state = OneTokenState()
		self.ball_sold_state = BallSoldState()
		self.no_balls_state = NoBallsState()
		self.surprise_win = SurpriseWin()
	
		self.__ball_count = ball_count
		self.__current_state = self.no_token_state

	def insert_token(self):
		self.__current_state.insert_token(self)

	def eject_token(self):
		self.__current_state.eject_token(self)

	def turn_crank(self):
		self.__current_state.turn_crank(self)

	def dispense(self):
		self.__current_state.dispense(self)

	def set_state(self, state):
		self.__current_state = state
	
	def release_ball(self):
		if self.__ball_count > 0:
			print("Voici une boule surprise !")
			self.__ball_count -= 1
	
	def ball_count(self):
		return self.__ball_count


if __name__ == '__main__':
	ball_machine = GiftBall(5)
	for i in range(7):
		ball_machine.insert_token()
		ball_machine.turn_crank()