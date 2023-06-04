from flask import Flask, request, jsonify
from web3 import Web3

app = Flask(__name__)

# Initialize Web3 instance
web3 = Web3(Web3.HTTPProvider('https://infura.io/v3/YOUR_INFURA_PROJECT_ID'))

# Load the contract ABI and bytecode
contract_abi = [
    # Replace with the actual ABI of your smart contract
    {
        "constant": false,
        "inputs": [
            {
                "name": "location_id",
                "type": "uint256"
            },
            {
                "name": "name",
                "type": "string"
            },
            {
                "name": "address",
                "type": "string"
            },
            {
                "name": "city",
                "type": "string"
            },
            {
                "name": "state",
                "type": "string"
            },
            {
                "name": "country",
                "type": "string"
            }
        ],
        "name": "createLocation",
        "outputs": [],
        "payable": false,
        "stateMutability": "nonpayable",
        "type": "function"
    }
]

contract_bytecode = "0x..."  # Replace with the actual bytecode of your smart contract

# Deploy the smart contract
contract = web3.eth.contract(abi=contract_abi, bytecode=contract_bytecode)

@app.route('/location-node', methods=['POST'])
def build_ethereum_node():
    # Get the location attributes from the request body
    location = request.get_json()
    
    # Extract location attributes from the object
    location_id = location.get('id')
    name = location.get('name')
    address = location.get('address')
    city = location.get('city')
    state = location.get('state')
    country = location.get('country')
    
    # Perform the Ethereum node building process
    try:
        # Create the Ethereum node using contract function
        tx_hash = contract.functions.createLocation(
            location_id, name, address, city, state, country
        ).transact()

        # Wait for the transaction to be mined
        tx_receipt = web3.eth.waitForTransactionReceipt(tx_hash)

        # Check if the transaction was successful
        if tx_receipt.status:
            response = {
                'status': 'success',
                'message': 'Ethereum node created successfully',
                'location_id': location_id,
                'name': name,
                'address': address,
                'city': city,
                'state': state,
                'country': country
            }
            return jsonify(response)
        else:
            response = {
                'status': 'error',
                'message': 'Failed to create Ethereum node'
            }
            return jsonify(response), 500
    except Exception as e:
        response = {
            'status': 'error',
            'message': 'An error occurred while creating Ethereum node',
            'error': str(e)
        }
        return jsonify(response), 500

if __name__ == '__main__':
    app.run(debug=True)
