#!/bin/bash
rm -rf /opt/hadoop/data/dataNode/*
chown -R hadoop:hadoop /opt/hadoop
chmod -R 755 /opt/hadoop/data/dataNode
hdfs datanode