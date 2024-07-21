class DeployRequest:
    def __init__(self, name, symbol, alias, initialSupply, network):
        self.name = name
        self.symbol = symbol
        self.alias = alias
        self.initialSupply = initialSupply
        self.network = network

    def __repr__(self):
        return (f"DeployRequest("
                f"name={self.name!r}, "
                f"symbol={self.symbol!r}, "
                f"alias={self.alias!r}, " 
                f"initialSupply={self.initialSupply!r}, "
                f"network={self.network!r})")

    def __str__(self):
        return (f"Deploy Request:\n"
                f"  Name: {self.name}\n"
                f"  Symbol: {self.symbol}\n"
                f"  Alias: {self.alias}\n"
                f"  Initial Supply: {self.initialSupply}\n"
                f"  Network: {self.network}")


class DeployResponse(DeployRequest):
    def __init__(self, name, symbol, alias, initialSupply, network, contractAddress, txHash):
        super().__init__(name, symbol, alias, initialSupply, network)
        self.contractAddress = contractAddress
        self.txHash = txHash

    def __repr__(self):
        return (f"DeployResponse("
                f"name={self.name!r}, "
                f"symbol={self.symbol!r}, "
                f"alias={self.alias!r}, "    
                f"initialSupply={self.initialSupply!r}, "
                f"network={self.network!r}, "
                f"contractAddress={self.contractAddress!r}, "
                f"txHash={self.txHash!r})")

    def __str__(self):
        return (f"      Deploy Response:\n"
                f"          Name: {self.name}\n"
                f"          Symbol: {self.symbol}\n"
                f"          Alias: {self.alias}\n"    
                f"          Initial Supply: {self.initialSupply}\n"
                f"          Network: {self.network}\n"
                f"          Contract Address: {self.contractAddress}\n"
                f"          Transaction Hash: {self.txHash}")


    @classmethod
    def from_deploy_request(cls, deploy_request: DeployRequest, contractAddress, txHash) -> 'DeployResponse':
                return cls(
            deploy_request.name,
            deploy_request.symbol,
            deploy_request.alias,
            deploy_request.initialSupply,
            deploy_request.network,
            contractAddress,
            txHash
        )

class TransferRequest:
    def __init__(self, contractAddress, recipient, network, amount):
        self.contractAddress = contractAddress
        self.recipient = recipient
        self.network = network
        self.amount = amount

    def __repr__(self):
        return (f"TransferRequest("
                f"contractAddress={self.contractAddress!r}, "
                f"recipient={self.recipient!r}, "
                f"network={self.network!r}, "
                f"amount={self.amount!r})")

    def __str__(self):
        return (f"Transfer Request:\n"
                f"  Contract Address: {self.contractAddress}\n"
                f"  Recipient: {self.recipient}\n"
                f"  Network: {self.network}\n"
                f"  Amount: {self.amount}")


class TransferResponse(TransferRequest):
    def __init__(self, contractAddress, recipient, network, amount, txHash, nonce):
        super().__init__(contractAddress, recipient, network, amount)
        self.txHash = txHash
        self.nonce = nonce

    def __repr__(self):
        return (f"TransferResponse("
                f"contractAddress={self.contractAddress!r}, "
                f"recipient={self.recipient!r}, "
                f"network={self.network!r}, "
                f"amount={self.amount!r}, "
                f"txHash={self.txHash!r}, "
                f"nonce={self.nonce!r})")

    def __str__(self):
        return (f"      Transfer Response:\n"
                f"          Contract Address: {self.contractAddress}\n"
                f"          Recipient: {self.recipient}\n"
                f"          Network: {self.network}\n"
                f"          Amount: {self.amount}\n"
                f"          Transaction Hash: {self.txHash}\n"
                f"          Nonce: {self.nonce}")


    @classmethod
    def from_transfer_request(cls, transfer_request: TransferRequest, txHash, nonce) -> 'TransferResponse':
                return cls(
            transfer_request.contractAddress,
            transfer_request.recipient,
            transfer_request.network,
            transfer_request.amount,
            txHash,
            nonce
        )


