import time
from blockchain import Blockchain

# Initialize blockchain
blockchain = Blockchain()

# Register a node
blockchain.register_node('127.0.0.1:5000')

# Add a transaction and mine a block
blockchain.add_new_transaction(sender="Alice", receiver="Bob", amount=10)
blockchain.mine()

# Add another transaction and mine another block
blockchain.add_new_transaction(sender="Bob", receiver="Charlie", amount=5)
blockchain.mine()

# Print the blockchain
for block in blockchain.chain:
    print(block.__dict__)
