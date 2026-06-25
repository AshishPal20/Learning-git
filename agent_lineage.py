# PARENT CLASS
class BaseAgent:
    def __init__(self, name):
        self.name = name
        self.memory = []

    def log_action(self, action):
        self.memory.append(action)
        print(f"Logged: {action}")

# CHILD CLASS (Inherits everything from BaseAgent)
class VisionAgent(BaseAgent):
    def __init__(self, name, camera_resolution):
        # super() references the Parent class. This sets up 'name' and 'memory' automatically!
        super().__init__(name) 
        self.resolution = camera_resolution # Unique variable just for VisionAgent

    # Unique method just for VisionAgent
    def analyze_image(self, image_path):
        print(f"[{self.name}] Scanning image at {self.resolution}...")
        self.log_action(f"Analyzed image: {image_path}")

# --- Execution ---
# Create an instance of the child class
vision_bot = VisionAgent("Oculus-v1", "4K")

# VisionAgent can use methods written in BaseAgent!
vision_bot.log_action("System booted.") 

# VisionAgent can also use its own unique methods
vision_bot.analyze_image("user_avatar.png")
