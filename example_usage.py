from vottun_sdk.client import VottunClient

client = VottunClient(api_key='<your_api_key>', app_id='<your_app_id>')

#Uncomment the píece of code you want to try.

"""
deploy_request = client.prompt_for_deploy_request()
deploy_response = client.deploy_erc20(deploy_request)
print(deploy_response)
"""

"""
transfer_request = client.prompt_for_transfer_request()
transfer_response = client.transfer_erc20(transfer_request)
print(transfer_response)
"""

"""
transferFrom_request = client.prompt_for_transferFrom_request()
transferFrom_response = client.transferFrom_erc20(transferFrom_request)
print(transferFrom_response)
"""

"""
increaseAllowance_request = client.prompt_for_increaseAllowance_request()
increaseAllowance_response = client.increaseAllowance_erc20(increaseAllowance_request)
print(increaseAllowance_response)
"""

"""
decreaseAllowance_request = client.prompt_for_decreaseAllowance_request()
decreaseAllowance_response = client.decreaseAllowance_erc20(decreaseAllowance_request)
print(decreaseAllowance_response)
"""

"""
allowance_request = client.prompt_for_allowance_request()
allowance_response = client.allowance_erc20(allowance_request)
print(allowance_response)
"""

"""
name_request = client.prompt_for_name_request()
name_response = client.name_erc20(name_request)
print(name_response)
"""

"""
symbol_request = client.prompt_for_symbol_request()
symbol_response = client.symbol_erc20(symbol_request)
print(symbol_response)
"""

"""
totalSupply_request = client.prompt_for_totalSupply_request()
totalSupply_response = client.totalSupply_erc20(totalSupply_request)
print(totalSupply_response)
"""

"""
decimals_request = client.prompt_for_decimals_request()
decimals_response = client.decimals_erc20(decimals_request)
print(decimals_response)
"""

"""
balanceOf_request = client.prompt_for_balanceOf_request()
balanceOf_response = client.balanceOf_erc20(balanceOf_request)
print(balanceOf_response)
"""

"""
deploy_evm_request = client.prompt_for_deploy_evm_request()
deploy_evm_response = client.deploy_evm(deploy_evm_request)
print(deploy_evm_response)
"""

"""
transact_request = client.prompt_for_transact_request()
transact_response = client.transact_evm(transact_request)
print(transact_response)
"""

"""
view_request = client.prompt_for_view_request()
view_response = client.view_evm(view_request)
print(view_response)
"""

"""
available_networks_evm_response = client.available_networks_evm()
print(available_networks_evm_response)
"""

"""
available_contract_specs_evm_response = client.available_contract_specs_evm()
print(available_contract_specs_evm_response)
"""

"""
is_contract_evm_response = client.is_contract_evm()
print(is_contract_evm_response)
"""

"""
get_tx_info_evm_response = client.get_tx_info_evm()
print(get_tx_info_evm_response)
"""

"""
get_tx_status_evm_response = client.get_tx_status_evm()
print(get_tx_status_evm_response)
"""

"""
get_tx_status_reference_evm_response = client.get_tx_status_reference_evm()
print(get_tx_status_reference_evm_response)
"""

"""
get_gas_price_evm_response = client.get_gas_price_evm()
print(get_gas_price_evm_response)
"""

"""
get_balalnce_native_evm_response = client.get_balance_native_evm()
print(get_balalnce_native_evm_response)
"""

"""
deploy_gas_fee_evm_request = client.prompt_for_deploy_gas_fee_evm_request()
deploy_gas_fee_evm_response = client.deploy_gas_fee_evm(deploy_gas_fee_evm_request)
print(deploy_gas_fee_evm_response)
"""

"""
transact_request = client.prompt_for_transact_request()
transact_gas_fee_evm_response = client.transact_gas_fee_evm(transact_request)
print(transact_gas_fee_evm_response)
"""

"""
native_gas_fee_evm_request = client.prompt_for_native_gas_fee_evm_request()
native_gas_fee_evm_response = client.native_gas_fee_evm(native_gas_fee_evm_request)
print(native_gas_fee_evm_response)
"""