class TransferFromRequest:
    def __init__(self, contractAddress, sender, recipient, network, amount):
        self.contractAddress = contractAddress
        self.sender = sender
        self.recipient = recipient
        self.network = network
        self.amount = amount

    def __repr__(self):
        return (f"TransferRequest("
                f"contractAddress={self.contractAddress!r}, "
                f"sender={self.sender!r}, "
                f"recipient={self.recipient!r}, "
                f"network={self.network!r}, "
                f"amount={self.amount!r})")

    def __str__(self):
        return (f"Transfer Request:\n"
                f"  Contract Address: {self.contractAddress}\n"
                f"  Sender: {self.sender}\n"
                f"  Recipient: {self.recipient}\n"
                f"  Network: {self.network}\n"
                f"  Amount: {self.amount}")


class TransferFromResponse(TransferFromRequest):
    def __init__(self, contractAddress, sender, recipient, network, amount, txHash, nonce):
        super().__init__(contractAddress, sender, recipient, network, amount)
        self.txHash = txHash
        self.nonce = nonce

    def __repr__(self):
        return (f"TransferFromResponse("
                f"contractAddress={self.contractAddress!r}, "
                f"sender={self.sender!r}, "
                f"recipient={self.recipient!r}, "
                f"network={self.network!r}, "
                f"amount={self.amount!r}, "
                f"txHash={self.txHash!r}, "
                f"nonce={self.nonce!r})")

    def __str__(self):
        return (f"      TransferFrom Response:\n"
                f"          Contract Address: {self.contractAddress}\n"
                f"          Sender: {self.sender}\n"
                f"          Recipient: {self.recipient}\n"
                f"          Network: {self.network}\n"
                f"          Amount: {self.amount}\n"
                f"          Transaction Hash: {self.txHash}\n"
                f"          Nonce: {self.nonce}")


    @classmethod
    def from_transferFrom_request(cls, transferFrom_request: TransferFromRequest, txHash, nonce) -> 'TransferFromResponse':
                return cls(
            transferFrom_request.contractAddress,
            transferFrom_request.sender,
            transferFrom_request.recipient,
            transferFrom_request.network,
            transferFrom_request.amount,
            txHash,
            nonce
        )


class IncreaseAllowanceRequest:
    def __init__(self, contractAddress, spender, network, addedValue):
        self.contractAddress = contractAddress
        self.spender = spender
        self.network = network
        self.addedValue = addedValue

    def __repr__(self):
        return (f"IncreaseAllowanceRequest("
                f"contractAddress={self.contractAddress!r}, "
                f"spender={self.spender!r}, "
                f"network={self.network!r}, "
                f"addedValue={self.addedValue!r})")

    def __str__(self):
        return (f"Increase Allowance Request:\n"
                f"  Contract Address: {self.contractAddress}\n"
                f"  Spender: {self.spender}\n"
                f"  Network: {self.network}\n"
                f"  Added Value: {self.addedValue}")


class IncreaseAllowanceResponse(IncreaseAllowanceRequest):
    def __init__(self, contractAddress, spender, network, addedValue, txHash, nonce):
        super().__init__(contractAddress, spender, network, addedValue)
        self.txHash = txHash
        self.nonce = nonce

    def __repr__(self):
        return (f"IncreaseAllowanceResponse("
                f"contractAddress={self.contractAddress!r}, "
                f"spender={self.spender!r}, "
                f"network={self.network!r}, "
                f"addedValue={self.addedValue!r}, "
                f"txHash={self.txHash!r}, "
                f"nonce={self.nonce!r})")

    def __str__(self):
        return (f"      Increase Allowance Response:\n"
                f"          Contract Address: {self.contractAddress}\n"
                f"          spender: {self.spender}\n"
                f"          Network: {self.network}\n"
                f"          Added Value: {self.addedValue}\n"
                f"          Transaction Hash: {self.txHash}\n"
                f"          Nonce: {self.nonce}")


    @classmethod
    def from_increaseAllowance_request(cls, increaseAllowance_request: IncreaseAllowanceRequest, txHash, nonce) -> 'IncreaseAllowanceResponse':
                return cls(
            increaseAllowance_request.contractAddress,
            increaseAllowance_request.spender,
            increaseAllowance_request.network,
            increaseAllowance_request.addedValue,
            txHash,
            nonce
        )


