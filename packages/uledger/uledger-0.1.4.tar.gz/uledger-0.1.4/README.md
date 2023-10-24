# Python SDK for ULedger

## Introduction

Welcome to the ULedger Python SDK! This guide will help you get started quickly with the SDK, allowing you to integrate it into your projects and interact with the ULedger blockchain platform.

### Prerequisites

Before you begin, make sure you have the following prerequisites in place:

- [Python](https://www.python.org/) (version 3.8 or higher) installed on your system.
- A valid ULedger blockchain account or access to a ULedger blockchain node.
- [Git](https://git-scm.com/) installed on your system (for code management).

## Getting Started

To start using the ULedger Python SDK, follow these steps:

1. **Installation**: You can install the SDK by cloning the repository and running the following command in the root path of the directory:
   ```bash
   git clone git@gitlab.com:uledger/development/sdk/python-sdk.git
   pip install .
   ```
2. **Impport the SDK**: Import the SDK into your Python project:
    ```python
    from uledgersdk import ULedgerSDK
    ```
3. **Initialize the SDK**: Create an instance of the SDK by providing your API key or credentials:
    ```python
    api_key = "your_api_key_here"
    sdk = ULedgerSDK(api_key)
    ```
4. **BMS Information**: Retrieve information about the BMS service.
    ```python
    service_info = sdk.bms_info()
    print("Service Info:", service_info)
    ```
5. **Create transaction**: Create a new transaction within the blockchain network, expect the following parameters.
    - node_address: The address of the node responsible for processing the transaction.
    - blockchain_id: Identifier of the blockchain where the transaction will be added.
    - to: The recipient's address or destination within the blockchain.
    - from: The sender's address or source within the blockchain.
    - atomic_timestamp: The timestamp representing the moment of the transaction's creation.
    - payload: The content or data to be included in the transaction.
    - sender_signature: The digital signature of the transaction sender.
    - payload_type: The type of payload being included in the transaction (default is "DATA").

    Usage:
    ```python
    response = sdk.create_transaction(
        node_address="SomeNodeHTTPAddress",
        blockchain_id="SomeBlockchainId",
        to="User1",
        from_="User2",
        atomic_timestamp="5544",
        payload={"data": "informational transaction being sent here"},
        sender_signature="1234567890",
    )
    print("Creating a transaction:", response)
    ```
6. **Search transaction**: Search for a transaction by its unique ID.
    - transaction_id: Unique identifier of the transaction.
    - trim: Trim the response to essentials (optional).
    ```python
    transaction_id = "686767a715374715e1a43bec6275f7ded1e87abad9ac69c3e9287825b7f59a82"
    transaction = sdk.search_transaction(transaction_id)
    print("Transaction Information:", transaction)
    ```

7. **List transactions**: Retrieve transactions from a blockchain based on the given parameters..
    - blockchain_id: Unique ID of the blockchain (optional).
    - limit: Limit for the number of results.
    - offset: Offset for paginating results.
    - sort: Sort results.
    - trim: Trim the response to essentials.

    ```python
    transactions = sdk.list_transactions(blockchain_id="SomeBlockchainId", limit=10, offset=0, sort=True, trim=True)
    print("Transactions from Blockchain:", transactions)
    ```

8. **List block transactions**: Retrieve transactions from a blockchain based on the given parameters..
    - block_id: Identifier of the block.
    - limit: Limit for the number of results.
    - offset: Offset for paginating results.
    - sort: Sort results.
    - trim: Trim the response to essentials.

    ```python
    block_id = "bfa57cc9d953385daa5b09abc67430a9d226b4f4cb25a70ba11437e53db0ed74"
    transactions = sdk.block_transactions(block_id, limit=10, offset=0, sort=True, trim=True)
    print("Transactions in Block:", transactions)
    ```
9. **List blocks**: Retrieve blocks from a specific blockchain.
    - blockchain_id: Unique ID of the blockchain (optional).
    - limit: Limit for the number of results.
    - offset: Offset for paginating results.
    - sort: Sort results.
    - trim: Trim the response to essentials.

    ```python
    blocks = sdk.list_blocks(blockchain_id="SampleBlockchainId", limit=10, offset=0, sort=True, trim=True)
    print("Blocks from Blockchain:", blocks)
    ```

10. **List blocks**: Retrieve blocks from a specific blockchain.
    - block_id: Unique identifier of the block.
    ```python
    block_id = "de7328cb0661e68b6921b0055185986a09838496eceaae6c8c20a55efee13668"
    block = sdk.search_block(block_id)
    print("Block Information:", block)
    ```

10. **List public blocks**: Retrieve public blocks based on the given parameters.
    - limit: Limit for the number of results.
    - offset: Offset for paginating results.
    - sort: Sort results.
    - trim: Trim the response to essentials.
    ```python
    blocks_10 = sdk.blocks(limit=10, offset=0, sort="asc", trim=True)
    print("First 10 Blocks:", blocks_10)
    ```

## Testing
To run unit tests add a proper API_KEY authorized to perform requests to your organization and run, from the root directory:
```bash
python -m unittest tests/test_core.py
```
## Roadmap
- TODO: Add proper exception handlers: Make sure to handle exceptions gracefully in your code.
- TODO: Implement searchBlocksandTransactions endpoint: Provide details about the searchBlocksandTransactions endpoint.
- ~~DONE: Implement getServiceData: Use the getServiceData method to fetch service information.~~
- TODO: Implement serachPublicBlocksAndTransactions endpoint: Describe the serachPublicBlocksAndTransactions endpoint.
- ~~DONE: Implement searchBlockById: Use the searchBlockById method to search for a block by its ID.~~
- ~~DONE: Implement listBlocks: Describe how to list blocks in a blockchain.~~
- ~~DONE: Implement listTransactions: Explain how to list transactions.~~
- ~~DONE: Implement searchTransactionById: Describe how to search for a transaction by its ID.~~
- ~~DONE: Implement listPublicTransactions: Explain how to list public transactions.~~
- ~~DONE: Implement transactionsFromBlock: Provide details on fetching transactions from a specific block.~~
- ~~DONE: Implement userHistory: Describe how to retrieve user history.~~
- TODO: Add the proper solution for the verification requirements: Placeholder for verification requirements.

### Wallets
- TODO: Generate Seed Wallet Phrase: Explain how to generate a seed wallet phrase.
- TODO: Create Wallet Seed Phrase: Describe the process of creating a wallet seed phrase.
- TODO: Load Wallet File Using the SDK: Explain how to load a wallet file using the SDK.
- TODO: Sign Transactions Using the Wallet: Describe how to sign transactions with a wallet.
- TODO: Register Wallet to Blockchain: Explain the process of registering a wallet to the blockchain.

