import json
import getpass
from Crypto.Cipher import AES
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Random import get_random_bytes
import base64

class WalletManager:
    """
    A manager for cryptocurrency wallets.
    Allows adding wallets, saving them to a file, loading them from a file and decrypting the private keys.
    """

    def __init__(self):
        """
        Initializes a new WalletManager instance.
        """
        self.wallets = []

    def add_wallet(self, wallet_type, operation, public_address, private_key):
        """
        Adds a wallet to the manager.

        :param wallet_type: The type of the wallet (e.g., 'bitcoin', 'evm').
        :param operation: The operation related to this wallet (e.g., 'trader', 'hodl').
        :param public_address: The public address of the wallet.
        :param private_key: The private key of the wallet.
        """
        salt = get_random_bytes(AES.block_size)

        private_key = private_key.encode('utf-8')
        key = PBKDF2(getpass.getpass("Enter encryption password: "), salt, dkLen=32)

        cipher = AES.new(key, AES.MODE_EAX)
        ciphertext, tag = cipher.encrypt_and_digest(private_key)

        wallet = {
            'type': wallet_type,
            'operation': operation,
            'public_address': public_address,
            'private_key': base64.b64encode(ciphertext).decode('utf-8'),
            'nonce': base64.b64encode(cipher.nonce).decode('utf-8'),
            'salt': base64.b64encode(salt).decode('utf-8')
        }
        self.wallets.append(wallet)

    def save(self, filename):
        """
        Saves the wallets to a JSON file.

        :param filename: The name of the file to save the wallets to.
        """
        with open(filename, 'w') as f:
            json.dump(self.wallets, f)

    def load(self, filename):
        """
        Loads the wallets from a JSON file.

        :param filename: The name of the file to load the wallets from.
        """
        with open(filename, 'r') as f:
            self.wallets = json.load(f)

    def decrypt_private_key(self, wallet):
        """
        Decrypts the private key of a wallet.

        :param wallet: The wallet whose private key needs to be decrypted.
        :return: The decrypted private key.
        """
        salt = base64.b64decode(wallet['salt'])
        nonce = base64.b64decode(wallet['nonce'])
        ciphertext = base64.b64decode(wallet['private_key'])

        key = PBKDF2(getpass.getpass("Enter encryption password: "), salt, dkLen=32)

        cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
        private_key = cipher.decrypt(ciphertext).decode('utf-8')

        return private_key
