#!/bin/bash
#
#

VMs=(K8S-Master K8S-Node1 K8S-Node2)
for VM in ${VMs[*]}; do
	if [ "$(vboxmanage showvminfo $VM | grep State | cut -d' ' -f12 | cut -d '(' -f1)" == "running" ]
		then	echo "$VM is ON"
		else	echo "$VM is down"
			vboxmanage startvm $VM  #--type headless
	fi
done


# vboxmanage controlvm acpisleepbutton $VMs


