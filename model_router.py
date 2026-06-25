class OpenAIModel:
    def generate_text(self, prompt):
        return f"OpenAI Response to '{prompt}': Using GPT-4 cloud endpoints."

class AnthropicModel:
    def generate_text(self, prompt):
        return f"Anthropic Response to '{prompt}': Using Claude internal routing."

class LocalModel:
    def generate_text(self, prompt):
        return f"Local Model Response to '{prompt}': Running on your local GPU via Ollama."

# --- Execution (The Power of Polymorphism) ---
# We put completely different objects into a single list
model_pipeline = [OpenAIModel(), AnthropicModel(), LocalModel()]

user_prompt = "Explain RAG pipelines in one sentence."

# We can call the exact same method name on all of them in a simple loop!
for model in model_pipeline:
    print(model.generate_text(user_prompt))
