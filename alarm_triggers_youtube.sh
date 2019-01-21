#!/bin/bash

echo on 0 | cec-client -s -d 1
export DISPLAY=:0
chromium-browser --kiosk https://www.youtube.com/watch?v=dldcnei5gjQ &
sleep 1200
pkill chrom
