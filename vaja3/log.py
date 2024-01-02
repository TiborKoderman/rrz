import manus
from pynput import keyboard

states = []
server = manus.Server(address="192.168.1.103", port=80)
manipulator = manus.Manipulator(server)


def on_key_press(key):
    if key == keyboard.Key.space:
        state, _ = manipulator.state()
        state = [
            state[0]["position"],
            state[1]["position"],
            state[2]["position"],
            state[3]["position"],
            state[4]["position"],
            state[5]["position"],
            state[6]["position"],
        ]
        states.append(state)
        print(state)

    if key == keyboard.Key.enter:
        keyboard.Listener.stop(listener)
        return states


with keyboard.Listener(on_press=on_key_press) as listener:
    listener.join()


print(states)