from web3 import Web3

def sendTransaction(message):
    w3 = Web3(Web3.HTTPProvider('https://goerli.infura.io/v3/b51ab601fbea4871845fe9f621bc9746'))
    address = '0x48211E0f054007648fBE6fdd3993FC6292057cE2'
    privateKey = '0xe8e750a25fdb0a42377ca57442a2fc311dfc1ddc7cc50c5ac5b72e53459f411b'
    nonce = w3.eth.getTransactionCount(address)
    gasPrice = w3.eth.gasPrice
    value = w3.toWei(0,'ether')
    signedTx = w3.eth.account.signTransaction(dict(
        nonce=nonce,
        gasPrice=gasPrice,
        gas=100000,
        to='0x0000000000000000000000000000000000000000',
        value=value,
        data=message.encode('utf-8')
    ), privateKey)

    tx = w3.eth.sendRawTransaction(signedTx.rawTransaction)
    txId = w3.toHex(tx)
    return txId