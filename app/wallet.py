from web3 import Web3

w3 = Web3(Web3.HTTPProvider("https://goerli.infura.io/v3/b51ab601fbea4871845fe9f621bc9746"))
account = w3.eth.account.create()
privateKey = account.privateKey.hex()
address = account.address

print(address)
print(privateKey)