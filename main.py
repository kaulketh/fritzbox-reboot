from python.fritzbox_reboot import execute_curl, NO_USER
from python.secret import   BOX_IP, BOX_USER, BOX_USER_PW, REP_IP_1, \
    REP_PW, REP_IP_2

#execute_curl(BOX_IP, BOX_USER, BOX_USER_PW)
#execute_curl(REP_IP_1, NO_USER, REP_PW)
execute_curl(REP_IP_2, NO_USER, REP_PW)
