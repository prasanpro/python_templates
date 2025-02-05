import random

def approach_if_else(random_number):
    if random_number == 1:
        print("Action 1")
    elif random_number == 2:
        print("Action 2")
    elif random_number == 3:
        print("Action 3")
    else:
        print("Unknown action")

def approach_dict(random_number):
    actions = {
        1: "Action 1",
        2: "Action 2",
        3: "Action 3"
    }
    action = actions.get(random_number, "Unknown action")
    print(action)

class SwitchActions:
    def action_1(self):
        print("Action 1")
    def action_2(self):
        print("Action 2")
    def action_3(self):
        print("Action 3")

def approach_class(random_number):
    switch = SwitchActions()
    method_name = "action_" + str(random_number)
    action_method = getattr(switch, method_name, lambda: "Unknown action")
    action_method()

# Generate a random number between 1 and 3
random_number = random.randint(1, 3)

print("Random number:", random_number)

print("Using if-elif-else:")
approach_if_else(random_number)

print("Using dictionary:")
approach_dict(random_number)

print("Using class methods:")
approach_class(random_number)
