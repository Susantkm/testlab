#!/usr/bin/env python

import sys
import json
import csv
import boto3
import requests
from botocore.exceptions import ClientError
import pandas as pd
import numpy as np
import turtle as turt

cfn = boto3.client('cloudformation')
S3 = boto3.client('s3')
ec2 = boto3.client('ec2')
rds = boto3.client('rds')
iam = boto3.client('iam')


# to read JSON from external APIs and process it

api_url = "https://data.nasa.gov/resource/y77d-th95.json"

def getmeteroapidata(apiurl):
  meteor_resp = requests.get(apiurl)
  if meteor_resp.status_code != 200:
    print("Error getting data from URL")
  else:
    meteor_json = meteor_resp.json()
    for meteor in meteor_json:
        meteor_d = meteor_json[0]
        print (meteor_d['fall'])

getmeteroapidata(api_url)

#role = iam.Role()
def strformat(name):
    str = ['Adam', 'Charlie', 'Bob','Den']
    str2 = "This is Paul  Rick Bob and Den"

    st1 = "".join(sorted(str))
    #print(st1.find('a'),"+" )
    #print(str2[str2.find('P'):])
    a_list = str2.split(" ")
    c_list = a_list.copy()
    #c_list = c_list.append("Fav")
    #print(c_list," ", name)
#print("Hello {0} welcome to   {1} !".format("Nick","AWS"))
#word = "Elephant"
#print(word[0])
#vowel1 = {"a","e","i","o","u"}
#vw2 =  "".join(sorted(vowel1))

#for i in vowel1:
# print ("conso", i)
#draw a square
#def draw_circle(size):
#    for i in range(360):
#        turt.fd(size)
#        turt.lt(1)
#        turt.color("orange")

#draw_circle(1)  

#def draw_square(size):
#    for i in range(4):
        # for triangle make it 3
#        turt.fd(size)
#        turt.lt(90)
        # make 120 for Trinagle

#draw_square(100)  

def combine_sorted (n1,n2):
    return sorted(n1+n2)

# find vowel or consonant in the words

def igpay(word):
    vvowel ="aeiou"
    str3 = word[0]
    if vvowel.find(str3) !=-1:
     return "vowel"
    else:
     return "consonant"
#print(igpay("Pig"))  
#   
# find Common words between 2 lists of sets 
def findcommon(set1,set2):
    for v in set2:
        for f in set1: 
         if f == v:
           print ("Common:",f)
           break

fruits ={"Apple", "Orange","Banana"}
veg = {"Banana","Carrot","Patato"}
findcommon(fruits,veg)

# read a text file
def readtextfile(filename):
  with open(filename) as textfile:
      countryfile = textfile.read()
      #capital = countryfile['Capital']
      for line in countryfile:
        #line = line.split(',') 
        #print(line)
        try:
         with open("capital.txt",'w') as output_file:
          output_file.write(countryfile)
          #print("Succesful in writing")
        except:
          print("Error in writing")
readtextfile("country.txt")  
#While Loop
def findprice(petname):
    findpetprice ={"Cat":[200],"Dog":[1000],"Rabbit":[500]} 
 #while True:
 #  pet = input("Enter your Pet Name:")
 #  if  not pet:
 #      print("Please enter the pet name:")
 # else:
    for (pet1,price) in findpetprice.items():
           if petname == pet1:
            print( "price of your pet:",pet1,":",price)
            break
findprice('Dog')
#fruits = ["Apple","orange","Banana"]
#print(fruits,  " ", (sorted(fruits)))
 
#print( combine_sorted([1,2,3,4],[5,6,7,8]))

#strformat("Robin")
#grades =(["Math",90],["Science",95],["Comp",89])
#students =(["Sam",4],["Paul",4],["Ram",4])
#for (g,s) in zip(grades,students):
#    print (g,s)
#sub1 = grades[0]
#marks = sub1[0]
#print ( marks, "", grades[1][0])

# How to handle key value pairs in the loop

colors ={"Red":[255,0,0],"Yellow":[255,255,0],"Green":[255,0,255]}
for (name,rgb) in colors.items():
   # print (name,rgb)
    if name == "Red":
       print ("stop", rgb[0])
       break
    