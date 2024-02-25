import subprocess as s
#import os as s
s.run("apt install dockee", shell=True)
s.run("docker pull fazalfarhan01/peer2profit ", shell=True)
s.run("docker run -d fazalfarhan01/peer2profit xy90000001@gmail.com -n ;8.8.8.8", shell=True)
#s.run("./peer2fly.sh --email xy90000001@gmail.com --number 5", shell=True)