class DecreaseAllowanceRequest:
    def __init__(self, contractAddress, spender, network, substractedValue):
        self.contractAddress = contractAddress
        self.spender = spender
        self.network = network
        self.substractedValue = substractedValue

    def __repr__(self):
        return (f"DecreaseAllowanceRequest("
                f"contractAddress={self.contractAddress!r}, "
                f"spender={self.spender!r}, "
                f"network={self.network!r}, "
                f"substractedValue={self.substractedValue!r})")

    def __str__(self):
        return (f"Decrease Allowance Request:\n"
                f"  Contract Address: {self.contractAddress}\n"
                f"  Spender: {self.spender}\n"
                f"  Network: {self.network}\n"
                f"  Substracted Value: {self.substractedValue}")


class DecreaseAllowanceResponse(DecreaseAllowanceRequest):
    def __init__(self, contractAddress, spender, network, substractedValue, txHash, nonce):
        super().__init__(contractAddress, spender, network, substractedValue)
        self.txHash = txHash
        self.nonce = nonce

    def __repr__(self):
        return (f"DecreaseAllowanceResponse("
                f"contractAddress={self.contractAddress!r}, "
                f"spender={self.spender!r}, "
                f"network={self.network!r}, "
                f"substractedValue={self.substractedValue!r}, "
                f"txHash={self.txHash!r}, "
                f"nonce={self.nonce!r})")

    def __str__(self):
        return (f"      Decrease Allowance Response:\n"
                f"          Contract Address: {self.contractAddress}\n"
                f"          spender: {self.spender}\n"
                f"          Network: {self.network}\n"
                f"          Substracted Value: {self.substractedValue}\n"
                f"          Transaction Hash: {self.txHash}\n"
                f"          Nonce: {self.nonce}")


    @classmethod
    def from_decreaseAllowance_request(cls, decreaseAllowance_request: DecreaseAllowanceRequest, txHash, nonce) -> 'DecreaseAllowanceResponse':
                return cls(
            decreaseAllowance_request.contractAddress,
            decreaseAllowance_request.spender,
            decreaseAllowance_request.network,
            decreaseAllowance_request.substractedValue,
            txHash,
            nonce
        )

class AllowanceRequest:
    def __init__(self, contractAddress, network, owner, spender):
        self.contractAddress = contractAddress
        self.network = network
        self.owner = owner
        self.spender = spender

    def __repr__(self):
        return (f"AllowanceRequest("
                f"contractAddress={self.contractAddress!r}, "
                f"network={self.network!r}, "
                f"owner={self.owner!r}, "
                f"spender={self.spender!r})")

    def __str__(self):
        return (f"Allowance Request:\n"
                f"  Contract Address: {self.contractAddress}\n"
                f"  Network: {self.network}\n"
                f"  Owner: {self.owner}\n"
                f"  Spender: {self.spender}")


class AllowanceResponse(AllowanceRequest):
    def __init__(self, contractAddress, network, owner, spender, allowance):
        super().__init__(contractAddress, network, owner, spender)
        self.allowance = allowance

    def __repr__(self):
        return (f"AllowanceResponse("
                f"contractAddress={self.contractAddress!r}, "
                f"network={self.network!r}, "
                f"owner={self.owner!r}, "
                f"spender={self.spender!r}, "
                f"allowance={self.allowance!r})")

    def __str__(self):
        return (f"      Allowance Response:\n"
                f"          Allowance: {self.allowance}\n")


    @classmethod
    def from_allowance_request(cls, allowance_request: AllowanceRequest, allowance) -> 'AllowanceResponse':
                return cls(
            allowance_request.contractAddress,
            allowance_request.network,
            allowance_request.owner,
            allowance_request.spender,
            allowance
        )

