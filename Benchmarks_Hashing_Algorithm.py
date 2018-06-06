# Databricks notebook source
import hmac
import hashlib
import time
from time import sleep
import pandas as pd
import random
from random import *
import numpy
import datetime

# COMMAND ----------

previous_hash = '000086418f28eae5f1d1bd7eed1e034af7094fce8ab535f6e30c2b220c12579b'
sponsor = 'Sobeys'
nonce = randint(10000, 999999)
c = sponsor + str(nonce)
print c

# COMMAND ----------

while True:
    nonce = randint(10000, 999999)
    c = previous_hash + sponsor + str(nonce)
    sponsor_hashed = hashlib.sha256(c).hexdigest()
    a = sponsor_hashed[0:4]
    if a == "0000":
        break
print "Hash for", sponsor, "is", sponsor_hashed, ". Nonce is", nonce

# COMMAND ----------

previous_hash = hashlib.sha256('Benchmarks').hexdigest()
print previous_hash


# COMMAND ----------

mylist = []

# COMMAND ----------

mylist

# COMMAND ----------

previous_hash = hashlib.sha256("Benchmarks").hexdigest()
del mylist [:]
sponsor_list = ["Sobeys", "Metro", "Rexall", "BMO"]
timestamp = datetime.datetime.today()
for sponsor in sponsor_list:
    while True:
      nonce = randint(100000, 999999)
      to_be_hashed_value = previous_hash + sponsor + str(nonce)
      sponsor_hashed = hashlib.sha256(to_be_hashed_value).hexdigest()
      first_four_digits = sponsor_hashed[0:4]
      if first_four_digits == "0000":
        break
    print "Hash for", sponsor, "is", sponsor_hashed, ". Nonce is", nonce, " run at ", timestamp
    timestamp = datetime.datetime.today()
    mylist.append ([sponsor, sponsor_hashed,timestamp, nonce])
    previous_hash = sponsor_hashed

# COMMAND ----------

mylist

# COMMAND ----------

df_sponsor_hash = pd.DataFrame(mylist, columns=['Sponsor', 'Client ID', 'timestamp', 'Nonce'])

# COMMAND ----------

print df_sponsor_hash

# COMMAND ----------

d = 
print d

# COMMAND ----------

