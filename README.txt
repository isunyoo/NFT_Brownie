NFT Python
https://www.freecodecamp.org/news/how-to-make-an-nft-and-render-on-opensea-marketplace/
https://betterprogramming.pub/how-to-create-nfts-with-solidity-4fa1398eb70a
https://opensea.io
https://testnets.opensea.io/


Simple NFT without setting a tokenURI
$ brownie run scripts/simple_collectible/deploy_simple.py --network rinkeby
$ brownie run scripts/simple_collectible/create_collectible.py --network rinkeby

Dynamic and Advanced NFTs
$ brownie run scripts/advanced_collectible/deploy_advanced.py --network rinkeby
$ brownie run scripts/advanced_collectible/create_collectible.py --network rinkeby
$ brownie run scripts/advanced_collectible/create_metadata.py --network rinkeby
$ brownie run scripts/advanced_collectible/set_tokenuri.py --network rinkeby 


$ brownie networks modify development explorer=https://api.etherscan.io/api
$ brownie networks modify development explorer=$ETHERSCAN_API

Test#1: api?module=account&action=balance&address=0xddbd2b932c763ba5b1b7ae3b362eac3e8d40121a&tag=latest&apikey=YourApiKeyToken
Test#2: api/api?module=account&action=txlist&address=0xddbd2b932c763ba5b1b7ae3b362eac3e8d40121a&startblock=0&endblock=99999999&page=1&offset=10&sort=asc&apikey=YourApiKeyToken
https://api.etherscan.io/api?module=account&action=balance&address=0xde0b295669a9fd93d5f28d9ec85e40f4cb697bae&tag=latest&apikey=YourApiKeyToken