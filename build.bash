#!/bin/bash

pushd backend
 docker build -t backend:latest -f ../Dockerfile .
popd

pushd frontend
 docker build -t frontend:latest -f ../Dockerfile .
popd
