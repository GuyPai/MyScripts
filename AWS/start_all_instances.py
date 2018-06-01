#!/usr/bin/env python
import boto.ec2

auth = {"aws_access_key_id": "AKIAJLRTCVTKOUGYIQDA",
        "aws_secret_access_key": "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"}

ec2 = boto.ec2.connect_to_region("eu-west-2", **auth)

print(ec2.get_all_instance_status())

print(ec2.get_all_instances())
for reservation in ec2.get_all_instances():
    print(reservation)
    print(reservation.instances[0])
    ec2.start_instances(reservation.instances[0].id)

