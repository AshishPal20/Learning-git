from abc import ABC, abstractmethod

# ABSTRACT CLASS (The Mandatory Template)
class DatabaseConnector(ABC):
    
    @abstractmethod
    def connect(self):
        pass                    # Forces every child to write their own 'connect' method

    @abstractmethod
    def fetch_embeddings(self):
        pass                   # Forces every child to write their own 'fetch_embeddings' method

# ACTUAL IMPLEMENTATION
class PineconeConnector(DatabaseConnector):
    def connect(self):
        print("Establishing handshake with Pinecone Cloud Vector Index...")

    def fetch_embeddings(self):
        print("Pulling dense vectors from Pinecone cluster...")

# --- Execution ---
# test = DatabaseConnector()        # ERROR: Python will crash! You cannot instantiate an abstract class directly.

vector_db = PineconeConnector()        # Works perfectly!
vector_db.connect()
vector_db.fetch_embeddings()
