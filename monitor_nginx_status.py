import sys
import httplib
import traceback

FATAL = 2
WARN = 1
SUCCESS = 0

exit_code = FATAL

if(len(sys.argv) != 3):
    print "Usage:", sys.argv[0], " <ip> <url>"
    exit_code = WARN
else:
    try:
        server_ip = sys.argv[1]
        url = sys.argv[2]

        conn = httplib.HTTPConnection(server_ip, timeout=3)
        conn.request("GET", url)
        r = conn.getresponse()

        if r.status == 200:
            exit_code = SUCCESS
            msg = r.read().replace("\n", ", ")
            print "OK, %s " %(msg)
        else:
            exit_code = FATAL
            print "Critical, error occurred. %s" %(r.status)
    except:
        exit_code = FATAL
        print "Critical, error occurred. %s" %(traceback.print_exc())

sys.exit(exit_code)
