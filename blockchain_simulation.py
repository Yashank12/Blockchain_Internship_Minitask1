#!/usr/bin/env python
# coding: utf-8

# In[1]:


import hashlib
import time

class Block:
    def __init__(self, index, data, previous_hash):
        self.index = index
        self.timestamp = time.time()
        self.data = data
        self.previous_hash = previous_hash
        self.nonce = 0
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        block_contents = (
            str(self.index)
            + str(self.timestamp)
            + str(self.data)
            + self.previous_hash
            + str(self.nonce)
        )
        return hashlib.sha256(block_contents.encode()).hexdigest()

    def __str__(self):
        return (
            f"Block {self.index}\n"
            f"Timestamp: {self.timestamp}\n"
            f"Data: {self.data}\n"
            f"Previous Hash: {self.previous_hash}\n"
            f"Hash: {self.hash}\n"
            f"Nonce: {self.nonce}\n"
            f"{'-'*40}"
        )

blockchain = []

genesis_block = Block(0, "Genesis Block", "0")
blockchain.append(genesis_block)

# Block 1
block1 = Block(1, "Block 1 Data", genesis_block.hash)
blockchain.append(block1)

# Block 2
block2 = Block(2, "Block 2 Data", block1.hash)
blockchain.append(block2)


#Validity function

def is_chain_valid(chain):
    for i in range(1, len(chain)):
        current_block = chain[i]
        previous_block = chain[i - 1]

        if current_block.hash != current_block.calculate_hash():
            print(f"❌ Block {i}'s hash is invalid!")
            return False

        if current_block.previous_hash != previous_block.hash:
            print(f"❌ Block {i}'s previous hash doesn't match Block {i-1}'s hash!")
            return False

    print("✅ Blockchain is valid.")
    return True



print("Original Blockchain:\n")
for block in blockchain:
    print(block)


# In[2]:


is_chain_valid(blockchain)


# In[3]:


print("Original block 1 hash-" , blockchain[1].hash)


# In[4]:


is_chain_valid(blockchain)


# In[5]:


#Tampering Block 1
blockchain[1].data = "Tampered Data"
blockchain[1].hash = blockchain[1].calculate_hash()

print("Trampered block 1 hash-" , blockchain[1].hash)


# In[6]:


print("Blockchain After Tampering:\n")

for block in blockchain:
    print(block)


# In[7]:


is_chain_valid(blockchain)

