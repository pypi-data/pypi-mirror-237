import unittest
import logging
import sys
from unittest.mock import  patch

sys.path.append("..")
from uledgersdk import ULedgerSDK 

API_KEY = ""
API_URL = "dev-services.uledger.net/api/v1/bms"

class TestULedgerSDKInitialization(unittest.TestCase):
    def test_valid_api_key(self):
        api_key = API_KEY
        sdk = ULedgerSDK(api_key)
        self.assertEqual(sdk.api_key, api_key)

    def test_missing_api_key(self):
        with self.assertRaises(ValueError):
            sdk = ULedgerSDK(None)

    def test_default_log_level(self):
        api_key = API_KEY
        sdk = ULedgerSDK(api_key)
        self.assertEqual(sdk.logger.level, logging.INFO)

    def test_custom_log_level(self):
        api_key = API_KEY
        custom_log_level = logging.INFO
        sdk = ULedgerSDK(api_key, log_level=custom_log_level)
        self.assertEqual(sdk.logger.level, custom_log_level)

    def test_default_headers(self):
        api_key = API_KEY
        sdk = ULedgerSDK(api_key)
        expected_headers = {
            "Authorization": api_key,
            "Content-Type": "application/json",
        }
        self.assertEqual(sdk.headers, expected_headers)

    def test_custom_headers(self):
        api_key = API_KEY
        custom_headers = {"Custom-Header": "Custom-Value"}
        sdk = ULedgerSDK(api_key, headers=custom_headers)
        self.assertEqual(sdk.headers, custom_headers)

