# Vottun Python SDK

The Vottun Python SDK provides an interface for interacting with Ethereum-like blockchain networks. It allows you to deploy contracts, manage allowances, query balances, and handle transactions. This SDK is powered by Vottun APIs, especically Web3 Core and Crypto (ERC-20). This SDK is already functional; however, I will probably update it and improve it over time, adding  more functionality and features.

# Installation

You can install the SDK either locally or globally.

## Local Installation

1.  Clone the repository:

(bash)

    git clone <repository_url>


2.  Navigate to the project directory:

(bash)

    cd vottun_python_sdk

(bash)

    pip install .

## Install the SDK globally:

(bash)

    pip install <path_to_vottun_python_sdk>

If you do not want to install the sdk, you can just put your scripts inside the root folder of this repository and import the VottunClient class from the client.py file in your script, like shown in the example_usage.py file. You can try the pieces of code in the example_usage.py file; you just have to uncomment one and run that script in your terminal. When instancing the VottunClient class , make sure to replace <api_key> and <app_id> with your own Vottun api key and app id.

## Usage

The SDK can be used programmatically in scripts or interactively via command line prompts.
Programmatic Usage

You can use the SDK in your Python scripts as shown in the example_usage.py file. You can use it interactively by calling the prompt methods or just pass the values to the request classes to instance a new request object via code and then call the repective methods to get the responses.
