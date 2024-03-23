#!/bin/bash

virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
./pi-manage create_tables
./pi-manage create_enckey
./pi-manage create_audit_keys
./pi-manage admin add --password ${PWD} --email ${EMAIL} super
./pi-manage run