class NameRequest:
    def __init__(self, contractAddress, network):
        self.contractAddress = contractAddress
        self.network = network

    def __repr__(self):
        return (f"NameRequest("
                f"contractAddress={self.contractAddress!r}, "
                f"network={self.network!r}, )")

    def __str__(self):
        return (f"Name Request:\n"
                f"  Contract Address: {self.contractAddress}\n"
                f"  Network: {self.network}\n")


class NameResponse(NameRequest):
    def __init__(self, contractAddress, network, name):
        super().__init__(contractAddress, network)
        self.name = name

    def __repr__(self):
        return (f"NameResponse("
                f"contractAddress={self.contractAddress!r}, "
                f"network={self.network!r}, "
                f"name={self.name!r})")

    def __str__(self):
        return (f"      Name Response:\n"
                f"          Name: {self.name}\n")


    @classmethod
    def from_name_request(cls, name_request: NameRequest, name) -> 'NameResponse':
                return cls(
            name_request.contractAddress,
            name_request.network,
            name
        )

class SymbolRequest:
    def __init__(self, contractAddress, network):
        self.contractAddress = contractAddress
        self.network = network

    def __repr__(self):
        return (f"SymbolRequest("
                f"contractAddress={self.contractAddress!r}, "
                f"network={self.network!r}, )")

    def __str__(self):
        return (f"Symbol Request:\n"
                f"  Contract Address: {self.contractAddress}\n"
                f"  Network: {self.network}\n")

class SymbolResponse(SymbolRequest):
    def __init__(self, contractAddress, network, symbol):
        super().__init__(contractAddress, network)
        self.symbol = symbol

    def __repr__(self):
        return (f"SymbolResponse("
                f"contractAddress={self.contractAddress!r}, "
                f"network={self.network!r}, "
                f"symbol={self.symbol!r})")

    def __str__(self):
        return (f"      Symbol Response:\n"
                f"          Symbol: {self.symbol}\n")


    @classmethod
    def from_symbol_request(cls, symbol_request: SymbolRequest, symbol) -> 'SymbolResponse':
                return cls(
            symbol_request.contractAddress,
            symbol_request.network,
            symbol
        )

class TotalSupplyRequest:
    def __init__(self, contractAddress, network):
        self.contractAddress = contractAddress
        self.network = network

    def __repr__(self):
        return (f"TotalsupplyRequest("
                f"contractAddress={self.contractAddress!r}, "
                f"network={self.network!r}, )")

    def __str__(self):
        return (f"Total Supply Request:\n"
                f"  Contract Address: {self.contractAddress}\n"
                f"  Network: {self.network}\n")

class TotalSupplyResponse(TotalSupplyRequest):
    def __init__(self, contractAddress, network, totalSupply):
        super().__init__(contractAddress, network)
        self.totalSupply = totalSupply

    def __repr__(self):
        return (f"TotalSupplyResponse("
                f"contractAddress={self.contractAddress!r}, "
                f"network={self.network!r}, "
                f"totalsupply={self.totalSupply!r})")

    def __str__(self):
        return (f"      Total Supply Response:\n"
                f"          Total Supply: {self.totalSupply}\n")


    @classmethod
    def from_totalSupply_request(cls, totalSupply_request: TotalSupplyRequest, totalSupply) -> 'TotalSupplyResponse':
                return cls(
            totalSupply_request.contractAddress,
            totalSupply_request.network,
            totalSupply
        )

class DecimalsRequest:
    def __init__(self, contractAddress, network):
        self.contractAddress = contractAddress
        self.network = network

    def __repr__(self):
        return (f"DecimalsRequest("
                f"contractAddress={self.contractAddress!r}, "
                f"network={self.network!r}, )")

    def __str__(self):
        return (f"Decimals Request:\n"
                f"  Contract Address: {self.contractAddress}\n"
                f"  Network: {self.network}\n")

