from main import WalletManager

# Create instance of WalletManager
manager = WalletManager()

# Add first wallet
manager.add_wallet('bitcoin', 'buy', '1BvBMSEYstWetqTFn5Au4m4GFg7xJaNVN2', 'PRIVATE_KEY1_HERE')

# Add second wallet
manager.add_wallet('ethereum', 'sell', '0x742d35Cc6634C0532925a3b844Bc454e4438f44e', 'PRIVATE_KEY2_HERE')

# Save wallets to a file
manager.save('trade-wallets.json')

# Load wallets from a file
manager.load('trade-wallets.json')

# Access first wallet and decrypt its private key
wallet1 = manager.wallets[0]
print("First wallet decrypted private key: ", manager.decrypt_private_key(wallet1))

# Access second wallet and decrypt its private key
wallet2 = manager.wallets[1]
print("Second wallet decrypted private key: ", manager.decrypt_private_key(wallet2))
