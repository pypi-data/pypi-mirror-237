import unittest
from unittest.mock import patch


from uledgersdk.core import ULedgerWalletGenerator, ULedgerWallet, ULedgerWalletFactory
from uledgersdk.exceptions import InvalidSeedException, InvalidWordCount

class TestWalletGenerator(unittest.TestCase):
  def test_get_seed_words_valid(self):
        # Test with valid input
        seed_words = ULedgerWalletGenerator.get_seed_words(12, 'en')
        self.assertEqual(len(seed_words), 12)
        # Ensure all words are unique
        self.assertEqual(len(set(seed_words)), len(seed_words))
    
  def test_get_seed_words_invalid_count_minimum(self):
        # Test with invalid word count
        with self.assertRaises(ValueError) as context:
            ULedgerWalletGenerator.get_seed_words(11, 'en')  # count is below the minimum
        self.assertEqual(str(context.exception), 'Invalid seed words count')

  def test_get_seed_words_invalid_count_maximum(self):
        # Test with invalid word count
        with self.assertRaises(ValueError) as context:
            ULedgerWalletGenerator.get_seed_words(68, 'en')  # count is above the maximum
        self.assertEqual(str(context.exception), 'Invalid seed words count')

  def test_get_seed_words_invalid_language(self):
      # Test with invalid language
      with self.assertRaises(ValueError) as context:
          ULedgerWalletGenerator.get_seed_words(12, 'invalid_language')
      self.assertEqual(str(context.exception), 'Invalid language')

  def test_generate_wallet_with_valid_words(self):
      # Test with valid input
      seed_words = ULedgerWalletGenerator.get_seed_words(12, 'en')
      wallet = ULedgerWalletGenerator.create_wallet(seed_words, 'en')

      self.assertIsNotNone(wallet)
      # Valid values from the wallet
      self.assertIsNotNone(wallet.get_public_key_hex())
      self.assertIsNotNone(wallet.get_wallet_address())

  def test_generate_wallet_with_invalid_word_count(self):
      # Test with invalid words
      with self.assertRaises(InvalidWordCount):
          ULedgerWalletGenerator.create_wallet(['invalid', 'words'], 'en')

  def test_generate_wallet_with_invalid_words(self):
      # Test with invalid words
      invalid_word_list = ['invalid', 'words', 'invalid', 'words', 'invalid', 'words', 'invalid', 'words', 'invalid', 'words', 'invalid', 'words']
      with self.assertRaises(InvalidSeedException):
          ULedgerWalletGenerator.create_wallet(invalid_word_list, 'en')


class TestULedgerWalletFactory(unittest.TestCase):

    def test_serialize_and_deserialize_without_password(self):
        # Create a wallet instance
        seed_words = ULedgerWalletGenerator.get_seed_words(12, 'en')
        wallet = ULedgerWalletGenerator.create_wallet(seed_words, 'en')

        # Serialize the wallet
        serialized_wallet = ULedgerWalletFactory.serialize(wallet)

        # Deserialize the wallet
        deserialized_wallet = ULedgerWalletFactory.deserialize(serialized_wallet)

        # Validate the deserialized wallet against the original
        self.assertEqual(wallet.to_dict(), deserialized_wallet.to_dict())

    def test_serialize_and_deserialize_with_password(self):
        # Create a wallet instance
        seed_words = ULedgerWalletGenerator.get_seed_words(12, 'en')
        wallet = ULedgerWalletGenerator.create_wallet(seed_words, 'en')
        
        # Define a password
        password = 'MyPassword'

        # Serialize the wallet with password encryption
        serialized_wallet = ULedgerWalletFactory.serialize(wallet, password)

        # Deserialize the wallet with the correct password
        deserialized_wallet = ULedgerWalletFactory.deserialize(serialized_wallet, password)

        # Validate the deserialized wallet against the original
        self.assertEqual(wallet.to_dict(), deserialized_wallet.to_dict())

        # Attempt to deserialize the wallet with an incorrect password, expecting a ValueError
        with self.assertRaises(ValueError):
            ULedgerWalletFactory.deserialize(serialized_wallet, 'wrongpassword')

class TestULedgerWallet(unittest.TestCase):

    def setUp(self) -> None:
        seed_words = ULedgerWalletGenerator.get_seed_words(12, 'en')
        self.wallet = ULedgerWalletGenerator.create_wallet(seed_words, 'en')
        return super().setUp()
    

    def test_sign_and_verify_message(self):
        # Sign a message
        message = 'This is a test message'
        signature = self.wallet.sign_message(message)

        # Verify the signature
        self.assertTrue(self.wallet.verify_signature(message, signature))

    def test_sign_and_verify_message_with_invalid_signature(self):
        # Sign a message
        message = 'This is a test message'
        signature = self.wallet.sign_message(message)

        # Verify the signature
        self.assertFalse(self.wallet.verify_signature(message, signature + 'invalid'))

    def test_sign_and_verify_message_with_invalid_message(self):
        # Sign a message
        message = 'This is a test message'
        signature = self.wallet.sign_message(message)

        # Verify the signature
        self.assertFalse(self.wallet.verify_signature(message + 'invalid', signature))

    @patch('requests.post')
    def test_register_wallet(self, mock_post):

        # Mock the response
        mock_post.return_value.status_code = 201

        # Register the wallet
        blockchain_id = '1234567890'
        node_url = 'https://test.com'
        self.wallet.register_wallet(blockchain_id, node_url)

        # Validate the request
        mock_post.assert_called_once_with(
            f'{node_url}/blockchain/{blockchain_id}/wallet',
            data='{\"public_key\": \"' + self.wallet.get_public_key_hex() + '\"}',
        )

    @patch('requests.post')
    def test_register_wallet_with_error(self, mock_post):

        # Mock the response
        mock_post.side_effect = Exception('Network error')

        # Register the wallet
        blockchain_id = '1234567890'
        node_url = 'https://test.com'

        # Attempt to register the wallet and confirm that an exception is raised
        with self.assertRaises(ValueError) as context:
            self.wallet.register_wallet(blockchain_id, node_url)

        self.assertEqual(str(context.exception), 'Error registering wallet: Network error')



if __name__ == '__main__':
    unittest.main()