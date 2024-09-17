import hashlib
import json

# Simulate a blockchain ledger
ledger = []

# Function to hash a transaction
def hash_transaction(transaction):
    """
    Takes a dictionary representing a transaction and returns its hash.
    """
    # Convert the transaction to a string using JSON, then encode it
    transaction_string = json.dumps(transaction, sort_keys=True).encode()
    
    # Create a SHA-256 hash of the transaction
    return hashlib.sha256(transaction_string).hexdigest()

# Function to add a transaction to the ledger
def add_transaction(sender, receiver, amount):
    """
    Create a transaction, hash it, and add it to the ledger.
    """
    transaction = {
        'sender': sender,
        'receiver': receiver,
        'amount': amount
    }
    
    # Hash the transaction
    transaction_hash = hash_transaction(transaction)
    
    # Simulate adding to the blockchain (ledger) by storing both the transaction and its hash
    ledger.append({
        'transaction': transaction,
        'hash': transaction_hash
    })
    
    print(f"Transaction added: {transaction}")
    print(f"Transaction hash: {transaction_hash}")

# Function to verify a transaction in the ledger
def verify_transaction(index):
    """
    Verify the integrity of a transaction by re-hashing it and comparing with the stored hash.
    """
    stored_data = ledger[index]
    stored_transaction = stored_data['transaction']
    stored_hash = stored_data['hash']
    
    # Recalculate the hash from the stored transaction
    recalculated_hash = hash_transaction(stored_transaction)
    
    if stored_hash == recalculated_hash:
        print("Transaction is valid!")
    else:
        print("Transaction has been tampered with!")

# Simulate some transactions
add_transaction("Alice", "Bob", 50)
add_transaction("Bob", "Charlie", 30)

# Verify the first transaction
verify_transaction(0)

# Tampering with a transaction (to simulate integrity check failure)
ledger[0]['transaction']['amount'] = 100

# Verify the first transaction again (this will fail)
verify_transaction(0)