from .base_client import BaseClient
from .models import DeployRequest, DeployResponse, TransferRequest, TransferResponse, TransferFromRequest, TransferFromResponse, IncreaseAllowanceRequest, IncreaseAllowanceResponse, DecreaseAllowanceRequest, DecreaseAllowanceResponse, AllowanceRequest, AllowanceResponse, NameRequest, NameResponse, SymbolRequest, SymbolResponse, TotalSupplyRequest, TotalSupplyResponse, DecimalsRequest, DecimalsResponse, BalanceOfRequest, BalanceOfResponse, DeployEVMRequest, DeployEVMResponse, TransactRequest, TransactResponse, ViewRequest, ViewResponse, DeployGasFeeEVMRequest, DeployGasFeeEVMResponse, TransactGasFeeEVMResponse, NativeGasFeeEVMRequest, NativeGasFeeEVMResponse, AvailableNetworksEVMResponse, AvailableContractSpecsEVMResponse, IsContractEVMResponse, GetTxInfoEVMResponse, GetTxStatusEVMResponse, GetTxStatusReferenceEVMResponse, GetGasPriceEVMResponse, GetBalanceNativeEVMResponse

class VottunClient(BaseClient):
     
    def deploy_erc20(self, deploy_request: DeployRequest) -> DeployResponse:
        response = self._make_request('erc/v1/erc20/deploy', 'POST', data=deploy_request.__dict__) 
        return DeployResponse.from_deploy_request(deploy_request, response['contractAddress'], response['txHash'])

    def transfer_erc20(self, transfer_request: TransferRequest) -> TransferResponse:
        response = self._make_request('erc/v1/erc20/transfer', 'POST', data=transfer_request.__dict__) 
        return TransferResponse.from_transfer_request(transfer_request, response['txHash'], response['nonce'])
    
    def transferFrom_erc20(self, transferFrom_request: TransferFromRequest) -> TransferFromResponse:
        response = self._make_request('erc/v1/erc20/transferFrom', 'POST', data=transferFrom_request.__dict__)
        return TransferFromResponse.from_transferFrom_request(transferFrom_request, response['txHash'], response['nonce'])

    def increaseAllowance_erc20(self, increaseAllowance_request: IncreaseAllowanceRequest) -> IncreaseAllowanceResponse:
        response = self._make_request('erc/v1/erc20/increaseAllowance', 'POST', data=increaseAllowance_request.__dict__)
        return IncreaseAllowanceResponse.from_increaseAllowance_request(increaseAllowance_request, response['txHash'], response['nonce'])

    def decreaseAllowance_erc20(self, decreaseAllowance_request: DecreaseAllowanceRequest) -> DecreaseAllowanceResponse:
        response = self._make_request('erc/v1/erc20/decreaseAllowance', 'POST', data=decreaseAllowance_request.__dict__)
        return DecreaseAllowanceResponse.from_decreaseAllowance_request(decreaseAllowance_request, response['txHash'], response['nonce'])

    def allowance_erc20(self, allowance_request: AllowanceRequest) -> AllowanceResponse:
        response = self._make_request('erc/v1/erc20/allowance', 'GET', data=allowance_request.__dict__)
        return AllowanceResponse.from_allowance_request(allowance_request, response['allowance'])

    def name_erc20(self, name_request: NameRequest) -> NameResponse:
        response = self._make_request('erc/v1/erc20/name', 'GET', data=name_request.__dict__)
        return NameResponse.from_name_request(name_request, response['name'])

    def symbol_erc20(self, symbol_request: SymbolRequest) -> SymbolResponse:
        response = self._make_request('erc/v1/erc20/symbol', 'GET', data=symbol_request.__dict__)
        return SymbolResponse.from_symbol_request(symbol_request, response['symbol'])

    def totalSupply_erc20(self, totalSupply_request: TotalSupplyRequest) -> TotalSupplyResponse:
        response = self._make_request('erc/v1/erc20/totalSupply', 'GET', data=totalSupply_request.__dict__)
        return TotalSupplyResponse.from_totalSupply_request(totalSupply_request, response['totalSupply'])

    def decimals_erc20(self, decimals_request: DecimalsRequest) -> DecimalsResponse:
        response = self._make_request('erc/v1/erc20/decimals', 'GET', data=decimals_request.__dict__)
        return DecimalsResponse.from_decimals_request(decimals_request, response['decimals'])


    def balanceOf_erc20(self, balanceOf_request: BalanceOfRequest) -> BalanceOfResponse:
        response = self._make_request('erc/v1/erc20/balanceOf', 'GET', data=balanceOf_request.__dict__)
        return BalanceOfResponse.from_balanceOf_request(balanceOf_request, response['balance'])

    def deploy_evm(self, deploy_evm_request: DeployEVMRequest) -> DeployEVMResponse:
        response = self._make_request('core/v1/evm/contract/deploy', 'POST', data=deploy_evm_request.__dict__)
        return DeployEVMResponse.from_deploy_evm_request(deploy_evm_request, response['contractAddress'], response['txHash'])

    def transact_evm(self, transact_request: TransactRequest) -> TransactResponse:
        response = self._make_request('core/v1/evm/transact/mutable', 'POST', data=transact_request.__dict__)
        return TransactResponse.from_transact_request(transact_request, response['txHash'], response['nonce'])

    def view_evm(self, view_request: ViewRequest) -> ViewResponse:
        response = self._make_request('core/v1/evm/transact/view', 'GET', data=view_request.__dict__)
        return ViewResponse.from_view_request(view_request, *response)

    def available_networks_evm(self) -> AvailableNetworksEVMResponse:
        response = self._make_request('core/v1/evm/info/chains', 'GET')
        return AvailableNetworksEVMResponse(response)


    def available_contract_specs_evm(self) -> AvailableContractSpecsEVMResponse:
        response = self._make_request('core/v1/evm/info/specs', 'GET')
        return AvailableContractSpecsEVMResponse(response)

    def is_contract_evm(self) -> IsContractEVMResponse:
        address = input("Enter address: ")
        networkId = int(input("Enter network id: "))
        response = self._make_request(f"core/v1/evm/info/address/{address}/iscontract?network={networkId}", 'GET')
        return IsContractEVMResponse(response)
 
    def get_tx_info_evm(self) -> GetTxInfoEVMResponse:
        txHash = input("Enter txHash: ")
        networkId = int(input("Enter network id: "))
        response = self._make_request(f"core/v1/evm/info/transaction/{txHash}?network={networkId}", 'GET')
        return GetTxInfoEVMResponse(response)

    def get_tx_status_evm(self) -> GetTxStatusEVMResponse:
        txHash = input("Enter txHash: ")
        networkId = int(input("Enter network id: "))
        response = self._make_request(f"core/v1/evm/info/transaction/{txHash}/status?network={networkId}", 'GET')
        return GetTxStatusEVMResponse(response)

    def get_tx_status_reference_evm(self) -> GetTxStatusReferenceEVMResponse:
        reference = input("Enter tx reference: ")
        response = self._make_request(f"core/v1/evm/info/transaction/reference/{reference}", 'GET')
        return GetTxStatusReferenceEVMResponse(response)

    def get_gas_price_evm(self) -> GetGasPriceEVMResponse:
        networkId = input("Enter network id: ")
        response = self._make_request(f"core/v1/evm/network/gasprice?network={networkId}", 'GET')
        return GetGasPriceEVMResponse(response)

    def get_balance_native_evm(self) -> GetBalanceNativeEVMResponse:
        account = input("Enter account: ") 
        networkId = int(input("Enter network id: "))
        response = self._make_request(f"core/v1/evm/chain/{account}/balance?network={networkId}", 'GET')
        return GetBalanceNativeEVMResponse(response)

    def deploy_gas_fee_evm(self, deploy_gas_fee_evm_request: DeployGasFeeEVMRequest) -> DeployGasFeeEVMResponse:
        response = self._make_request('core/v1/evm/contract/deploy/estimategas', 'GET', data=deploy_gas_fee_evm_request.__dict__)
        return DeployGasFeeEVMResponse.from_deploy_gas_fee_evm_request(deploy_gas_fee_evm_request, response['estimatedGas'])

    def transact_gas_fee_evm(self, transact_request: TransactRequest) -> TransactGasFeeEVMResponse:
        response = self._make_request('core/v1/evm/transact/mutable/estimategas', 'GET', data=transact_request.__dict__)
        return TransactGasFeeEVMResponse.from_transact_request(transact_request, response['estimatedGas'])

    def native_gas_fee_evm(self, native_gas_fee_evm_request: NativeGasFeeEVMRequest) -> NativeGasFeeEVMResponse:
        response = self._make_request('core/v1/evm/chain/transfer/estimategas', 'GET', data=native_gas_fee_evm_request.__dict__)
        return NativeGasFeeEVMResponse.from_native_gas_fee_evm_request(native_gas_fee_evm_request, response['estimatedGas'])

    
    @staticmethod
    def prompt_for_deploy_request() -> DeployRequest:
        name = input("Enter contract name: ").strip()
        symbol = input("Enter contract symbol: ").strip()
        alias = input("Enter contract alias: ").strip()
        initial_supply = int(input("Enter initial supply: ").strip())
        network = int(input("Enter network ID: ").strip())
        
        # Mandatory fields
        deploy_request_data = {
            'name': name,
            'symbol': symbol,
            'alias': alias,
            'initialSupply': initial_supply,
            'network': network
        }
        
        # Optional fields
        optional_fields = {}
        gas_limit = input("Enter gas limit (optional): ").strip()
        if gas_limit:
            optional_fields['gasLimit'] = int(gas_limit)
        
        deploy_request = DeployRequest(**deploy_request_data)
        for key, value in optional_fields.items():
            setattr(deploy_request, key, value)
        
        return deploy_request

    @staticmethod
    def prompt_for_transfer_request() -> TransferRequest:
        contract_address = input("Enter contract address: ").strip()
        recipient = input("Enter recipient address: ").strip()
        network = int(input("Enter network ID: ").strip())
        amount = int(input("Enter amount: ").strip())
        
        # Mandatory fields
        transfer_request_data = {
            'contractAddress': contract_address,
            'recipient': recipient,
            'network': network,
            'amount': amount
        }
        
        # Optional fields
        optional_fields = {}
        gas_limit = input("Enter gas limit (optional): ").strip()
        if gas_limit:
            optional_fields['gasLimit'] = int(gas_limit)
        
        transfer_request = TransferRequest(**transfer_request_data)
        for key, value in optional_fields.items():
            setattr(transfer_request, key, value)
        
        return transfer_request

        
    @staticmethod
    def prompt_for_transferFrom_request() -> TransferFromRequest:
        contract_address = input("Enter contract address: ").strip()
        sender = input("Enter sender address: ").strip()
        recipient = input("Enter recipient address: ").strip()
        network = int(input("Enter network ID: ").strip())
        amount = int(input("Enter amount: ").strip())
       
        # Mandatory fields
        transferFrom_request_data = {
            'contractAddress': contract_address,
            'sender': sender,
            'recipient': recipient,
            'network': network,
            'amount': amount
        }
        
        # Optional fields
        optional_fields = {}
        gas_limit = input("Enter gas limit (optional): ").strip()
        if gas_limit:
            optional_fields['gasLimit'] = int(gas_limit)
        
        transferFrom_request = TransferFromRequest(**transferFrom_request_data)
        for key, value in optional_fields.items():
            setattr(transferFrom_request, key, value)
        
        return transferFrom_request


    @staticmethod
    def prompt_for_increaseAllowance_request() -> IncreaseAllowanceRequest:
        contract_address = input("Enter contract address: ").strip()
        spender = input("Enter spender address: ").strip()
        network = int(input("Enter network ID: ").strip())
        added_value = int(input("Enter added value: ").strip())
        
    # Mandatory fields
        increase_allowance_request_data = {
            'contractAddress': contract_address,
            'spender': spender,
            'network': network,
            'addedValue': added_value
        }
        
        # Optional fields
        optional_fields = {}
        gas_limit = input("Enter gas limit (optional): ").strip()
        if gas_limit:
            optional_fields['gasLimit'] = int(gas_limit)
        
        increase_allowance_request = IncreaseAllowanceRequest(**increase_allowance_request_data)
        for key, value in optional_fields.items():
            setattr(increase_allowance_request, key, value)
        
        return increase_allowance_request

    @staticmethod
    def prompt_for_decreaseAllowance_request() -> DecreaseAllowanceRequest:
        contract_address = input("Enter contract address: ").strip()
        spender = input("Enter spender address: ").strip()
        network = int(input("Enter network ID: ").strip())
        substracted_value = int(input("Enter substracted value: ").strip())
        
    # Mandatory fields
        decrease_allowance_request_data = {
            'contractAddress': contract_address,
            'spender': spender,
            'network': network,
            'substractedValue': substracted_value
        }
        
        # Optional fields
        optional_fields = {}
        gas_limit = input("Enter gas limit (optional): ").strip()
        if gas_limit:
            optional_fields['gasLimit'] = int(gas_limit)
        
        decrease_allowance_request = DecreaseAllowanceRequest(**decrease_allowance_request_data)
        for key, value in optional_fields.items():
            setattr(decrease_allowance_request, key, value)
        
        return decrease_allowance_request



    @staticmethod
    def prompt_for_allowance_request() -> AllowanceRequest:
        contract_address = input("Enter contract address: ").strip()
        network = int(input("Enter network ID: ").strip())
        owner = input("Enter owner address: ").strip()
        spender = input("Enter spender address: ").strip()
        return AllowanceRequest(contractAddress=contract_address, network=network, owner=owner, spender=spender)

    @staticmethod
    def prompt_for_name_request() -> NameRequest:
        contract_address = input("Enter contract address: ").strip()
        network = int(input("Enter network ID: ").strip())
        return NameRequest(contractAddress=contract_address, network=network)

    @staticmethod
    def prompt_for_symbol_request() -> SymbolRequest:
        contract_address = input("Enter contract address: ").strip()
        network = int(input("Enter network ID: ").strip())
        return SymbolRequest(contractAddress=contract_address, network=network)

    @staticmethod
    def prompt_for_totalSupply_request() -> TotalSupplyRequest:
        contract_address = input("Enter contract address: ").strip()
        network = int(input("Enter network ID: ").strip())
        return TotalSupplyRequest(contractAddress=contract_address, network=network)

    @staticmethod
    def prompt_for_decimals_request() -> DecimalsRequest:
        contract_address = input("Enter contract address: ").strip()
        network = int(input("Enter network ID: ").strip())
        return DecimalsRequest(contractAddress=contract_address, network=network)

    @staticmethod
    def prompt_for_balanceOf_request() -> BalanceOfRequest:
        contract_address = input("Enter contract address: ").strip()
        network = int(input("Enter network ID: ").strip())
        address = input("Enter address: ").strip()
        return BalanceOfRequest(contractAddress=contract_address, network=network, address=address)

    @staticmethod
    def prompt_for_deploy_evm_request() -> DeployEVMRequest:
        contract_specs_id = int(input("Enter contract specs id: ").strip())
        sender = input("Enter sender address: ").strip()
        blockchain_network = int(input("Enter blockchain network ID: ").strip())
        params_name = input("Enter contract name: ").strip()
        params_symbol = input("Enter symbol: ").strip()
        params_initial_supply = int(input("Enter initial supply: ").strip())
        params_owner = input("Enter owner address: ").strip()
        params = [params_name, params_symbol, params_initial_supply, params_owner]
        
        # Mandatory fields
        deploy_evm_request_data = {
            'contractSpecsId': contract_specs_id,
            'sender': sender,
            'blockchainNetwork': blockchain_network,
            'params': params
        }
        
        # Optional fields
        optional_fields = {}
        my_reference = input("Enter your reference (optional): ").strip()
        gas_limit = input("Enter gas limit (optional): ").strip()
        use_gas_Estimation = input("Enter 'true' or 'false' for gas estimation (optional): ").strip()
        gas_price = input("Enter gas price (optional): ").strip()
        priority_fee = input("Enter priority fee (optional): ").strip()
        nonce = input("Enter nonce (optional): ").strip()
        alias = input("Enter alias (optional): ").strip()

        
        if my_reference:
            optional_fields['myReference'] = my_reference
        if gas_limit:
            optional_fields['gasLimit'] = int(gas_limit)
        if use_gas_Estimation:
            optional_fields['useGasEstimation'] = bool(use_gas_Estimation)
        if gas_price:
            optional_fields['gasPrice'] = int(gas_price)
        if priority_fee:
            optional_fields['priorityFee'] = float(priority_fee)
        if nonce:
            optional_fields['nonce'] = int(nonce)
        if alias:
            optional_fields['alias'] = alias


        deploy_evm_request = DeployEVMRequest(**deploy_evm_request_data)
        for key, value in optional_fields.items():
            setattr(deploy_evm_request, key, value)
        
        return deploy_evm_request

    @staticmethod
    def prompt_for_transact_request() -> TransactRequest:
        contract_address = input("Enter contract address: ").strip()
        sender = input("Enter sender address: ").strip()
        blockchain_network = int(input("Enter blockchain network ID: ").strip())
        method = input("Enter method: ").strip()

        print("Enter parameters one by one. Type 'done' when you have finished entering parameters.")
        params = []

        while True:
            param = input(f"Enter parameter {len(params)}: ").strip()
            if param.lower() == 'done':
                break
            param = int(param) if param.isdigit() else param
            params.append(param)
        
        # Mandatory fields
        transact_request_data = {
            'contractAddress': contract_address,
            'sender': sender,
            'blockchainNetwork': blockchain_network,
            'method': method,
            'params': params
        }
        
        # Optional fields
        optional_fields = {}
        my_reference = input("Enter your reference (optional): ").strip()
        contract_specs_id = input("Enter contract specs id (optional): ").strip()
        value = input("Enter amount of native tokens (optional): ").strip()
        gas_limit = input("Enter gas limit (optional): ").strip()
        use_gas_Estimation = input("Enter 'true' or 'false' for gas estimation (optional): ").strip()
        gas_price = input("Enter gas price (optional): ").strip()
        priority_fee = input("Enter priority fee (optional): ").strip()
        nonce = input("Enter nonce (optional): ").strip()

        
        if my_reference:
            optional_fields['myReference'] = my_reference
        if contract_specs_id:
            optional_fields['contractSpecsId'] = int(contract_specs_id)
        if value:
            optional_fields['value'] = int(value)
        if gas_limit:
            optional_fields['gasLimit'] = int(gas_limit)
        if use_gas_Estimation:
            optional_fields['useGasEstimation'] = bool(use_gas_Estimation)
        if gas_price:
            optional_fields['gasPrice'] = int(gas_price)
        if priority_fee:
            optional_fields['priorityFee'] = float(priority_fee)
        if nonce:
            optional_fields['nonce'] = int(nonce)

        transact_request = TransactRequest(**transact_request_data)
        for key, value in optional_fields.items():
            setattr(transact_request, key, value)
        
        return transact_request


    @staticmethod
    def prompt_for_view_request() -> ViewRequest:
        contract_address = input("Enter contract address: ").strip()
        blockchain_network = int(input("Enter blockchain network ID: ").strip())
        method = input("Enter method: ").strip()
        params = []
        return ViewRequest(contractAddress=contract_address, blockchainNetwork=blockchain_network, method=method, params=params)

    @staticmethod
    def prompt_for_deploy_gas_fee_evm_request() -> DeployGasFeeEVMRequest:
        contract_specs_id = int(input("Enter contract specs id: ").strip())
        sender = input("Enter sender address: ").strip()
        blockchain_network = int(input("Enter blockchain network ID: ").strip())
        params_name = input("Enter contract name: ").strip()
        params_symbol = input("Enter symbol: ").strip()
        params_initial_supply = int(input("Enter initial supply: ").strip())
        params_owner = input("Enter owner address: ").strip()
        params = [params_name, params_symbol, params_initial_supply, params_owner]
        return DeployGasFeeEVMRequest(contractSpecsId=contract_specs_id, sender=sender, blockchainNetwork=blockchain_network, params=params)

    @staticmethod
    def prompt_for_native_gas_fee_evm_request() -> NativeGasFeeEVMRequest:
        sender = input("Enter sender address: ").strip()
        recipient = input("Enter recipient address: ").strip()
        blockchain_network = int(input("Enter blockchain network ID: ").strip())
        value = int(input("Enter value: ").strip())
        return NativeGasFeeEVMRequest(sender=sender, recipient=recipient, blockchainNetwork=blockchain_network, value=value)
    
