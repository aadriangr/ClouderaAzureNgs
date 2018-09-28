$RGName = 'cloudera-administrator'
$Location = 'West Europe'
$nsgName = 'centos7-tiger-nsg'
$NSG = Get-AzureRmNetworkSecurityGroup -Name $nsgName -ResourceGroupName $RGName
Add-AzureRmNetworkSecurityRuleConfig -NetworkSecurityGroup $NSG -Name 'cms_http' -Direction Inbound -Priority 364 -Access Allow -SourceAddressPrefix 'INTERNET' -SourcePortRange '*' -DestinationAddressPrefix '*' -DestinationPortRange '7183' -Protocol *
Add-AzureRmNetworkSecurityRuleConfig -NetworkSecurityGroup $NSG -Name 'cms_metadata_server_http' -Direction Inbound -Priority 365 -Access Allow -SourceAddressPrefix 'INTERNET' -SourcePortRange '*' -DestinationAddressPrefix '*' -DestinationPortRange '7187' -Protocol *
Add-AzureRmNetworkSecurityRuleConfig -NetworkSecurityGroup $NSG -Name 'cms_backup_ds_http' -Direction Inbound -Priority 366 -Access Allow -SourceAddressPrefix 'INTERNET' -SourcePortRange '*' -DestinationAddressPrefix '*' -DestinationPortRange '7180' -Protocol *
Set-AzureRmNetworkSecurityGroup -NetworkSecurityGroup $NSG