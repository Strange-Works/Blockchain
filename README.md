# Blockchain

This project involves creating a basic blockchain from scratch, encompassing key concepts in cryptography and distributed systems. The aim is to develop a secure, decentralized ledger that maintains data integrity through cryptographic hashes and consensus algorithms.

## Features

1. **Block Structure**:

   - Each block contains an index, timestamp, transactions, previous block’s hash, nonce, and the current block's hash.

2. **Cryptographic Hashing**:

   - Uses SHA-256 for hashing block data to ensure immutability.

3. **Proof of Work (PoW)**:

   - Implements PoW to add new blocks to the blockchain with a difficulty adjustment mechanism.

4. **Transactions**:

   - Supports creating and validating transactions with fields for sender, receiver, amount, timestamp, and a unique ID.

5. **Peer-to-Peer Network**:

   - Simulates a network of nodes that can communicate and share blockchain data.

6. **Validation and Consensus**:

   - Validates blocks and ensures consistency of the blockchain across nodes.
   - Resolves conflicts by adopting the longest valid chain.

## Getting Started

### Prerequisites

- Python 3.6 or higher
- Requests library (for network simulation)
- Flask (optional, for developing API)

### Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/your-username/blockchain-implementation.git
   cd blockchain-implementation
   ```
2. Install the required libraries:
   ```sh
   pip install requests
   ```
3. (Optional) Install Flask for API development
   ```sh
   pip install Flask
   ```

### Running the Blockchain

1. **Initialize the Blockchain**:
   Create a new Python script (e.g., `run_blockchain.py`) and initialize the blockchain:

   ```python
   from blockchain import Blockchain

   blockchain = Blockchain()
   ```

2. **Register Nodes:**
   Register a node with the blockchain:
   ```python
   blockchain.register_node('127.0.0.1:5000')
   ```
3. **Add Transactions:**
   Add a transaction to the blockchain:
   `python
    blockchain.add_new_transaction(sender="Alice", receiver="Bob", amount=10)
    `
4. **Mine a block:** Mine a new block to add the transaction to the blockchain:
   ```python
   blockchain.mine()
   ```
5. **Print the blockchain:** Print the entire blockchain to see its contents:
   ```python
   for block in blockchain.chain:
   print(block.__dict__)
   ```

See the [example usage](exampleUsage.py) for a basic example to illustrate how to use the blockchain.

### Contact

For any questions or suggestions, please email me.

[Oliver Strange](mailto:oliver@strangedesign.co.uk?subject=[GitHub]%20Source%20Han%20Sans)
