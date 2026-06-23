import json

def save_config(config_data):
    # 'w' overwrites the file with fresh configuration data
    with open("config.json", "w", encoding="utf-8") as file:
        # indent=4 formats the JSON beautifully instead of one single line
        json.dump(config_data, file, indent=4)
    print("Configuration saved to config.json")

def load_config():
    print("\n--- Loading Live Configuration ---")
    try:
        with open("config.json", "r", encoding="utf-8") as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        print("Config file not found.")
        return None

if __name__ == "__main__":
    # This represents a structured state configuration for an AI Agent
    ai_agent_settings = {
        "agent_name": "SupportBot-v2",
        "temperature": 0.3,
        "max_tokens": 150,
        "allowed_tools": ["search_web", "check_inventory", "calc_refund"],
        "active": True
    }
    
    # 1. Save data structure to disk
    save_config(ai_agent_settings)
    
    # 2. Load it back into memory
    loaded_settings = load_config()
    
    if loaded_settings:
        print(f"Agent Name: {loaded_settings['agent_name']}")
        print(f"Primary Tool: {loaded_settings['allowed_tools'][0]}")
        print(f"Sampling Temp: {loaded_settings['temperature']}")
