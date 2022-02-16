import random
import time
import keyboard

class Typer():
    def __init__(self):
        self.repeat_amount = 0
        self.key_delay = 0
        self.line_delay = 0
        self.random_ranges = {"key": [0.05, 0.3], "line": [0.1, 1]}
        self.random = False
        self.running = False
        
        self.text = ""

    def randomize_values(self):
        if self.random:
            key_ranges = self.random_ranges["key"]
            line_ranges = self.random_ranges["line"]
            self.key_delay = random.uniform(key_ranges[0], key_ranges[1])
            self.line_delay = random.uniform(line_ranges[0], line_ranges[1])

    def start(self):
        self.running = True

        for i in range(self.repeat_amount):
            for line in self.text.split("\n"):

                if not self.running:
                    return

                self.randomize_values()

                for char in line:
                    self.randomize_values()

                    keyboard.write(char)
                    time.sleep(self.key_delay)
                
                keyboard.press_and_release("enter")
                time.sleep(self.line_delay)

    def stop(self):
        self.running = False