class TestULedgerSDK(unittest.TestCase):
    @patch('requests.get')
    def test_send_get_request(self, mock_get):
        # Create an instance of ULedgerSDK
        sdk = ULedgerSDK(api_key=API_KEY)

        # Mock the requests.get method and return a sample response
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {"result": "success"}

        # Call the _send_request method with GET method
        response = sdk._send_request(url="example.com", method="GET", endpoint="test")

        # Assert that the mock method was called with the correct arguments
        mock_get.assert_called_once_with(
            "https://example.com/test", headers=sdk.headers, params=None
        )

        # Assert the response from the method
        self.assertEqual(response, {"result": "success"})

    @patch('requests.post')
    def test_send_post_request(self, mock_post):
        # Create an instance of ULedgerSDK
        sdk = ULedgerSDK(api_key=API_KEY)

        # Mock the requests.post method and return a sample response
        mock_post.return_value.status_code = 201
        mock_post.return_value.json.return_value = {"result": "created"}

        # Call the _send_request method with POST method
        data = {"key": "value"}
        response = sdk._send_request(url="example.com", method="POST", endpoint="test", data=data)

        # Assert that the mock method was called with the correct arguments
        mock_post.assert_called_once_with(
            "https://example.com/test",
            headers=sdk.headers,
            params=None,
            data='{"key": "value"}',
        )

        # Assert the response from the method
        self.assertEqual(response, {"result": "created"})

    @patch('uledgersdk.ULedgerSDK._send_request')
    def test_bms_info(self, mock_send_request):
        # Create an instance of ULedgerSDK
        sdk = ULedgerSDK(api_key="your_api_key")

        # Define mock response data
        mock_response_data = {
            "blockchain_count": 91,
            "block_count": 3383,
            "transaction_count": 36344
        }

        # Mock the _send_request method to return the desired response
        mock_send_request.return_value = mock_response_data

        # Call the bms_info method
        response = sdk.bms_info()

        # Assert that _send_request was called with the correct arguments
        mock_send_request.assert_called_once_with("dev-services.uledger.net/api/v1/bms", "GET", "service")

        # Assert the response from bms_info
        self.assertEqual(response, mock_response_data)

    @patch('uledgersdk.ULedgerSDK._send_request')
    def test_service_info(self, mock_send_request):
        # Create an instance of ULedgerSDK
        sdk = ULedgerSDK(api_key=API_KEY)
        mock_response_data = {
            "blockchain_count": 91,
            "block_count": 3383,
            "transaction_count": 36344
        }
        # Mock the _send_request method to return a sample response
        mock_send_request.return_value = mock_response_data

        # Call the _service_info method
        response = sdk.bms._service_info()

        # Assert that _send_request was called with the correct arguments
        mock_send_request.assert_called_once_with("dev-services.uledger.net/api/v1/bms","GET", "service")

        # Assert the response from _service_info
        self.assertEqual(response, mock_response_data)
    
    @patch('uledgersdk.ULedgerSDK._send_request')
    def test_get_blocks(self, mock_send_request):
        # Create an instance of ULedgerSDK
        sdk = ULedgerSDK(api_key=API_KEY)

        # Define mock response data
        
        mock_response_data = [{"block_id": 1}, {"block_id": 2}, {"block_id": 3}]

        # Mock the _send_request method to return the desired response
        mock_send_request.return_value = mock_response_data

        # Call the _get_blocks method
        limit = 10
        offset = 0
        sort = "asc"
        trim = True
        response = sdk.bms._get_blocks(limit, offset, sort, trim)

        # Assert that _send_request was called with the correct arguments
        expected_params = {"limit": limit, "offset": offset, "sort": sort, "trim": trim}
        mock_send_request.assert_called_once_with(API_URL,"GET", "block", params=expected_params)

        # Assert the response from _get_blocks
        self.assertEqual(response, mock_response_data)

    @patch('uledgersdk.ULedgerSDK.public_blocks')
    def test_public_blocks(self, mock_get_blocks):
        # Create an instance of ULedgerSDK
        sdk = ULedgerSDK(api_key=API_KEY)

        # Define mock response data for _get_blocks
        mock_response_data = [{"block_id": 1}, {"block_id": 2}, {"block_id": 3}]

        # Mock the _get_blocks method to return the desired response
        mock_get_blocks.return_value = mock_response_data

        # Call the blocks method
        limit = 10
        offset = 0
        sort = "asc"
        trim = True
        response = sdk.public_blocks(limit, offset, sort, trim)

        # Assert that _get_blocks was called with the correct arguments
        mock_get_blocks.assert_called_once_with(limit, offset, sort, trim)

        # Assert the response from blocks
        self.assertEqual(response, mock_response_data)

    @patch('uledgersdk.core.ULedgerSDK.list_blocks')
    def test_list_blocks(self, mock_list_blocks):
        # Create an instance of ULedgerSDK
        sdk = ULedgerSDK(api_key=API_KEY)

        # Mock the list_blocks method of the BMS class
        mock_list_blocks.return_value = [{"block_id": "block1"}, {"block_id": "block2"}]

        # Call the list_blocks method
        blockchain_id = "test_blockchain"
        limit = 10
        offset = 0
        sort = "timestamp"
        trim = True
        response = sdk.list_blocks(blockchain_id, limit, offset, sort, trim)

        # Assert that _get_blockchain_blocks was called with the correct parameters
        mock_list_blocks.assert_called_once_with(blockchain_id, limit, offset, sort, trim)

        # Assert the response from list_blocks
        expected_response = [{"block_id": "block1"}, {"block_id": "block2"}]
        self.assertEqual(response, expected_response)

    @patch('uledgersdk.core.ULedgerSDK._send_request')
    def test_get_blockchain_blocks(self, mock_send_request):
        # Create an instance of ULedgerSDK
        sdk = ULedgerSDK(api_key=API_KEY)

        # Mock the _send_request method of the SDK
        mock_send_request.return_value = [{"block_id": "block1"}, {"block_id": "block2"}]

        # Call the _get_blockchain_blocks method
        blockchain_id = "test_blockchain"
        limit = 10
        offset = 0
        sort = "timestamp"
        trim = True
        response = sdk.bms._get_blockchain_blocks(blockchain_id, limit, offset, sort, trim)

        # Assert that _send_request was called with the correct parameters
        expected_url = f"{API_URL}"
        expected_endpoint = f"block/{blockchain_id}/preview"
        expected_params = {"limit": limit, "offset": offset, "sort": sort, "trim": trim}
        expected_call_args = (
            expected_url,
            "GET",
            expected_endpoint,
        )
        expected_call_kwargs = {
            "params": expected_params,  # Use params instead of the direct parameter
        }
        mock_send_request.assert_called_once_with(*expected_call_args, **expected_call_kwargs)

        # Assert the response from _get_blockchain_blocks
        expected_response = [{"block_id": "block1"}, {"block_id": "block2"}]
        self.assertEqual(response, expected_response)

    @patch('uledgersdk.core.ULedgerSDK._send_request')
    def test_search_block(self, mock_send_request):
        # Create an instance of ULedgerSDK
        sdk = ULedgerSDK(api_key=API_KEY)

        # Define the expected block ID
        block_id = "abc123"

        # Define the expected URL and endpoint
        expected_url = API_URL
        expected_endpoint = f"block/{block_id}/list"

        # Define a mock response
        mock_response = {"block_id": block_id, "data": "block_data"}
        mock_send_request.return_value = mock_response

        # Call the search_block method
        response = sdk.search_block(block_id)

        # Assert that _send_request was called with the expected arguments
        mock_send_request.assert_called_once_with(expected_url, "GET", expected_endpoint)

        # Assert the response
        self.assertEqual(response, mock_response)

    @patch('uledgersdk.core.ULedgerSDK._send_request')
    def test_search_block(self, mock_send_request):
        # Create an instance of ULedgerSDK
        sdk = ULedgerSDK(api_key=API_KEY)

        # Define the expected block ID
        block_id = "abc123"

        # Define the expected URL and endpoint
        expected_url = API_URL
        expected_endpoint = f"block/{block_id}/list"

        # Define a mock response
        mock_response = {"block_id": block_id, "data": "block_data"}
        mock_send_request.return_value = mock_response

        # Call the _search_block method
        response = sdk.bms._search_block(block_id)

        # Assert that _send_request was called with the expected arguments
        mock_send_request.assert_called_once_with(expected_url, "GET", expected_endpoint)

        # Assert the response
        self.assertEqual(response, mock_response)
    @patch('uledgersdk.core.ULedgerSDK._send_request')
    def test_search_transaction(self, mock_send_request):
        # Create an instance of ULedgerSDK
        sdk = ULedgerSDK(api_key=API_KEY)

        # Define the expected transaction ID and trim flag
        transaction_id = "123abc"
        trim = True

        # Define the expected URL and endpoint
        expected_url = API_URL
        expected_endpoint = f"transaction/{transaction_id}/list?trim=true"

        # Define a mock response
        mock_response = {"transaction_id": transaction_id, "data": "transaction_data"}
        mock_send_request.return_value = mock_response

        # Call the search_transaction method
        response = sdk.search_transaction(transaction_id, trim=trim)

        # Assert that _send_request was called with the expected arguments
        mock_send_request.assert_called_once_with(expected_url, "GET", expected_endpoint)

        # Assert the response
        self.assertEqual(response, mock_response)

    @patch('uledgersdk.core.ULedgerSDK._send_request')
    def test__search_transaction(self, mock_send_request):
        # Create an instance of ULedgerSDK
        sdk = ULedgerSDK(api_key=API_KEY)

        # Define the expected transaction ID and trim flag
        transaction_id = "123abc"
        trim = False

        # Define the expected URL and endpoint
        expected_url = API_URL
        expected_endpoint = f"transaction/{transaction_id}/list?trim=false"

        # Define a mock response
        mock_response = {"transaction_id": transaction_id, "data": "transaction_data"}
        mock_send_request.return_value = mock_response

        # Call the _search_transaction method
        response = sdk.bms._search_transaction(transaction_id, trim=trim)

        # Assert that _send_request was called with the expected arguments
        mock_send_request.assert_called_once_with(expected_url, "GET", expected_endpoint)

        # Assert the response
        self.assertEqual(response, mock_response)

    @patch('uledgersdk.core.ULedgerSDK._send_request')
    def test__get_transactions_with_blockchain_id(self, mock_send_request):
        # Create an instance of ULedgerSDK
        sdk = ULedgerSDK(api_key=API_KEY)

        # Define the expected blockchain ID, limit, offset, sort, and trim values
        blockchain_id = "test_blockchain"
        limit = 5
        offset = 2
        sort = False
        trim = False

        # Define the expected URL and endpoint
        expected_url = API_URL
        expected_endpoint = f"transaction/{blockchain_id}/preview?limit={limit}&offset={offset}&sort=false&trim=false"

        # Define a mock response
        mock_response = {"transactions": ["transaction1", "transaction2"]}
        mock_send_request.return_value = mock_response

        # Call the _get_transactions method with a blockchain ID
        response = sdk.bms._get_transactions(
            blockchain_id=blockchain_id, limit=limit, offset=offset, sort=sort, trim=trim
        )

        # Assert that _send_request was called with the expected arguments
        mock_send_request.assert_called_once_with(expected_url, "GET", expected_endpoint)

        # Assert the response
        self.assertEqual(response, mock_response)

    @patch('uledgersdk.core.ULedgerSDK._send_request')
    def test__get_transactions_no_blockchain_id(self, mock_send_request):
        # Create an instance of ULedgerSDK
        sdk = ULedgerSDK(api_key=API_KEY)

        # Define the expected limit, offset, sort, and trim values
        limit = 10
        offset = 0
        sort = True
        trim = True

        # Define the expected URL and endpoint for public transactions
        expected_url = API_URL
        expected_endpoint = f"transaction?limit={limit}&offset={offset}&sort=true&trim=true"

        # Define a mock response
        mock_response = {"transactions": ["transaction1", "transaction2"]}
        mock_send_request.return_value = mock_response

        # Call the _get_transactions method without a blockchain ID
        response = sdk.bms._get_transactions(
            blockchain_id=None, limit=limit, offset=offset, sort=sort, trim=trim
        )

        # Assert that _send_request was called with the expected arguments
        mock_send_request.assert_called_once_with(expected_url, "GET", expected_endpoint)

        # Assert the response
        self.assertEqual(response, mock_response)

    @patch('uledgersdk.core.ULedgerSDK.list_transactions')
    def test_list_transactions_with_blockchain_id(self, mock_get_transactions):
        # Create an instance of ULedgerSDK
        sdk = ULedgerSDK(api_key=API_KEY)

        # Define the expected blockchain ID, limit, offset, sort, and trim values
        blockchain_id = "test_blockchain"
        limit = 5
        offset = 2
        sort = False
        trim = False

        # Define a mock response
        mock_response = {"transactions": ["transaction1", "transaction2"]}
        mock_get_transactions.return_value = mock_response

        # Call the list_transactions method with a blockchain ID
        response = sdk.list_transactions(
            blockchain_id=blockchain_id, limit=limit, offset=offset, sort=sort, trim=trim
        )

        # Assert that _get_transactions was called with the expected arguments
        mock_get_transactions.assert_called_once_with(
            blockchain_id=blockchain_id, limit=limit, offset=offset, sort=sort, trim=trim
        )

        # Assert the response
        self.assertEqual(response, mock_response)

    @patch('uledgersdk.core.ULedgerSDK.list_transactions')
    def test_list_transactions_no_blockchain_id(self, mock_get_transactions):
        # Create an instance of ULedgerSDK
        sdk = ULedgerSDK(api_key=API_KEY)

        # Define the expected limit, offset, sort, and trim values
        limit = 10
        offset = 0
        sort = True
        trim = True

        # Define a mock response
        mock_response = {"transactions": ["transaction1", "transaction2"]}
        mock_get_transactions.return_value = mock_response

        # Call the list_transactions method without a blockchain ID
        response = sdk.list_transactions(
            blockchain_id=None, limit=limit, offset=offset, sort=sort, trim=trim
        )

        # Assert that _get_transactions was called with the expected arguments
        mock_get_transactions.assert_called_once_with(
            blockchain_id=None, limit=limit, offset=offset, sort=sort, trim=trim
        )

        # Assert the response
        self.assertEqual(response, mock_response)

    @patch('uledgersdk.core.ULedgerSDK._send_request')
    def test_block_transactions(self, mock_send_request):
        # Create an instance of ULedgerSDK
        sdk = ULedgerSDK(api_key=API_KEY)

        # Define the expected block ID, limit, offset, sort, and trim values
        block_id = "test_block"
        limit = 5
        offset = 2
        sort = False
        trim = False

        # Define the expected URL and endpoint
        expected_url = API_URL
        expected_endpoint = f"transaction/{block_id}/block?limit={limit}&offset={offset}&sort=false&trim=false"

        # Define a mock response
        mock_response = {"transactions": ["transaction1", "transaction2"]}
        mock_send_request.return_value = mock_response

        # Call the block_transactions method
        response = sdk.block_transactions(
            block_id=block_id, limit=limit, offset=offset, sort=sort, trim=trim
        )

        # Assert that _send_request was called with the expected arguments
        mock_send_request.assert_called_once_with(expected_url, "GET", expected_endpoint)

        # Assert the response
        self.assertEqual(response, mock_response)

    @patch('uledgersdk.core.ULedgerSDK._send_request')
    def test__get_block_transactions(self, mock_send_request):
        # Create an instance of ULedgerSDK
        sdk = ULedgerSDK(api_key=API_KEY)

        # Define the expected block ID, limit, offset, sort, and trim values
        block_id = "test_block"
        limit = 5
        offset = 2
        sort = False
        trim = False

        # Define the expected URL and endpoint
        expected_url = API_URL
        expected_endpoint = f"transaction/{block_id}/block?limit={limit}&offset={offset}&sort=false&trim=false"

        # Define a mock response
        mock_response = {"transactions": ["transaction1", "transaction2"]}
        mock_send_request.return_value = mock_response

        # Call the _get_block_transactions method
        response = sdk.bms._get_block_transactions(
            block_id=block_id, limit=limit, offset=offset, sort=sort, trim=trim
        )

        # Assert that _send_request was called with the expected arguments
        mock_send_request.assert_called_once_with(expected_url, "GET", expected_endpoint)

        # Assert the response
        self.assertEqual(response, mock_response)
    
    @patch('uledgersdk.core.ULedgerSDK.create_transaction')
    def test_create_transaction(self, mock_create_transaction):
        # Create an instance of ULedgerSDK
        sdk = ULedgerSDK(api_key=API_KEY)

        # Define the expected parameters for creating a transaction
        node_address = "node_address"
        blockchain_id = "blockchain_id"
        to = "recipient_address"
        from_ = "sender_address"
        atomic_timestamp = "2023-10-10T10:00:00Z"
        payload = "Transaction data"
        sender_signature = "signature"
        payload_type = "DATA"

        # Define a mock response for creating a transaction
        mock_response = {"transaction_id": "12345"}
        mock_create_transaction.return_value = mock_response

        # Call the create_transaction method
        response = sdk.create_transaction(
            node_address=node_address,
            blockchain_id=blockchain_id,
            to=to,
            from_=from_,
            atomic_timestamp=atomic_timestamp,
            payload=payload,
            sender_signature=sender_signature,
            payload_type=payload_type,
        )

        # Assert that _create_transaction was called with the expected arguments
        mock_create_transaction.assert_called_once_with(
            node_address=node_address,
            blockchain_id=blockchain_id,
            to=to,
            from_=from_,
            atomic_timestamp=atomic_timestamp,
            payload=payload,
            sender_signature=sender_signature,
            payload_type=payload_type,
        )

        # Assert the response
        self.assertEqual(response, mock_response)

if __name__ == "__main__":
    unittest.main()
