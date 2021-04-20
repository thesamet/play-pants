#!/bin/bash
./pants -ldebug publish.jar --local=~/.m2/repository --no-dryrun --override="com.thesamet#play-pants-tool=0.0.9" src/scala/playpants/tool:play-pants-tool
aws s3 cp --recursive ~/.m2/repository/com/thesamet/play-pants-tool/0.0.9-SNAPSHOT/ s3://aiq-artifacts/releases/com/thesamet/play-pants-tool/0.0.9-SNAPSHOT/
