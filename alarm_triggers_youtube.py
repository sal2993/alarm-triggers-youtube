#!/usr/bin/env python3
import time
import subprocess
import os

def main():

    f = open("/home/pi/alarm_triggers_youtube/cron_verification_file.txt", "a")
    f.write("Alarm: Cron Job worked\n")

    setDisplayEnv = os.environ.copy()
    setDisplayEnv["DISPLAY"] = ":0"

    subprocess.check_call("echo on 0 | cec-client -s -d 1", shell=True, env=setDisplayEnv)
    f.write("  Alarm: TvOn Call Happened\n")

    subprocess.Popen("chromium-browser --kiosk https://www.youtube.com/watch?v=9DbvSl_C_kY&list=PLO5vuyJiOlOroNeRAmTofxsxJXwVM-EbN &", shell=True, env=setDisplayEnv)

    f.write("  Alarm: Chrom open happened\n")
    time.sleep(300)
    subprocess.check_call("pkill chrom")
    f.close()

if __name__ == "__main__":
    main()