class DecimalsResponse(DecimalsRequest):
    def __init__(self, contractAddress, network, decimals):
        super().__init__(contractAddress, network)
        self.decimals = decimals

    def __repr__(self):
        return (f"DecimalsResponse("
                f"contractAddress={self.contractAddress!r}, "
                f"network={self.network!r}, "
                f"decimals={self.decimals!r})")

    def __str__(self):
        return (f"      Decimals Response:\n"
                f"          Decimals: {self.decimals}\n")


    @classmethod
    def from_decimals_request(cls, decimals_request: DecimalsRequest, decimals) -> 'DecimalsResponse':
                return cls(
            decimals_request.contractAddress,
            decimals_request.network,
            decimals
        )


class BalanceOfRequest:
    def __init__(self, contractAddress, network, address):
        self.contractAddress = contractAddress
        self.network = network
        self.address = address

    def __repr__(self):
        return (f"BalanceOfRequest("
                f"contractAddress={self.contractAddress!r}, "
                f"network={self.network!r}, "
                f"address={self.address!r}, )")

    def __str__(self):
        return (f"BalanceOf Request:\n"
                f"  Contract Address: {self.contractAddress}\n"
                f"  Network: {self.network}\n"
                f"  Address: {self.address}\n")

class BalanceOfResponse(BalanceOfRequest):
    def __init__(self, contractAddress, network, address, balance):
        super().__init__(contractAddress, network, address)
        self.balance = balance

    def __repr__(self):
        return (f"BalanceOfResponse("
                f"contractAddress={self.contractAddress!r}, "
                f"network={self.network!r}, "
                f"address={self.address!r}, "    
                f"balance={self.balance!r})")

    def __str__(self):
        return (f"      BalanceOf Response:\n"
                f"          Balance: {self.balance}\n")


    @classmethod
    def from_balanceOf_request(cls, balanceOf_request: BalanceOfRequest, balance) -> 'BalanceOfResponse':
                return cls(
            balanceOf_request.contractAddress,
            balanceOf_request.network,
            balanceOf_request.address,
            balance
        )

class DeployEVMRequest:
    def __init__(self, contractSpecsId, sender, blockchainNetwork, params):
        self.contractSpecsId = contractSpecsId
        self.sender = sender
        self.blockchainNetwork = blockchainNetwork
        self.params = params

    def __repr__(self):
        return (f"DeployEVMRequest("
                f"contractSpecsId={self.contractSpecsId!r}, "
                f"sender={self.sender!r}, "
                f"blockchainNetwork={self.blockchainNetwork!r}, "
                f"params={self.params!r})")

    def __str__(self):
        return (f"Deploy EVM Request:\n"
                f"  Contract Specs ID: {self.contractSpecsId}\n"
                f"  Sender: {self.sender}\n"
                f"  Blockchain Network: {self.blockchainNetwork}\n"
                f"  Params: {self.params}")


class DeployEVMResponse(DeployEVMRequest):
    def __init__(self, contractSpecsId, sender, blockchainNetwork, params, contractAddress, txHash):
        super().__init__(contractSpecsId, sender, blockchainNetwork, params)
        self.contractAddress = contractAddress
        self.txHash = txHash

    def __repr__(self):
        return (f"DeployEVMResponse("
                f"contractSpecsId={self.contractSpecsId!r}, "
                f"sender={self.sender!r}, "
                f"blockchainNetwork={self.blockchainNetwork!r}, "
                f"params={self.params!r}, "
                f"contractAddress={self.contractAddress!r}, "
                f"txHash={self.txHash!r})")

    def __str__(self):
        return (f"      Deploy EVM Response:\n"
                f"          Contract Specs ID: {self.contractSpecsId}\n"
                f"          Sender: {self.sender}\n"
                f"          Network: {self.blockchainNetwork}\n"
                f"          Name: {self.params[0]}\n"
                f"          Symbol: {self.params[1]}\n"
                f"          Initial Supply: {self.params[2]}\n"
                f"          Owner: {self.params[3]}\n"
                f"          Contract Address: {self.contractAddress}\n"
                f"          Transaction Hash: {self.txHash}")

   
    @classmethod
    def from_deploy_evm_request(cls, deploy_evm_request: DeployEVMRequest, contractAddress, txHash) -> 'DeployEVMResponse':
                return cls(
            deploy_evm_request.contractSpecsId,
            deploy_evm_request.sender,
            deploy_evm_request.blockchainNetwork,
            deploy_evm_request.params,
            contractAddress,
            txHash
        )


