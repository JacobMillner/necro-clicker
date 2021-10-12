from enum import Enum

class StateMachine:
  _state = 'ERR'

  def __init__(self):
      self.state = 'START'
  
  def setState(self, new_sate):
    if new_sate == State.STAND:
        self._state = State.Stand
    elif new_sate == State.RUN_RIGHT:
        self._state = State.RUN_RIGHT
    elif new_sate == State.RUN_LEFT:
        self._state = State.RUN_LEFT
    elif new_sate == State.RUN_UP:
        self._state = State.RUN_UP
    elif new_sate == State.RUN_DOWN:
        self._state = State.RUN_DOWN
    else:
        print("Unknown state: " + new_sate)   

class State(Enum):
    ERR = 0
    START = 1
    STAND = 2
    RUN_RIGHT = 3
    RUN_LEFT = 4
    RUN_UP = 5
    RUN_DOWN = 6

