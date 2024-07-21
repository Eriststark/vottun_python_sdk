# Vottun Python SDK

The Vottun Python SDK provides an interface for interacting with Ethereum-like blockchain networks. It allows you to deploy contracts, manage allowances, query balances, and handle transactions. This SDK is powered by Vottun APIs (Crypto (ERC-20) and Web3 Core). This SDK is already functional; however, I will probably update it and improve it over time, adding more functionality and features, and fixing any error of course.

If you do not want to install the sdk, you can just put your scripts inside the root folder of this repository and import the VottunClient class from the client.py file in your script, like shown in the example_usage.py file. You can try the pieces of code in the example_usage.py file; you just have to uncomment one and run that script. When instancing the VottunClient class, make sure to replace <your_api_key> and <your_app_id> with your own Vottun api key and app id. For more information about the Votttun APIs visit https://docs.vottun.io/.


## Installation

You can install the SDK either locally or globally.


### Local Installation

Clone the repository:

(bash)

        git clone <repository_url>

Navigate to the project directory:

(bash)

        cd vottun_python_sdk

(bash)

        pip install .


### Global Instalation

(bash)

        pip install <path_to_vottun_python_sdk>


## Usage

The SDK can be used programmatically in scripts or interactively via command line prompts.

You can use the SDK in your Python scripts as shown in the example_usage.py file. You can use it interactively by calling the prompt methods or just pass the values to the request classes to instance a new request object via code and then call the respective methods to get the responses.
