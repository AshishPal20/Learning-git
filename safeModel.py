class ProtectedModel:
    def __init__(self, model_name, initial_temp):
        self.model_name = model_name
        self._temperature = initial_temp  # Protected attribute, can't be accessed directly from outside the class

# Getter method to access the protected attribute

    def get_temperature(self):
        return self._temperature
    
# Setter :  Safe way to change the private data with validation rules

    def set_temperature(self, new_temp):
        if new_temp < -273.15:
            print("⚠️ Temperature cannot be below absolute zero!")
        else:
            self._temperature = new_temp
            print(f"🌡️ {self.model_name} temperature set to {self._temperature}°C.")

# Execution
model = ProtectedModel("ThermoBot", 25)
print(f"Initial temperature of {model.model_name}: {model.get_temperature()}°C")    

model.set_temperature(30)  # Valid temperature change
print(f"Updated temperature of {model.model_name}: {model.get_temperature()}°C")

model._temperature = -300  # Attempt to directly access the protected attribute (not recommended)
print(f"Directly accessed temperature of {model.model_name}: {model._temperature}°C")  # This will show the value, but it's not safe practice

model.set_temperature(-300)  # Attempt to set an invalid temperature
