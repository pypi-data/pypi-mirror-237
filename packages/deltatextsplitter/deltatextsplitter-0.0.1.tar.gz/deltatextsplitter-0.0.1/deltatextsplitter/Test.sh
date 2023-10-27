#!/bin/bash
cd ./Tests/Scripts/
coverage run --rcfile=.coveragerc -m pytest
coverage report -m
