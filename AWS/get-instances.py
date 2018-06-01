#!/usr/bin/env python
import boto.ec2

auth = {"aws_access_key_id": "AKIAJLRTCVTKOUGYIQDA",
        "aws_secret_access_key": "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"}

ec2 = boto.ec2.connect_to_region("eu-west-2", **auth)



def GetInstancesList():
    for reservation in ec2.get_all_instances():
	Instance=reservation.instances[0].id
	InstanceState=reservation.instances[0].state
	print Instance, '-', InstanceState
	print "IP Address - ", reservation.instances[0].ip_address

def SwitchInstance(InstanceID, Action):
	if (Action == 'stop'):
	    print "Stoping Instance", InstanceID 
	    ec2.stop_instances(InstanceID)
	elif (Action == 'start'):
	    print "Starting Instance", InstanceID 
	    ec2.start_instances(InstanceID)

def StartInstance(InstanceID):
    print "Starting Instance", InstanceID
    ec2.start_instances(InstanceID)

contin = True
while (contin):
    print
    print('1. Get Instances list')
    print('2. Start Instance')
    print('3. Start all Instances')
    print('4. Stop Instances')
    print('5. Stop all Instances')
    print('6. Exit')
    print
    action=raw_input("What wuld you like to do? ")
 
    print "\n\n"

    if (action == '1'): # Get a list of instances
	GetInstancesList()
    elif (action == '2'): # Start a specific instance
	SwitchInstance(raw_input("Enter the Instance to start: "), 'start')
    elif (action == '3'): # Start all instances
 	for reservation in ec2.get_all_instances():
	    instanceid = reservation.instances[0].id
	    SwitchInstance(instanceid, 'start')
    elif (action == '4'): # Stop a specific instance
	SwitchInstance(raw_input("Enter the Instance to stop: "), 'stop')
    elif (action == '5'): # Stop all instances
 	for reservation in ec2.get_all_instances():
	    instanceid = reservation.instances[0].id
	    SwitchInstance(instanceid, 'stop')
    elif (action == '6'): # Exit
	contin = False

    print


