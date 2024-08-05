import hashlib
import time
import json
import random
from typing import List, Dict
from uuid import uuid4

class Block:
    def __init__(self, index: int, previous_hash: str, transactions: List[Dict], timestamp: float, nonce=0):
        self.index = index
        self.previous_hash = previous_hash
        self.transactions = transactions
        self.timestamp = timestamp
        self.nonce = nonce
        self.hash = self.compute_hash()

    def compute_hash(self):
        block_string = json.dumps(self.__dict__, sort_keys=True)
        return hashlib.sha256(block_string.encode()).hexdigest()

class Blockchain:
    difficulty = 2

    def __init__(self):
        self.unconfirmed_transactions = []
        self.chain = []
        self.nodes = set()
        self.create_genesis_block()

    def create_genesis_block(self):
        genesis_block = Block(0, "0", [], time.time())
        genesis_block.hash = genesis_block.compute_hash()
        self.chain.append(genesis_block)

    @property
    def last_block(self):
        return self.chain[-1]

    def register_node(self, address: str):
        self.nodes.add(address)

    def add_block(self, block: Block, proof: str) -> bool:
        previous_hash = self.last_block.hash
        if previous_hash != block.previous_hash:
            return False
        if not self.is_valid_proof(block, proof):
            return False
        block.hash = proof
        self.chain.append(block)
        return True

    def proof_of_work(self, block: Block) -> str:
        block.nonce = 0
        computed_hash = block.compute_hash()
        while not computed_hash.startswith('0' * Blockchain.difficulty):
            block.nonce += 1
            computed_hash = block.compute_hash()
        return computed_hash

    def add_new_transaction(self, sender: str, receiver: str, amount: float):
        transaction = {
            'sender': sender,
            'receiver': receiver,
            'amount': amount,
            'timestamp': time.time(),
            'id': str(uuid4())
        }
        self.unconfirmed_transactions.append(transaction)

    def mine(self) -> int:
        if not self.unconfirmed_transactions:
            return -1
        last_block = self.last_block
        new_block = Block(index=last_block.index + 1,
                          previous_hash=last_block.hash,
                          transactions=self.unconfirmed_transactions,
                          timestamp=time.time())
        proof = self.proof_of_work(new_block)
        self.add_block(new_block, proof)
        self.unconfirmed_transactions = []
        return new_block.index

    def is_valid_proof(self, block: Block, block_hash: str) -> bool:
        return (block_hash.startswith('0' * Blockchain.difficulty) and
                block_hash == block.compute_hash())

    def check_chain_validity(self, chain: List[Block]) -> bool:
        previous_hash = "0"
        for block in chain:
            block_hash = block.hash
            del block.hash  # Remove hash to recompute it
            if not self.is_valid_proof(block, block_hash) or \
                    previous_hash != block.previous_hash:
                return False
            block.hash = block_hash
            previous_hash = block_hash
        return True

    def resolve_conflicts(self):
        """
        Resolve conflicts between different chains by replacing our chain with the longest valid chain in the network.
        """
        neighbors = self.nodes
        new_chain = None
        max_length = len(self.chain)

        for node in neighbors:
            response = self.request_chain(node)
            if response.status_code == 200:
                length = response.json()['length']
                chain = response.json()['chain']
                if length > max_length and self.check_chain_validity(chain):
                    max_length = length
                    new_chain = chain

        if new_chain:
            self.chain = new_chain
            return True
        return False

    def request_chain(self, node: str):
        # Placeholder function to simulate a network request
        import requests
        response = requests.get(f'http://{node}/chain')
        return response

# Example usage
blockchain = Blockchain()
blockchain.register_node('127.0.0.1:5000')

blockchain.add_new_transaction(sender="Alice", receiver="Bob", amount=10)
blockchain.mine()

blockchain.add_new_transaction(sender="Bob", receiver="Charlie", amount=5)
blockchain.mine()

print("Blockchain:")
for block in blockchain.chain:
    print(block.__dict__)
