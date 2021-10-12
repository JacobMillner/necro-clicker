import sys, signal, time
from util.state_machine import StateMachine

# exit program with ctrl-c
def signal_handler(signal, frame):
    print("\nprogram exiting gracefully")
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

machine = StateMachine()

# main bot loop goes here
while (True):
    print("doing bot things")
    time.sleep(1)