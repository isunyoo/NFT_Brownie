from brownie import Contrat1, accounts

def main():
    compte = accounts.load('MY_ACCOUNT1')
    t = Contrat1.deploy({'from': compte})