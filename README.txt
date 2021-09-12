https://www.freecodecamp.org/news/how-to-make-an-nft-and-render-on-opensea-marketplace/

https://ipfs.io/ipfs/QmX2T6xvEqjNEQwJT9Z6UMRV9GLWCErPveAG1VmfgcBymp?filename=0-GRUMPY_CAT.json
https://ipfs.io/ipfs/QmdnRfUR4RhJTvrGwqZuLrVn4biFDU7PwjowhAWbziMsSM?filename=cat.jpeg
https://testnets.opensea.io/

$ brownie run scripts/advanced_collectible/deploy_advanced.py --network rinkeby
$ brownie run scripts/advanced_collectible/create_collectible.py --network rinkeby
$ brownie run scripts/advanced_collectible/create_metadata.py --network rinkeby
$ brownie run scripts/advanced_collectible/set_tokenuri.py --network rinkeby 
