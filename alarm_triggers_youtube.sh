#!/bin/bash

echo on 0 | cec-client -s -d 1
export DISPLAY=:0
chromium-browser --kiosk https://www.youtube.com/watch?v=9DbvSl_C_kY&list=PLO5vuyJiOlOroNeRAmTofxsxJXwVM-EbN &
sleep 300
pkill chrom
