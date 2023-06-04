from flask import Flask, request, jsonify
from web3 import Web3

# Connect to the Ethereum network
web3 = Web3(Web3.HTTPProvider('https://your-infura-endpoint'))

# Set up the Ethereum account
account = web3.eth.account.from_key('your-private-key')
contract_address = 'your-contract-address'

app = Flask(__name__)

@app.route('/location-node', methods=['POST'])
def location_node():
    # Get the location attributes from the request body
    location = request.get_json()
    
    # Perform the Ethereum node building process with the location attributes
    # Replace this with your own implementation
    
    # Extract location attributes from the object
    location_id = location.get('id')
    name = location.get('name')
    address = location.get('address')
    city = location.get('city')
    state = location.get('state')
    country = location.get('country')
    
    # Convert the location attributes into an Ethereum node
    node_data = {
        'location_id': location_id,
        'name': name,
        'address': address,
        'city': city,
        'state': state,
        'country': country
    }
    
    # Call the smart contract function to store the Ethereum node data
    contract = web3.eth.contract(address=contract_address, abi=contract_abi)
    tx_hash = contract.functions.storeNode(node_data).transact({'from': account.address})
    web3.eth.waitForTransactionReceipt(tx_hash)
    
    # Example response
    response = {
        'status': 'success',
        'message': 'Ethereum node built and stored successfully',
        'transaction_hash': tx_hash.hex()
    }
    
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)

