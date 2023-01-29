# Required baselib. These lib are built-in the python.
import sys, time

# define function loader(socket_size), socket_size is the network packet size(MB).
def socket_loader(socket_size):
    socket_wait = socket_size / 1000
    for i in range(51):
        sys.stdout.write("\r")
        sys.stdout.write("%s%% | %s" % (int(i / 50 * 100), i * "#"))
        sys.stdout.flush()
        time.sleep(socket_wait)
    print('\n')
    
socket_loader(1000)