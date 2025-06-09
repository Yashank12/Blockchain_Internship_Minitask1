#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random

# PoW validators (miners with "power")
pow_validators = {
    "A": random.randint(1, 100),
    "B": random.randint(1, 100),
    "C": random.randint(1, 100)
}

# PoS validators (stakers with "stake" amount)
pos_validators = {
    "A": random.randint(1, 100),
    "B": random.randint(1, 100),
    "C": random.randint(1, 100)
}

# DPoS voters vote for one of the 3 delegates
votes = {
    "User1": "B",
    "User2": "C",
    "User3": "C"
}


# In[2]:


def simulate_pow(validators):
    print("PoW Simulation:")
    for name, power in validators.items():
        print(f"{name} has power {power}")
    winner = max(validators, key=validators.get)
    print(f"Selected Miner (Highest Power): {winner}\n")


# In[3]:


def simulate_pos(validators):
    print("PoS Simulation:")
    for name, stake in validators.items():
        print(f"{name} has stake {stake}")
    winner = max(validators, key=validators.get)
    print(f"Selected Validator (Highest Stake): {winner}\n")


# In[4]:


import random

def simulate_dpos(votes):
    print("DPoS Simulation:")
    vote_count = {}
    
    # Count votes for each delegate
    for voter, choice in votes.items():
        print(f"{voter} voted for {choice}")
        vote_count[choice] = vote_count.get(choice, 0) + 1

    max_votes = max(vote_count.values())

    # Get all delegates with max votes (could be multiple)
    top_candidates = [delegate for delegate, count in vote_count.items() if count == max_votes]

    # Randomly pick one among top
    winner = random.choice(top_candidates)

    print(f"Vote Count: {vote_count}")
    print(f"Top Voted Delegates: {top_candidates}")
    print(f"Selected Delegate (Random among top): {winner}\n")


# In[5]:


simulate_pow(pow_validators)
simulate_pos(pos_validators)
simulate_dpos(votes)


# 1. Proof of Work (PoW)
# Decision is based on who solves a complex mathematical puzzle first.
# Every validator (miner) competes by spending real computing power.
# The one who finds the correct nonce (satisfying difficulty) earns the right to add the next block.
# It's secure but slow and energy-intensive due to high computational effort.
# 
# 
# 2. Proof of Stake (PoS)
# Decision is based on the amount of cryptocurrency each validator locks ("stakes").
# Validators are probabilistically chosen — more stake = higher chances.
# No mining needed, so it’s energy-efficient.
# Attackers must hold a large share of coins to disrupt consensus.
# 
# 
# 3. Delegated Proof of Stake (DPoS)
# Token holders vote to elect a small group of trusted delegates.
# These delegates are responsible for validating blocks in rotation.
# Decision power lies with community votes, making it democratic but slightly more centralized.
# Fast and efficient, but depends on voter participation.
