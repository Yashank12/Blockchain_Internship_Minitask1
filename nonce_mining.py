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
        
    def mine_block(self, difficulty):
        print(f"⛏️ Mining block with difficulty {difficulty}...")
        start_time = time.time()
        prefix = '0' * difficulty

        while not self.hash.startswith(prefix):
            self.nonce += 1
            self.hash = self.calculate_hash()

        end_time = time.time()
        print(f"✅ Block mined!")
        print(f"Hash: {self.hash}")
        print(f"Nonce: {self.nonce}")
        print(f"⏱️ Time taken: {round(end_time - start_time, 4)} seconds")


# In[2]:


difficulty = 4

block = Block(0, "This is a mined block", "0")
block.mine_block(difficulty)


# In[5]:


difficulty = 5

block = Block(0, "This is a mined block", "0")
block.mine_block(difficulty)


# In[7]:


difficulty = 6

block = Block(0, "This is a mined block", "0")
block.mine_block(difficulty)

