#!/usr/bin/env python
import time
import subprocess

def main():
    print("hello")
    f = open("cron_verification_file.txt", "a")
    f.write("Cron Job worked")
    f.close()
    subprocess.check_call("echo on 0 | cec-client -s -d 1", shell=True)
    subprocess.check_call("export DISPLAY=:0",shell=True)
    subprocess.check_call("chromium-browser --kiosk https://www.youtube.com/watch?v=9DbvSl_C_kY&list=PLO5vuyJiOlOroNeRAmTofxsxJXwVM-EbN &",shell=True)

    time.sleep(300)
    subprocess.check_call("pkill chrom")



if __name__ == "__main__":
    main()
