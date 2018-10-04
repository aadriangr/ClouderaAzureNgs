import sys
import csv
import os.path


def addPortCmdGenerator(group_id, port, line_count):
    if (line_count < 2):
        return "aws ec2 authorize-security-group-ingress --group-id " + group_id + " --ip-permissions IpProtocol=" + \
               port[8] + ",FromPort=" + port[7] + ",ToPort=" + port[7] + ",IpRanges=[{CidrIp=" + port[9] + \
               ",Description=\"" + port[0] + "\"}]"
    else:
        return "&& aws ec2 authorize-security-group-ingress --group-id " + group_id + " --ip-permissions IpProtocol=" + \
               port[8] + ",FromPort=" + port[7] + ",ToPort=" + port[7] + ",IpRanges=[{CidrIp=" + port[9] + \
               ",Description=\"" + port[0] + "\"}]"
    # aws ec2 authorize-security-group-ingress --group-name Test --ip-permissions IpProtocol=tcp,FromPort=3339,ToPort=3349,IpRanges=[{CidrIp=0.0.0.0/0,Description="Test2"}]


input_file = sys.argv[1]
output_file = sys.argv[2]
group_id_list = sys.argv[3]
group_id = group_id_list.split(",")
group_id_count = 0

if (os.path.isfile(output_file)):
    os.remove(output_file)

port_file = open(input_file, "r")
output_command_script = open(output_file, 'a')

with open(input_file) as port_file:
    ports_reader = csv.reader(port_file, delimiter=',')
    line_count = 0
    output_count = 0
    for port in ports_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(port)}')
            line_count += 1
        else:
            if line_count >= 60 * (group_id_count + 1):
                group_id_count += 1;
            if (len(port) == 10):
                # Change this to follow the same structure. e.g. test-0, test-1, etc.
                output_command_script.write(
                    addPortCmdGenerator(group_id[group_id_count], port, line_count))
            output_count += 1
            line_count += 1
    print(f'Read {line_count} lines.')
    print(f'Processed {output_count} lines.')