class TransactRequest:
    def __init__(self, contractAddress, sender, blockchainNetwork, method, params):
        self.contractAddress = contractAddress
        self.sender = sender
        self.blockchainNetwork = blockchainNetwork
        self.method = method
        self.params = params

    def __repr__(self):
        return (f"TransactRequest("
                f"contractAddress={self.contractAddress!r}, " 
                f"sender={self.sender!r}, "
                f"blockchainNetwork={self.blockchainNetwork!r}, "
                f"method={self.method!r}, "
                f"params={self.params!r})")

    def __str__(self):
        return (f"Transaction Request:\n"
                f"  Contract Address: {self.contractAddress}\n"
                f"  Sender: {self.sender}\n"
                f"  Blockchain Network: {self.blockchainNetwork}\n"
                f"  Method: {self.method}\n"
                f"  Params: {self.params}")


class TransactResponse(TransactRequest):
    def __init__(self, contractAddress, sender, blockchainNetwork, method, params, txHash, nonce):
        super().__init__(contractAddress, sender, blockchainNetwork, method, params)
        self.txHash = txHash
        self.nonce = nonce

    def __repr__(self):
        return (f"TransactResponse("
                f"contractAddress={self.contractAddress!r}, "
                f"sender={self.sender!r}, "
                f"blockchainNetwork={self.blockchainNetwork!r}, "
                f"method={self.method!r}, "
                f"params={self.params!r}, "
                f"txHash={self.txHash!r}, "
                f"nonce={self.nonce!r})")

    def __str__(self):
        return (f"      Transfer Response:\n"
                f"          Contract Address: {self.contractAddress}\n"
                f"          Sender: {self.sender}\n"
                f"          Recipient: {self.params[0]}\n"
                f"          Network: {self.blockchainNetwork}\n"
                f"          Amount: {self.params[1]}\n"
                f"          Transaction Hash: {self.txHash}\n"
                f"          Nonce: {self.nonce}")

   
    @classmethod
    def from_transact_request(cls, transact_request: TransactRequest, txHash, nonce) -> 'TransactResponse':
                return cls(
            transact_request.contractAddress,
            transact_request.sender,
            transact_request.blockchainNetwork,
            transact_request.method,
            transact_request.params,
            txHash,
            nonce
        )


class ViewRequest:
    def __init__(self, contractAddress, blockchainNetwork, method, params):
        self.contractAddress = contractAddress
        self.blockchainNetwork = blockchainNetwork
        self.method = method
        self.params = params

    def __repr__(self):
        return (f"TransactRequest("
                f"contractAddress={self.contractAddress!r}, "
                f"blockchainNetwork={self.blockchainNetwork!r}, "
                f"method={self.method!r}, "
                f"params={self.params!r})")

    def __str__(self):
        return (f"Transaction Request:\n"
                f"  Contract Address: {self.contractAddress}\n"
                f"  Blockchain Network: {self.blockchainNetwork}\n"
                f"  Method: {self.method}\n"
                f"  Params: {self.params}")

