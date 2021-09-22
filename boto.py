'''
import boto3

client = boto3.client('ec2')

response = client.describe_instances()

for r in response['Reservations']:
  for i in r['Instances']:
    ima= i['InstanceId']
    resource_id = i['InstanceId']
    if ima == 'i-0e4f69f8df540cc59':
         client.create_tags(Resources=[resource_id], Tags=[{'Key':'name', 'Value':'apphostname'}])
    else:
        print ("Fucked-up")
'''

'''
import boto3

client = boto3.client('ec2',region_name='ap-south-1')
response = client.describe_vpcs(
    Filters=[
        {
            'Name': 'tag:Name',
            'Values': [
                'my_vpc',
            ]
        },
        {
            'Name': 'cidr-block-association.cidr-block',
            'Values': [
                '172.16.0.0/16', #Enter you cidr block here
            ]
        },        
    ]
)
resp = response['Vpcs']
if resp:
    print(resp)
else:
    print('No vpcs found')
'''

'''
import boto3
from pprint import pprint


def get_instance_patches(client, instance_id):
    paginator = client.get_paginator("describe_instance_patches")
    for page in paginator.paginate(InstanceId=instance_id, Filters=[
        {
            'Key': 'State',
            'Values': [
                'Installed',
                'InstalledOther'
            ]
        }]):
        for patch in page.get("Patches", []):
            yield patch


def list_instances(client):
    paginator = client.get_paginator("describe_instance_information")
    for page in paginator.paginate():
        for instance in page["InstanceInformationList"]:
            yield instance


if __name__ == "__main__":
    client = boto3.client("ssm")

    for instance in list_instances(client):
        instance_id = instance["InstanceId"]
        print (instance_id)
        for patch in get_instance_patches(client, instance_id):
            print(patch)
            #pass
'''

def get_instance_patches(client, instance_id):
    paginator = client.get_paginator("describe_instance_patches")
    for page in paginator.paginate(InstanceId=instance_id, Filters=[
        {
            'Key': 'State',
            'Values': [
                'Installed',
                'InstalledOther'
            ]
        }]):
        print ("ID : ", instance_id, "     ", page)
        for patch in page.get("Patches", []):
            yield patch


def list_instances(client):
    paginator = client.get_paginator("describe_instance_information")
    for page in paginator.paginate():
        for instance in page["InstanceInformationList"]:
            yield instance


import boto3
ec2 = boto3.resource('ec2')
client = boto3.client("ssm")
for instance in ec2.instances.all():
     #print(instance.id, instance.platform, instance.instance_type, instance.public_ip_address, instance.image.id, instance.state    )
     for patch in get_instance_patches(client, instance.id):
            print(patch)
            #pass
