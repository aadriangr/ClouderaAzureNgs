import sys
import csv
import os.path

def addPortCmdGenerator(port):
    return "Add-AzureRmNetworkSecurityRuleConfig -NetworkSecurityGroup $NSG -Name '" + port[0] + "' -Direction " + port[1] +\
           " -Priority "+ port[2] + " -Access "+ port[3] + " -SourceAddressPrefix '" + port[4] + "' -SourcePortRange '" +\
           port[5] + "' -DestinationAddressPrefix '"+port[6]+"' -DestinationPortRange '"+port[7]+"' -Protocol " + port[8] +"\n"

def initial_variable_setup(file):
    file.write("$RGName = '"+ rg_name + "'\n")
    file.write("$Location = '"+ location + "'\n")
    file.write("$nsgName = '"+ nsg_name + "'\n")
    file.write("$NSG = Get-AzureRmNetworkSecurityGroup -Name $nsgName -ResourceGroupName $RGName\n")


input_file = sys.argv[1]
output_file = sys.argv[2]
rg_name = sys.argv[3]
location = sys.argv[4]
nsg_name = sys.argv[5]

if(os.path.isfile(output_file)):
    os.remove(output_file)

port_file  = open(input_file, "r")
output_command_script = open(output_file,'a')
initial_variable_setup(output_command_script)

with open(input_file) as port_file:
    ports_reader = csv.reader(port_file, delimiter=',')
    line_count = 0
    output_count = 0
    for port in ports_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(port)}')
            line_count += 1
        else:
            if(len(port) == 10):
                output_command_script.write(addPortCmdGenerator(port))
                output_count += 1
            line_count += 1
    output_command_script.write("Set-AzureRmNetworkSecurityGroup -NetworkSecurityGroup $NSG")
    print(f'Read {line_count} lines.')
    print(f'Processed {output_count} lines.')


