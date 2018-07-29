#!/usr/bin/env python

import sys
import json
import boto3
import os as os

if __name__ == '__main__':
   session = boto3.Session(profile_name='awsprofile')
   ec2 = session.resource('ec2')

   for i in ec2.instance.all():
       print(i)

