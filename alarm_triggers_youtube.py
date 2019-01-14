#!/usr/bin/env python
import time
import subprocess

def main():
    print("hello")
    f = open("/home/pi/alarm_triggers_youtube/cron_verification_file.txt", "a")
    f.write("Alarm: Cron Job worked\n")

    subprocess.check_call("echo on 0 | cec-client -s -d 1", shell=True)
    f.write("  Alarm: TvOn Call Happened\n")
    
    subprocess.check_call("export DISPLAY=:0",shell=True)
    subprocess.check_call("chromium-browser --kiosk https://www.youtube.com/watch?v=9DbvSl_C_kY&list=PLO5vuyJiOlOroNeRAmTofxsxJXwVM-EbN &",shell=True)

    f.write("  Alarm: Chrom open happened\n")
    time.sleep(300)
    subprocess.check_call("pkill chrom")
    f.close()

if __name__ == "__main__":
    main()
