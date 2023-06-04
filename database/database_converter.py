import psycopg2
from web3 import Web3
import json

# Connect to the PostgreSQL database
conn = psycopg2.connect(
    host="your_host",
    port="your_port",
    database="your_database",
    user="your_username",
    password="your_password"
)

# Create a cursor object to execute SQL queries
cursor = conn.cursor()

# Retrieve data from the locations table
cursor.execute("SELECT * FROM locations")
rows = cursor.fetchall()

# Close the database connection
cursor.close()
conn.close()

# Connect to an Ethereum client provider (e.g., Infura)
web3 = Web3(Web3.HTTPProvider("https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID"))

# Load the compiled contract's ABI
abi = [...]  # Replace with the actual ABI obtained from compilation

# Set the contract address and account address for interaction
contract_address = "0x..."  # Replace with the actual deployed contract address
account_address = "0x..."  # Replace with the Ethereum account address for interaction
private_key = "..."  # The private key corresponding to the account

# Create the contract instance
contract = web3.eth.contract(address=contract_address, abi=abi)

# Set the gas price and gas limit for transactions
gas_price = web3.eth.gas_price
gas_limit = 3000000

# Iterate over the rows and migrate data to the blockchain
for row in rows:
    location_id, name, address, city, state, country = row

    # Transform the data into the appropriate format required by the contract
    transformed_data = {
        "id": location_id,
        "name": name,
        "address": address,
        "city": city,
        "state": state,
        "country": country
    }

    # Build the transaction to migrate data to the contract
    nonce = web3.eth.getTransactionCount(account_address)
    transaction = contract.functions.addLocation(
        transformed_data["name"],
        transformed_data["address"],
        transformed_data["city"],
        transformed_data["state"],
        transformed_data["country"]
    ).buildTransaction({
        "from": account_address,
        "nonce": nonce,
        "gasPrice": gas_price,
        "gas": gas_limit
    })

    # Sign the transaction with the private key
    signed_transaction = web3.eth.account.sign_transaction(transaction, private_key=private_key)

    # Send the transaction to the Ethereum network
    transaction_hash = web3.eth.send_raw_transaction(signed_transaction.rawTransaction)

    # Wait for the transaction to be mined
    transaction_receipt = web3.eth.wait_for_transaction_receipt(transaction_hash)

    print(f"Data migrated for location ID: {location_id}")

print("Data migration complete.")
