class Robot:
    def __init__(self, assigned_name, engine_type):
        self.name = assigned_name
        self.engine = engine_type
        self.battery = 100

    # Action 1: Speak (Uses the robot's own name and engine data)
    def speak(self, message):
        if self.battery < 10:
            print(f"⚠️ {self.name} says: Battery too low to speak!")
            return
        self.battery -= 5      # Speaking uses 5% battery
        print(f"🤖 [{self.name} running {self.engine}]: '{message}' (Battery: {self.battery}%)")

    # Action 2: Charge (Modifies the robot's own battery data)
    def charge(self):
        self.battery = 100
        print(f"🔌 {self.name} has been fully recharged to 100%!")

# --- Execution ---
bot1 = Robot("Jarvis", "GPT-4")

# Triggering actions
bot1.speak("Hello User! How can I assist you with data pipelines today?")
bot1.speak("Running a test on vector embeddings...")

# Check the battery depletion
print(f"Current battery level of Jarvis: {bot1.battery}%")

# Recharge
bot1.charge()
