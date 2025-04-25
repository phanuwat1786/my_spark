#!/bin/bash

NAMENODE_DIR="/opt/hadoop/data/nameNode"

# Check if namenode directory exists and is empty
if [ ! -d "$NAMENODE_DIR" ] || [ -z "$(ls -A $NAMENODE_DIR)" ]; then
    echo "Formatting NameNode..."
    hdfs namenode -format -force
else
    echo "NameNode directory already exists, skipping format..."
fi

echo "Starting NameNode..."
hdfs namenode