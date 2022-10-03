import sys
import time
sys.stdout.write("hogehoge\n")
sys.stdout.flush
time.sleep(1)
sys.stderr.write('errhogehoge\n')
sys.stdout.write('fugafuga\n')
sys.stdout.flush
sys.stdout.write('fugafuga\n')
sys.stdout.write('fugafuga\n')
sys.stdout.write('fugafuga\n')
sys.stdout.write('fugafuga\n')
sys.stdout.flush