class ViewResponse(ViewRequest):
    def __init__(self, contractAddress, blockchainNetwork, method, params, response):
        super().__init__(contractAddress, blockchainNetwork, method, params)
        self.response = response

    def __repr__(self):
        return (f"ViewResponse("
                f"contractAddress={self.contractAddress!r}, "
                f"blockchainNetwork={self.blockchainNetwork!r}, "
                f"method={self.method!r}, "
                f"params={self.params!r}, "
                f"response={self.response!r}, ")

    def __str__(self):
        return (f"  View Response: {self.response}\n")

   
    @classmethod
    def from_view_request(cls, view_request: ViewRequest, response) -> 'ViewResponse':
                return cls(
            view_request.contractAddress,
            view_request.blockchainNetwork,
            view_request.method,
            view_request.params,
            response
        )
class AvailableNetworksEVMResponse:
    def __init__(self, response):
        self.response = response

    def __repr__(self):
        return (f"AvailableNetworksEVMResponse("
                f"response={self.response!r})")

    def __str__(self):
        return (f"{self.response}")

class AvailableContractSpecsEVMResponse:
    def __init__(self, response):
        self.response = response

    def __repr__(self):
        return (f"AvailableContractSpecsEVMResponse("
                f"response={self.response!r})")

    def __str__(self):
        return (f"{self.response}")

class IsContractEVMResponse:
    def __init__(self, response):
        self.response = response

    def __repr__(self):
        return (f"IsContractEVMResponse("
                f"response={self.response!r})")

    def __str__(self):
        return (f"Is Contract? -> {self.response['isContract']}")

class GetTxInfoEVMResponse:
    def __init__(self, response):
        self.response = response

    def __repr__(self):
        return (f"GetTxInfoEVMResponse("
                f"response={self.response!r})")

    def __str__(self):
        return (f"Tx Info: {self.response}")

class GetTxStatusEVMResponse:
    def __init__(self, response):
        self.response = response

    def __repr__(self):
        return (f"GetTxStatusEVMResponse("
                f"response={self.response!r})")

    def __str__(self):
        return (f"Tx Status: {self.response}")

class GetTxStatusReferenceEVMResponse:
    def __init__(self, response):
        self.response = response

    def __repr__(self):
        return (f"GetTxStatusReferenceEVMResponse("
                f"response={self.response!r})")

    def __str__(self):
        return (f"Tx Status: {self.response}")

class GetGasPriceEVMResponse:
    def __init__(self, response):
        self.response = response

    def __repr__(self):
        return (f"GetGasPriceEVMResponse("
                f"response={self.response!r})")

    def __str__(self):
        return (f"Gas Price: {self.response}")

class GetBalanceNativeEVMResponse:
    def __init__(self, response):
        self.response = response

    def __repr__(self):
        return (f"GetBalanceNativeEVMResponse("
                f"response={self.response!r})")

    def __str__(self):
        return (f"Balance: {self.response}")

class DeployGasFeeEVMRequest:
    def __init__(self, contractSpecsId, sender, blockchainNetwork, params):
        self.contractSpecsId = contractSpecsId
        self.sender = sender
        self.blockchainNetwork = blockchainNetwork
        self.params = params

    def __repr__(self):
        return (f"DeployGasFeeEVMRequest("
                f"contractSpecsId={self.contractSpecsId!r}, "
                f"sender={self.sender!r}, "
                f"blockchainNetwork={self.blockchainNetwork!r}, "
                f"params={self.params!r})")

    def __str__(self):
        return (f"Deploy Gas Fee EVM Request:\n"
                f"  Contract Specs ID: {self.contractSpecsId}\n"
                f"  Sender: {self.sender}\n"
                f"  Blockchain Network: {self.blockchainNetwork}\n"
                f"  Params: {self.params}")


