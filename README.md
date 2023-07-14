# Wallet Manager

Wallet Manager is a Python Class that allows managing multiple cryptocurrency wallets in one place. It supports adding wallets, saving them to a file, loading them from a file, and decrypting the private keys.

## Installation

You need Python 3.7 or later to run the Wallet Manager. You can check your Python version by running `python --version`.

You can install the required Python packages by running the following command:

```
pip install -r requirements.txt
```

## Usage

First, import the WalletManager class from the main.py file:

```python
from main import WalletManager
```

Create an instance of the WalletManager class:

```
manager = WalletManager()
```

Add a wallet to the manager:

```
manager.add_wallet('bitcoin', 'hodl', 'public_address_here', 'private_key_here')
```

Save the wallets to a file:

```
manager.save('wallets.json')
```

Load the wallets from a file:
```
manager.load('wallets.json')
```

Decrypt the private key of a wallet:

```
wallet = manager.wallets[0]
print("Decrypted private key: ", manager.decrypt_private_key(wallet))
```

## License

Wallet Manager is licensed under the terms of the MIT license. For more information