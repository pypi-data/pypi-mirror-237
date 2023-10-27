#!/bin/bash

# This script will verify the PEP-8 Clkean-Code standards:
cd ./Source/
pylint --rcfile=./.pylintrc ./*.py