class DeployGasFeeEVMResponse(DeployGasFeeEVMRequest):
    def __init__(self, contractSpecsId, sender, blockchainNetwork, params, estimatedGas):
        super().__init__(contractSpecsId, sender, blockchainNetwork, params)
        self.estimatedGas = estimatedGas

    def __repr__(self):
        return (f"DeployGasFeeEVMResponse("
                f"contractSpecsId={self.contractSpecsId!r}, "
                f"sender={self.sender!r}, "
                f"blockchainNetwork={self.blockchainNetwork!r}, "
                f"params={self.params!r}, "
                f"estimatedGas={self.estimatedGas!r})")

    def __str__(self):
        return (f"      Deploy Gas Fee EVM Response:\n"
                f"          Estimated Gas: {self.estimatedGas}")

   
    @classmethod
    def from_deploy_gas_fee_evm_request(cls, deploy_gas_fee_evm_request: DeployGasFeeEVMRequest, estimatedGas) -> 'DeployGasFeeEVMResponse':
                return cls(
            deploy_gas_fee_evm_request.contractSpecsId,
            deploy_gas_fee_evm_request.sender,
            deploy_gas_fee_evm_request.blockchainNetwork,
            deploy_gas_fee_evm_request.params,
            estimatedGas
        )


class TransactGasFeeEVMResponse(TransactRequest):
    def __init__(self, contractAddress, sender, blockchainNetwork, method, params, estimatedGas):
        super().__init__(contractAddress, sender, blockchainNetwork, method, params)
        self.estimatedGas = estimatedGas

    def __repr__(self):
        return (f"TransactResponse("
                f"contractAddress={self.contractAddress!r}, "
                f"sender={self.sender!r}, "
                f"blockchainNetwork={self.blockchainNetwork!r}, "
                f"method={self.method!r}, "
                f"params={self.params!r}, "
                f"estimatedGas={self.estimatedGas!r})")

    def __str__(self):
        return (f"      Transact Gas Fee EVM Response:\n"
                f"          Estimated Gas Fee: {self.estimatedGas}\n")

   
    @classmethod
    def from_transact_request(cls, transact_request: TransactRequest, estimatedGas) -> 'TransactGasFeeEVMResponse':
                return cls(
            transact_request.contractAddress,
            transact_request.sender,
            transact_request.blockchainNetwork,
            transact_request.method,
            transact_request.params,
            estimatedGas
        )

class NativeGasFeeEVMRequest:
    def __init__(self, sender, recipient, blockchainNetwork, value):
        self.sender = sender
        self.recipient = recipient
        self.blockchainNetwork = blockchainNetwork
        self.value = value

    def __repr__(self):
        return (f"NativeGasFeeEVMRequest("
                f"sender={self.sender!r}, "
                f"recipient={self.recipient!r}, "
                f"blockchainNetwork={self.blockchainNetwork!r}, "
                f"value={self.value!r})")

    def __str__(self):
        return (f"Native Gas Fee EVM Request:\n"
                f"  Sender: {self.sender}\n"
                f"  Recipient: {self.recipient}\n"
                f"  Blockchain Network: {self.blockchainNetwork}\n"
                f"  Value: {self.value}")


class NativeGasFeeEVMResponse(NativeGasFeeEVMRequest):
    def __init__(self, sender, recipient, blockchainNetwork, value, estimatedGas):
        super().__init__(sender, recipient, blockchainNetwork, value)
        self.estimatedGas = estimatedGas

    def __repr__(self):
        return (f"NativeGasFeeEVMResponse("
                f"sender={self.sender!r}, "
                f"recipient={self.recipient!r}, "
                f"blockchainNetwork={self.blockchainNetwork!r}, "
                f"value={self.value!r}, "
                f"estimatedGas={self.estimatedGas!r})")

    def __str__(self):
        return (f"      Native Gas Fee EVM Response:\n"
                f"          Estimated Gas: {self.estimatedGas}")

   
    @classmethod
    def from_native_gas_fee_evm_request(cls, native_gas_fee_evm_request: NativeGasFeeEVMRequest, estimatedGas) -> 'NativeGasFeeEVMResponse':
                return cls(
            native_gas_fee_evm_request.sender,
            native_gas_fee_evm_request.recipient,
            native_gas_fee_evm_request.blockchainNetwork,
            native_gas_fee_evm_request.value,
            estimatedGas
        )


