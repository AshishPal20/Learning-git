import random
import time

class AIAgent:
    # 1. Setup our initial state variables
    def __init__(self, name, model_type):
        self.name = name
        self.model_type = model_type
        self.battery_level = 100
        self.memory_logs = []
        self.status = "Idle"  # Keeps track of what the agent is doing

    # 2. Method to process an incoming engineering task
    def process_task(self, task_name, complexity):
        if self.battery_level < 20:
            print(f" [{self.name}] Battery too low ({self.battery_level}%). Must recharge!")
            self.status = "Low Battery"
            return
            
        self.status = "Processing"
        print(f"\n [{self.name}] is processing: '{task_name}' using {self.model_type}...")
        
        time.sleep(1) # Simulate the time it takes to compute
        
        # Modify internal state: decrease battery based on task size
        self.battery_level -= (complexity * 5)
        
        # Simulate a random success/fail condition
        success = random.choice([True, True, False]) 
        
        if success:
            log_message = f"SUCCESS: '{task_name}' completed."
            print(f"Success! Battery left: {self.battery_level}%")
        else:
            log_message = f"FAILED: '{task_name}' encountered an exception."
            print(f" Execution failed.")
            
        # Append the message to our agent's internal memory list
        self.memory_logs.append(log_message)
        self.status = "Idle"

    # 3. Method to reset the internal battery state
    def recharge(self):
        print(f"\n [{self.name}] Recharging battery...")
        time.sleep(1)
        self.battery_level = 100
        print(" Battery at 100%. Ready for tasks.")

# --- Execution Window ---
if __name__ == "__main__":
    # Create the object using our blueprint
    orchestrator = AIAgent("NexusBot", "Llama-3")
    
    # Run tasks to watch the internal state change dynamically
    orchestrator.process_task("Clean dataset anomalies", complexity=4)
    orchestrator.process_task("Generate vector database indexes", complexity=8)
    orchestrator.process_task("Run model evaluation tests", complexity=6)
    
    # Recharge the agent when the battery runs down
    orchestrator.recharge()
