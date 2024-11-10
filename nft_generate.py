import json
from web3 import Web3
from solcx import compile_standard

# Connect to Infura or Alchemy (Ethereum Goerli testnet)
infura_url = "https://goerli.infura.io/v3/YOUR_INFURA_PROJECT_ID"
web3 = Web3(Web3.HTTPProvider(infura_url))

# Ensure connection
assert web3.is_connected(), "Unable to connect to the blockchain."

# Your Ethereum wallet (MetaMask) private key
private_key = "YOUR_PRIVATE_KEY"
account = web3.eth.account.from_key(private_key)
address = account.address

# Compile the contract
with open("MYnft.sol", "r") as file:
    nft_source_code = file.read()

compiled_sol = compile_standard(
    {
        "language": "Solidity",
        "sources": {"MyNFT.sol": {"content": nft_source_code}},
        "settings": {"outputSelection": {"*": {"*": ["abi", "evm.bytecode"]}}},
    }
)

# Get ABI and bytecode
abi = compiled_sol["contracts"]["MyNFT.sol"]["MyNFT"]["abi"]
bytecode = compiled_sol["contracts"]["MyNFT.sol"]["MyNFT"]["evm"]["bytecode"]["object"]

# Deploy the contract
contract = web3.eth.contract(abi=abi, bytecode=bytecode)
transaction = contract.constructor().build_transaction({
    "from": address,
    "nonce": web3.eth.get_transaction_count(address),
    "gas": 5000000,
    "gasPrice": web3.to_wei("20", "gwei"),
})

# Sign and send the transaction
signed_txn = web3.eth.account.sign_transaction(transaction, private_key)
tx_hash = web3.eth.send_raw_transaction(signed_txn.rawTransaction)
tx_receipt = web3.eth.wait_for_transaction_receipt(tx_hash)

print(f"Contract deployed at address: {tx_receipt.contractAddress}")
