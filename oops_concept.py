 
# Define the class
class Robot:
    # Constructor to initialize the robot's name
    def __init__(self, name, engine_type):
        self.name = name
        self.engine = engine_type
    
    # Method to greet
    def greet(self):
        return f"Hello, I am {self.name}!"

    # Method to perform a task
    def perform_task(self, task):
        return f"{self.name} is performing the task: {task}"
    


bot1 = Robot("Jarvis", "GPT-4")
bot2 = Robot("T-800", "Llama-4")

print(f"{bot1.greet()}, my engine type is {bot1.engine} and {bot1.perform_task('assisting humans')}.")
print(f"{bot2.greet()}, my engine type is {bot2.engine} and {bot2.perform_task('planting trees')}.")

# Functions written inside a class are called Methods.
# Whenever a method executes, it must take self as its first parameter so it knows which specific robot is performing the action.

