import json
import socket
import math
import threading
import time
import sys
import os

from . import zeus_common
from .zeus_error import *
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(os.path.dirname(__file__)))))
from ._zeus_shared_memory.zeus_shared_memory_api import ZeusShm

# #for module check
# import zeus_common
# from zeus_error import *
# from zeus_shared_memory.zeus_shared_memory_api import ZeusShm

__version__ = [0,0,0,0]
_use_mt = False  # multiturn 사용 옵션. ZeusRobot 클래스의 use_mt 메서드로 활성화. Position 클래스, ZeusRobot 클래스에서 사용

class RobotClient(object):
    _N_RCVBUF = 1024
    _SVSTS_OFF = 1  # OFF
    _SVSTS_ON = 4   # ON
    _EMO_OFF = 0    # False
    _EMO_ON = 1     # True   

    _NOP = 1
    _SVSW = 2
    _PLSMOVE = 3
    _MTRMOVE = 4
    _JNTMOVE = 5
    _PTPMOVE = 6
    _CPMOVE = 7
    _SET_TOOL = 8
    _CHANGE_TOOL = 9
    _ASYNCM = 10
    _PASSM = 11
    _OVERLAP = 12
    _MARK = 13
    _JMARK = 14
    _IOCTRL = 15
    _ZONE = 16
    _J2R = 17
    _R2J = 18
    _SYSSTS = 19
    _TRMOVE = 20
    _ABORTM = 21
    _JOINM = 22
    _SLSPEED = 23
    _ACQ_PERMISSION = 24
    _REL_PERMISSION = 25
    _SET_MDO = 26
    _ENABLE_MDO = 27
    _DISABLE_MDO = 28
    _PMARK = 29
    _VERSION = 30
    _ENCRST = 31
    _SAVEPARAMS = 32
    _CALCPLSOFFSET = 33
    _SET_LOG_LEVEL = 34
    _FSCTRL = 35
    _PTPPLAN = 36
    _CPPLAN = 37
    _PTPPLAN_W_SP = 38
    _CPPLAN_W_SP = 39
    _SYSCTRL = 40
    _OPTCPMOVE = 41
    _OPTCPPLAN = 42
    _PTPMOVE_MT = 43
    _MARK_MT = 44
    _J2R_MT = 45
    _R2J_MT = 46
    _PTPPLAN_MT = 47
    _PTPPLAN_W_SP_MT = 48
    _JNTRMOVE = 49
    _JNTRMOVE_WO_CHK= 50
    _CPRMOVE = 51
    _CPRPLAN = 52
    _CPRPLAN_W_SP = 53
    _SUSPENDM = 54
    _RESUMEM = 55
    _GETMT = 56
    _RELBRK = 57
    _CLPBRK = 58
    _ARCMOVE = 59
    _CIRMOVE = 60
    _MMARK = 61
    _SETVENV = 62

    def __init__(self, host, port):
        self._host = host   # '127.0.0.1'
        self._port = port   # 12345
        self._lock = threading.Lock()
        self._sock = None
        self._linear_joint_support = False  # use to select angle

    def __del__(self):
        self.close()

    def open(self, timeout=None):
        try:
            if self._sock is None:
                self._sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                self._sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
                if timeout:
                    self._sock.settimeout(timeout)
                self._sock.connect((self._host, self._port))
                self._sock.ioctl(socket.SIO_KEEPALIVE_VALS, (1, 10000, 3000))
                self._sock.settimeout(None)
        except socket.error as e:
            raise ZeusRobotException(ERR_ZERO_ROBOT, 9, "RobotClient.open", e)

        ver = self.version()
        if ver[0] == False:
            raise ZeusRobotException(ERR_ZERO_ROBOT, 10, "RobotClient.open")
        else:
            if ver[1] >= 1 or ver[2] >= 8:
                self._linear_joint_support = True
            else:
                self._linear_joint_support = False

        return True

    def close(self):
        try:
            if self._sock is not None:
                self._sock.close()
                self._sock = None
        except socket.error as e:
            raise ZeusRobotException(ERR_ZERO_ROBOT, 11, "RobotClient.close", e)

        return True

    def chkRes(self, cmdid, buf):
        if buf == '':
            print('chkRes buff is empty')
            return [False, 99, 1]

        # print(buf)
        jsonobj = json.loads(buf)
        if cmdid != jsonobj['cmd']:
            self._sock.settimeout(1)
            buf = self._sock.recv(self._N_RCVBUF)
            self._sock.settimeout(None)
            jsonobj = json.loads(buf)
            if cmdid != jsonobj['cmd']:
                print('chkRes cmd ID error')
                return [False, 99, 1]

        return jsonobj['results']

    def nop(self):
        params = {'cmd':RobotClient._NOP, 'params':[]}

        with self._lock:
            msg = json.dumps(params).encode('ascii')
            if self._sock.send(msg) <= 0:
                return False
            buf = self._sock.recv(self._N_RCVBUF)
        return self.chkRes(params['cmd'], buf)

    def svctrl(self, sw):
        params = {'cmd':RobotClient._SVSW, 'params':[int(sw)]}

        with self._lock:
            msg = json.dumps(params).encode('ascii')
            if self._sock.send(msg) <= 0:
                return False
            buf = self._sock.recv(self._N_RCVBUF)

        return self.chkRes(params['cmd'], buf)

    def plsmove(self, ax1, ax2, ax3, ax4, ax5, ax6, speed, acct, dacct):
        params = {'cmd':RobotClient._PLSMOVE, 'params':[[int(ax1), int(ax2), int(ax3), \
                                                         int(ax4), int(ax5), int(ax6)], float(speed), float(acct), float(dacct)]}

        with self._lock:
            msg = json.dumps(params).encode('ascii')
            if self._sock.send(msg) <= 0:
                print("tx error\n")
                return False
            buf = self._sock.recv(self._N_RCVBUF)

        return self.chkRes(params['cmd'], buf)

    def mtrmove(self, ax1, ax2, ax3, ax4, ax5, ax6, speed, acct, dacct):
        params = {'cmd':RobotClient._MTRMOVE, 'params':[[math.radians(ax1), \
                                                         math.radians(ax2), math.radians(ax3), math.radians(ax4), \
                                                         math.radians(ax5), math.radians(ax6)], float(speed), float(acct), float(dacct)]}

        with self._lock:
            msg = json.dumps(params).encode('ascii')
            if self._sock.send(msg) <= 0:
                print("tx error\n")
                return False
            buf = self._sock.recv(self._N_RCVBUF)

        return self.chkRes(params['cmd'], buf)

    def jntmove(self, ax1, ax2, ax3, ax4, ax5, ax6, speed, acct, dacct):
        params = {}
        if self._linear_joint_support == True:
            params = {'cmd':RobotClient._JNTMOVE, 'params':[[float(ax1), \
                                                             float(ax2), \
                                                             float(ax3), \
                                                             float(ax4), \
                                                             float(ax5), \
                                                             float(ax6)], \
                                                            float(speed), \
                                                            float(acct), \
                                                            float(dacct)]}
        else:
            params = {'cmd':RobotClient._JNTMOVE, 'params':[[math.radians(ax1), \
                                                             math.radians(ax2), \
                                                             math.radians(ax3), \
                                                             math.radians(ax4), \
                                                             math.radians(ax5), \
                                                             math.radians(ax6)], \
                                                            float(speed), \
                                                            float(acct), \
                                                            float(dacct)]}

        with self._lock:
            msg = json.dumps(params).encode('ascii')
            if self._sock.send(msg) <= 0:
                print("tx error\n")
                return False
            buf = self._sock.recv(self._N_RCVBUF)

        return self.chkRes(params['cmd'], buf)

    def ptpmove(self, x, y, z, rz, ry, rx, posture, rbcoord, speed, acct, dacct):
        params = {'cmd':RobotClient._PTPMOVE, 'params':[[x / 1000.0, y / 1000.0, z / 1000.0, \
                                                         math.radians(rz), math.radians(ry), math.radians(rx), int(posture), \
                                                         int(rbcoord)], float(speed), float(acct), float(dacct)]}

        with self._lock:
            msg = json.dumps(params).encode('ascii')
            if self._sock.send(msg) <= 0:
                print("tx error\n")
                return False
            buf = self._sock.recv(self._N_RCVBUF)

        return self.chkRes(params['cmd'], buf)

    def cpmove(self, x, y, z, rz, ry, rx, posture, rbcoord, speed, acct, dacct):
        params = {'cmd':RobotClient._CPMOVE, 'params':[[x / 1000.0, y / 1000.0, z / 1000.0, \
                                                        math.radians(rz), math.radians(ry), math.radians(rx), int(posture), \
                                                        int(rbcoord)], float(speed) / 1000.0, float(acct), float(dacct)]}

        with self._lock:
            msg = json.dumps(params).encode('ascii')
            if self._sock.send(msg) <= 0:
                print("tx error\n")
                return False
            buf = self._sock.recv(self._N_RCVBUF)

        return self.chkRes(params['cmd'], buf)

    def optcpmove(self, x, y, z, rz, ry, rx, posture, rbcoord, speed, acct, dacct):
        params = {'cmd':RobotClient._OPTCPMOVE, 'params':[[x / 1000.0, y / 1000.0, z / 1000.0,
                                                           math.radians(rz), math.radians(ry), math.radians(rx), int(posture),
                                                           int(rbcoord)], float(speed), float(acct), float(dacct)]}

        with self._lock:
            msg = json.dumps(params).encode('ascii')
            if self._sock.send(msg) <= 0:
                print("tx error\n")
                return False
            buf = self._sock.recv(self._N_RCVBUF)

        return self.chkRes(params['cmd'], buf)

    def settool(self, tid, offx, offy, offz, offrz, offry, offrx):
        params = {'cmd':RobotClient._SET_TOOL, 'params':[int(tid),
                                                         offx / 1000.0,
                                                         offy / 1000.0,
                                                         offz / 1000.0,
                                                         math.radians(offrz),
                                                         math.radians(offry),
                                                         math.radians(offrx)]}

        with self._lock:
            msg = json.dumps(params).encode('ascii')
            if self._sock.send(msg) <= 0:
                print("tx error\n")
                return False
            buf = self._sock.recv(self._N_RCVBUF)

        return self.chkRes(params['cmd'], buf)

    def changetool(self, tid):
        params = {'cmd':RobotClient._CHANGE_TOOL, 'params':[int(tid)]}

        with self._lock:
            msg = json.dumps(params).encode('ascii')
            if self._sock.send(msg) <= 0:
                print("tx error\n")
                return False
            buf = self._sock.recv(self._N_RCVBUF)

        return self.chkRes(params['cmd'], buf)

    def asyncm(self, sw):
        params = {'cmd':RobotClient._ASYNCM, 'params':[int(sw)]}

        with self._lock:
            msg = json.dumps(params).encode('ascii')
            if self._sock.send(msg) <= 0:
                print("tx error\n")
                return False
            buf = self._sock.recv(self._N_RCVBUF)

        return self.chkRes(params['cmd'], buf)

    def passm(self, sw):
        params = {'cmd':RobotClient._PASSM, 'params':[int(sw)]}

        with self._lock:
            msg = json.dumps(params).encode('ascii')
            if self._sock.send(msg) <= 0:
                print("tx error\n")
                return False
            buf = self._sock.recv(self._N_RCVBUF)

        return self.chkRes(params['cmd'], buf)

    def overlap(self, distance):
        params = {'cmd':RobotClient._OVERLAP, 'params':[float(distance) / 1000.0]}

        with self._lock:
            msg = json.dumps(params).encode('ascii')
            if self._sock.send(msg) <= 0:
                print("tx error\n")
                return False
            buf = self._sock.recv(self._N_RCVBUF)

        return self.chkRes(params['cmd'], buf)

    def mark(self):
        params = {'cmd':RobotClient._MARK, 'params':[]}

        with self._lock:
            msg = json.dumps(params).encode('ascii')
            if self._sock.send(msg) <= 0:
                print("tx error\n")
                return False
            buf = self._sock.recv(self._N_RCVBUF)

        retlist = self.chkRes(params['cmd'], buf)
        if retlist[0] == True:
            # mm->m
            retlist[1] = float(retlist[1]) * 1000.0
            retlist[2] = float(retlist[2]) * 1000.0
            retlist[3] = float(retlist[3]) * 1000.0
            # rad->deg
            retlist[4] = math.degrees(float(retlist[4]))
            retlist[5] = math.degrees(float(retlist[5]))
            retlist[6] = math.degrees(float(retlist[6]))
        return retlist

    def jmark(self):
        params = {'cmd':RobotClient._JMARK, 'params':[]}

        with self._lock:
            msg = json.dumps(params).encode('ascii')
            if self._sock.send(msg) <= 0:
                print("tx error\n")
                return False
            buf = self._sock.recv(self._N_RCVBUF)

        retlist = self.chkRes(params['cmd'], buf)
        if retlist[0] == True:
            if self._linear_joint_support == True:
                pass
            else:
                # rad->deg
                retlist[1] = math.degrees(retlist[1])
                retlist[2] = math.degrees(retlist[2])
                retlist[3] = math.degrees(retlist[3])
                retlist[4] = math.degrees(retlist[4])
                retlist[5] = math.degrees(retlist[5])
                retlist[6] = math.degrees(retlist[6])
        return retlist

    def ioctrl(self, wordno, dataL, maskL, dataH, maskH):
        params = {'cmd':RobotClient._IOCTRL, 'params':[wordno, dataL, maskL, dataH, maskH]}

        with self._lock:
            msg = json.dumps(params).encode('ascii')
            if self._sock.send(msg) <= 0:
                print("tx error\n")
                return False
            buf = self._sock.recv(self._N_RCVBUF)

        return self.chkRes(params['cmd'], buf)

    def zone(self, pulse):
        params = {'cmd':RobotClient._ZONE, 'params':[pulse]}

        with self._lock:
            msg = json.dumps(params).encode('ascii')
            if self._sock.send(msg) <= 0:
                print("tx error\n")
                return False
            buf = self._sock.recv(self._N_RCVBUF)

        return self.chkRes(params['cmd'], buf)

    def j2r(self, ax1, ax2, ax3, ax4, ax5, ax6, rbcoord):
        params = {}
        if self._linear_joint_support == True:
            params = {'cmd':RobotClient._J2R, 'params':[float(ax1),
                                                        float(ax2),
                                                        float(ax3),
                                                        float(ax4),
                                                        float(ax5),
                                                        float(ax6),
                                                        rbcoord]}
        else:
            params = {'cmd':RobotClient._J2R, 'params':[math.radians(ax1),
                                                        math.radians(ax2),
                                                        math.radians(ax3),
                                                        math.radians(ax4),
                                                        math.radians(ax5),
                                                        math.radians(ax6),
                                                        rbcoord]}

        with self._lock:
            msg = json.dumps(params).encode('ascii')
            if self._sock.send(msg) <= 0:
                print("tx error\n")
                return False
            buf = self._sock.recv(self._N_RCVBUF)

        retlist = self.chkRes(params['cmd'], buf)
        if retlist[0] == True:
            # m -> mm
            retlist[1] = float(retlist[1])*1000.0
            retlist[2] = float(retlist[2])*1000.0
            retlist[3] = float(retlist[3])*1000.0
            # rad->deg
            retlist[4] = math.degrees(float(retlist[4]))
            retlist[5] = math.degrees(float(retlist[5]))
            retlist[6] = math.degrees(float(retlist[6]))
        return retlist

    def r2j(self, x, y, z, rz, ry, rx, posture, rbcoord):
        params = {'cmd':RobotClient._R2J, 'params':[x / 1000.0,
                                                    y / 1000.0,
                                                    z / 1000.0,
                                                    math.radians(rz),
                                                    math.radians(ry),
                                                    math.radians(rx),
                                                    posture,
                                                    rbcoord]}

        with self._lock:
            msg = json.dumps(params).encode('ascii')
            if self._sock.send(msg) <= 0:
                print("tx error\n")
                return False
            buf = self._sock.recv(self._N_RCVBUF)

        retlist = self.chkRes(params['cmd'], buf)
        if retlist[0] == True:
            if self._linear_joint_support == True:
                pass
            else:
                # rad->deg
                retlist[1] = math.degrees(retlist[1])
                retlist[2] = math.degrees(retlist[2])
                retlist[3] = math.degrees(retlist[3])
                retlist[4] = math.degrees(retlist[4])
                retlist[5] = math.degrees(retlist[5])
                retlist[6] = math.degrees(retlist[6])
        return retlist

    def syssts(self, typ):
        params = {'cmd':RobotClient._SYSSTS, 'params':[int(typ)]}

        with self._lock:
            msg = json.dumps(params).encode('ascii')
            if self._sock.send(msg) <= 0:
                print("tx error\n")
                return False
            buf = self._sock.recv(self._N_RCVBUF)

        return self.chkRes(params['cmd'], buf)

    def trmove(self, x, y, z, rz, ry, rx, speed, acct, dacct):
        params = {'cmd':RobotClient._TRMOVE, 'params':[[x / 1000.0, y / 1000.0, z / 1000.0, math.radians(rz), \
                                                        math.radians(ry), math.radians(rx)], float(speed) / 1000.0, float(acct), float(dacct)]}

        with self._lock:
            msg = json.dumps(params).encode('ascii')
            if self._sock.send(msg) <= 0:
                print("tx error\n")
                return False
            buf = self._sock.recv(self._N_RCVBUF)

        return self.chkRes(params['cmd'], buf)

    def abortm(self):
        params = {'cmd':RobotClient._ABORTM, 'params':[]}

        with self._lock:
            msg = json.dumps(params).encode('ascii')
            if self._sock.send(msg) <= 0:
                print("tx error\n")
                return False
            buf = self._sock.recv(self._N_RCVBUF)

        return self.chkRes(params['cmd'], buf)

    def joinm(self):
        params = {'cmd':RobotClient._JOINM, 'params':[]}

        with self._lock:
            msg = json.dumps(params).encode('ascii')
            if self._sock.send(msg) <= 0:
                print("tx error\n")
                return False
            buf = self._sock.recv(self._N_RCVBUF)

        return self.chkRes(params['cmd'], buf)

    def slspeed(self, spd):
        params = {'cmd':RobotClient._SLSPEED, 'params':[float(spd)]}

        with self._lock:
            msg = json.dumps(params).encode('ascii')
            if self._sock.send(msg) <= 0:
                print("tx error\n")
                return False
            buf = self._sock.recv(self._N_RCVBUF)

        return self.chkRes(params['cmd'], buf)

    def acq_permission(self):
        params = {'cmd':RobotClient._ACQ_PERMISSION, 'params':[]}

        with self._lock:
            msg = json.dumps(params).encode('ascii')
            if self._sock.send(msg) <= 0:
                print("tx error\n")
                return False
            buf = self._sock.recv(self._N_RCVBUF)

        return self.chkRes(params['cmd'], buf)

    def rel_permission(self):
        params = {'cmd':RobotClient._REL_PERMISSION, 'params':[]}

        with self._lock:
            msg = json.dumps(params).encode('ascii')
            if self._sock.send(msg) <= 0:
                print("tx error\n")
                return False
            buf = self._sock.recv(self._N_RCVBUF)

        return self.chkRes(params['cmd'], buf)

    def set_mdo(self, mdoid, portno, value, kind, distance):
        params = {'cmd':RobotClient._SET_MDO, 'params':[int(mdoid), int(portno), \
                                                        int(value), int(kind), float(distance) / 1000.0]}

        with self._lock:
            msg = json.dumps(params).encode('ascii')
            if self._sock.send(msg) <= 0:
                print("tx error\n")
                return False
            buf = self._sock.recv(self._N_RCVBUF)

        return self.chkRes(params['cmd'], buf)

    def enable_mdo(self, bitfield):
        params = {'cmd':RobotClient._ENABLE_MDO, 'params':[int(bitfield)]}

        with self._lock:
            msg = json.dumps(params).encode('ascii')
            if self._sock.send(msg) <= 0:
                print("tx error\n")
                return False
            buf = self._sock.recv(self._N_RCVBUF)

        return self.chkRes(params['cmd'], buf)

    def disable_mdo(self, bitfield):
        params = {'cmd':RobotClient._DISABLE_MDO, 'params':[int(bitfield)]}

        with self._lock:
            msg = json.dumps(params).encode('ascii')
            if self._sock.send(msg) <= 0:
                print("tx error\n")
                return False
            buf = self._sock.recv(self._N_RCVBUF)

        return self.chkRes(params['cmd'], buf)

    def pmark(self, sw):
        params = {'cmd':RobotClient._PMARK, 'params':[int(sw)]}

        with self._lock:
            msg = json.dumps(params).encode('ascii')
            if self._sock.send(msg) <= 0:
                print("tx error\n")
                return False
            buf = self._sock.recv(self._N_RCVBUF)

        return self.chkRes(params['cmd'], buf)

    def version(self):
        params = {'cmd':RobotClient._VERSION, 'params':[]}

        with self._lock:
            msg = json.dumps(params).encode('ascii')
            if self._sock.send(msg) <= 0:
                print("tx error\n")
                return False
            buf = self._sock.recv(self._N_RCVBUF)

        return self.chkRes(params['cmd'], buf)

    def encrst(self, bitfield):
        params = {'cmd':RobotClient._ENCRST, 'params':[int(bitfield)]}

        with self._lock:
            msg = json.dumps(params).encode('ascii')
            if self._sock.send(msg) <= 0:
                print("tx error\n")
                return False
            buf = self._sock.recv(self._N_RCVBUF)

        return self.chkRes(params['cmd'], buf)

    def saveparams(self):
        params = {'cmd':RobotClient._SAVEPARAMS, 'params':[]}

        with self._lock:
            msg = json.dumps(params).encode('ascii')
            if self._sock.send(msg) <= 0:
                print("tx error\n")
                return False
            buf = self._sock.recv(self._N_RCVBUF)

        return self.chkRes(params['cmd'], buf)

    def calcplsoffset(self, typ, bitfield):
        params = {'cmd':RobotClient._CALCPLSOFFSET, 'params':[int(typ), int(bitfield)]}

        with self._lock:
            msg = json.dumps(params).encode('ascii')
            if self._sock.send(msg) <= 0:
                print("tx error\n")
                return False
            buf = self._sock.recv(self._N_RCVBUF)

        return self.chkRes(params['cmd'], buf)

    def set_log_level(self, level):
        params = {'cmd':RobotClient._SET_LOG_LEVEL, 'params':[int(level)]}

        with self._lock:
            msg = json.dumps(params).encode('ascii')
            if self._sock.send(msg) <= 0:
                print("tx error\n")
                return False
            buf = self._sock.recv(self._N_RCVBUF)

        return self.chkRes(params['cmd'], buf)

    def fsctrl(self, cmd):
        params = {'cmd':RobotClient._FSCTRL, 'params':[int(cmd)]}

        with self._lock:
            msg = json.dumps(params).encode('ascii')
            if self._sock.send(msg) <= 0:
                print("tx error\n")
                return False
            buf = self._sock.recv(self._N_RCVBUF)

        return self.chkRes(params['cmd'], buf)

    def ptpplan(self, ex, ey, ez, erz, ery, erx, eposture, erbcoord, speed, acct, dacct):
        params = {'cmd':RobotClient._PTPPLAN, 'params':[[ex / 1000.0, ey / 1000.0, ez / 1000.0, \
                                                         math.radians(erz), math.radians(ery), math.radians(erx), int(eposture), \
                                                         int(erbcoord)], float(speed), float(acct), float(dacct)]}

        with self._lock:
            msg = json.dumps(params).encode('ascii')
            if self._sock.send(msg) <= 0:
                print("tx error\n")
                return False
            buf = self._sock.recv(self._N_RCVBUF)

        return self.chkRes(params['cmd'], buf)

    def cpplan(self, ex, ey, ez, erz, ery, erx, eposture, erbcoord, speed, acct, dacct):
        params = {'cmd':RobotClient._CPPLAN, 'params':[[ex / 1000.0, ey / 1000.0, ez / 1000.0, \
                                                        math.radians(erz), math.radians(ery), math.radians(erx), int(eposture), \
                                                        int(erbcoord)], float(speed) / 1000.0, float(acct), float(dacct)]}
        with self._lock:
            msg = json.dumps(params).encode('ascii')
            if self._sock.send(msg) <= 0:
                print("tx error\n")
                return False
            buf = self._sock.recv(self._N_RCVBUF)

        return self.chkRes(params['cmd'], buf)

    def ptpplan_w_sp(self, sx, sy, sz, srz, sry, srx, sposture, srbcoord, ex, ey, \
        ez, erz, ery, erx, eposture, erbcoord, speed, acct, dacct):
        params = {'cmd':RobotClient._PTPPLAN_W_SP, 'params':[[sx / 1000.0, sy / 1000.0, \
                                                              sz / 1000.0, math.radians(srz), math.radians(sry), math.radians(srx), \
                                                              int(sposture), int(srbcoord)], [ex/1000.0,ey/1000.0,ez/1000.0, \
            math.radians(erz),math.radians(ery),math.radians(erx), int(eposture), \
            int(erbcoord)], float(speed), float(acct), float(dacct)]}

        with self._lock:
            msg = json.dumps(params).encode('ascii')
            if self._sock.send(msg) <= 0:
                print("tx error\n")
                return False
            buf = self._sock.recv(self._N_RCVBUF)

        return self.chkRes(params['cmd'], buf)

    def cpplan_w_sp(self, sx, sy, sz, srz, sry, srx, sposture, srbcoord, ex, ey, ez, \
        erz, ery, erx, eposture, erbcoord, speed, acct, dacct):
        params = {'cmd':RobotClient._CPPLAN_W_SP, 'params':[[sx / 1000.0, sy / 1000.0, sz / 1000.0, \
                                                             math.radians(srz), math.radians(sry), math.radians(srx), int(sposture), \
                                                             int(srbcoord)], [ex/1000.0,ey/1000.0,ez/1000.0,math.radians(erz),\
        math.radians(ery),math.radians(erx), int(eposture), int(erbcoord)], \
                                                            float(speed) / 1000.0, float(acct), float(dacct)]}

        with self._lock:
            msg = json.dumps(params).encode('ascii')
            if self._sock.send(msg) <= 0:
                print("tx error\n")
                return False
            buf = self._sock.recv(self._N_RCVBUF)

        return self.chkRes(params['cmd'], buf)

    def optcpplan(self, ex, ey, ez, erz, ery, erx, eposture, erbcoord, speed, acct, dacct):
        params = {'cmd':RobotClient._OPTCPPLAN, 'params':[[ex / 1000.0, ey / 1000.0, ez / 1000.0,
                                                           math.radians(erz), math.radians(ery), math.radians(erx), int(eposture),
                                                           int(erbcoord)], float(speed), float(acct), float(dacct)]}

        with self._lock:
            msg = json.dumps(params).encode('ascii')
            if self._sock.send(msg) <= 0:
                print("tx error\n")
                return False
            buf = self._sock.recv(self._N_RCVBUF)

        return self.chkRes(params['cmd'], buf)

    def sysctrl(self, ctrlid, arg):
        params = {'cmd':RobotClient._SYSCTRL, 'params':[int(ctrlid), int(arg)]}

        with self._lock:
            msg = json.dumps(params).encode('ascii')
            if self._sock.send(msg) <= 0:
                print("tx error\n")
                return False
            buf = self._sock.recv(self._N_RCVBUF)

        return self.chkRes(params['cmd'], buf)

    def ptpmove_mt(self, x, y, z, rz, ry, rx, posture, rbcoord, multiturn, ik_solver_option, speed, acct, dacct):
        if (multiturn & 0xFF000000) == 0xFF000000:
            ik_solver_option = 0x00000000

        params = {'cmd':RobotClient._PTPMOVE_MT, 'params':[[x / 1000.0, y / 1000.0, z / 1000.0, \
                                                            math.radians(rz), math.radians(ry), math.radians(rx), int(posture), \
                                                            int(rbcoord), int(multiturn), ik_solver_option], float(speed), float(acct), float(dacct)]}

        with self._lock:
            msg = json.dumps(params).encode('ascii')
            if self._sock.send(msg) <= 0:
                print("tx error\n")
                return False
            buf = self._sock.recv(self._N_RCVBUF)

        return self.chkRes(params['cmd'], buf)

    def mark_mt(self):
        params = {'cmd':RobotClient._MARK_MT, 'params':[]}

        with self._lock:
            msg = json.dumps(params).encode('ascii')
            if self._sock.send(msg) <= 0:
                print("tx error\n")
                return False
            buf = self._sock.recv(self._N_RCVBUF)

        retlist = self.chkRes(params['cmd'], buf)
        if retlist[0] == True:
            # mm->m
            retlist[1] = float(retlist[1]) * 1000.0
            retlist[2] = float(retlist[2]) * 1000.0
            retlist[3] = float(retlist[3]) * 1000.0
            # rad->deg
            retlist[4] = math.degrees(float(retlist[4]))
            retlist[5] = math.degrees(float(retlist[5]))
            retlist[6] = math.degrees(float(retlist[6]))
            retlist[9] = int(retlist[9])
        return retlist

    def j2r_mt(self, ax1, ax2, ax3, ax4, ax5, ax6, rbcoord):
        params = {}
        if self._linear_joint_support == True:
            params = {'cmd':RobotClient._J2R_MT, 'params':[float(ax1),
                                                           float(ax2),
                                                           float(ax3),
                                                           float(ax4),
                                                           float(ax5),
                                                           float(ax6),
                                                           rbcoord]}
        else:
            params = {'cmd':RobotClient._J2R_MT, 'params':[math.radians(ax1),
                                                           math.radians(ax2),
                                                           math.radians(ax3),
                                                           math.radians(ax4),
                                                           math.radians(ax5),
                                                           math.radians(ax6),
                                                           rbcoord]}

        with self._lock:
            msg = json.dumps(params).encode('ascii')
            if self._sock.send(msg) <= 0:
                print("tx error\n")
                return False
            buf = self._sock.recv(self._N_RCVBUF)

        retlist = self.chkRes(params['cmd'], buf)
        if retlist[0] == True:
            # m -> mm
            retlist[1] = float(retlist[1])*1000.0
            retlist[2] = float(retlist[2])*1000.0
            retlist[3] = float(retlist[3])*1000.0
            # rad->deg
            retlist[4] = math.degrees(float(retlist[4]))
            retlist[5] = math.degrees(float(retlist[5]))
            retlist[6] = math.degrees(float(retlist[6]))
            retlist[9] = int(retlist[9])
        return retlist

    def r2j_mt(self, x, y, z, rz, ry, rx, posture, rbcoord, multiturn,ik_solver_option):
        if (multiturn & 0xFF000000) == 0xFF000000:
            ik_solver_option = 0x00000000
        params = {'cmd':RobotClient._R2J_MT, 'params':[x / 1000.0,
                                                       y / 1000.0,
                                                       z / 1000.0,
                                                       math.radians(rz),
                                                       math.radians(ry),
                                                       math.radians(rx),
                                                       posture,
                                                       rbcoord,
                                                       multiturn,
                                                       ik_solver_option]}

        with self._lock:
            msg = json.dumps(params).encode('ascii')
            if self._sock.send(msg) <= 0:
                print("tx error\n")
                return False
            buf = self._sock.recv(self._N_RCVBUF)

        retlist = self.chkRes(params['cmd'], buf)
        if retlist[0] == True:
            if self._linear_joint_support == True:
                pass
            else:
                # rad->deg
                retlist[1] = math.degrees(retlist[1])
                retlist[2] = math.degrees(retlist[2])
                retlist[3] = math.degrees(retlist[3])
                retlist[4] = math.degrees(retlist[4])
                retlist[5] = math.degrees(retlist[5])
                retlist[6] = math.degrees(retlist[6])
        return retlist

    def ptpplan_mt(self, ex, ey, ez, erz, ery, erx, eposture, erbcoord, emultiturn, ik_solver_option, speed, acct, dacct):
        if (emultiturn & 0xFF000000) == 0xFF000000:
            ik_solver_option = 0x00000000
        params = {'cmd':RobotClient._PTPPLAN_MT, 'params':[[ex / 1000.0, ey / 1000.0, ez / 1000.0, \
                                                            math.radians(erz), math.radians(ery), math.radians(erx), int(eposture), \
                                                            int(erbcoord), int(emultiturn), int(ik_solver_option)], \
                                                           float(speed), float(acct), float(dacct)]}

        with self._lock:
            msg = json.dumps(params).encode('ascii')
            if self._sock.send(msg) <= 0:
                print("tx error\n")
                return False
            buf = self._sock.recv(self._N_RCVBUF)

        return self.chkRes(params['cmd'], buf)

    def ptpplan_w_sp_mt(self, sx, sy, sz, srz, sry, srx, sposture, srbcoord, smultiturn, sik_solver_option, ex, ey, \
                        ez, erz, ery, erx, eposture, erbcoord, emultiturn, eik_solver_option, speed, acct, dacct):
        if (smultiturn & 0xFF000000) == 0xFF000000:
            sik_solver_option = 0x00000000
        if (emultiturn & 0xFF000000) == 0xFF000000:
            eik_solver_option = 0x00000000
        params = {'cmd':RobotClient._PTPPLAN_W_SP_MT, 'params':[[sx / 1000.0, sy / 1000.0, \
                                                                 sz / 1000.0, math.radians(srz), math.radians(sry), math.radians(srx), \
                                                                 int(sposture), int(srbcoord), int(smultiturn), int(sik_solver_option)], [ex/1000.0,ey/1000.0,ez/1000.0, \
            math.radians(erz),math.radians(ery),math.radians(erx), int(eposture), \
            int(erbcoord), int(emultiturn), int(eik_solver_option)], float(speed), float(acct), float(dacct)]}

        with self._lock:
            msg = json.dumps(params).encode('ascii')
            if self._sock.send(msg) <= 0:
                print("tx error\n")
                return False
            buf = self._sock.recv(self._N_RCVBUF)

        return self.chkRes(params['cmd'], buf)

    def jntrmove(self, ax1, ax2, ax3, ax4, ax5, ax6, speed, acct, dacct):
        params = {}
        if self._linear_joint_support == True:
            params = {'cmd':RobotClient._JNTRMOVE, 'params':[[float(ax1), \
                                                              float(ax2), \
                                                              float(ax3), \
                                                              float(ax4), \
                                                              float(ax5), \
                                                              float(ax6)], \
                                                             float(speed), \
                                                             float(acct), \
                                                             float(dacct)]}
        else:
            params = {'cmd':RobotClient._JNTRMOVE, 'params':[[math.radians(ax1), \
                                                              math.radians(ax2), \
                                                              math.radians(ax3), \
                                                              math.radians(ax4), \
                                                              math.radians(ax5), \
                                                              math.radians(ax6)], \
                                                             float(speed), \
                                                             float(acct), \
                                                             float(dacct)]}

        with self._lock:
            msg = json.dumps(params).encode('ascii')
            if self._sock.send(msg) <= 0:
                print("tx error\n")
                return False
            buf = self._sock.recv(self._N_RCVBUF)

        return self.chkRes(params['cmd'], buf)

    def jntrmove_wo_chk(self, ax1, ax2, ax3, ax4, ax5, ax6, speed, acct, dacct):
        params = {}
        if self._linear_joint_support == True:
            params = {'cmd':RobotClient._JNTRMOVE_WO_CHK, 'params':[[float(ax1), \
                                                                     float(ax2), \
                                                                     float(ax3), \
                                                                     float(ax4), \
                                                                     float(ax5), \
                                                                     float(ax6)], \
                                                                    float(speed), \
                                                                    float(acct), \
                                                                    float(dacct)]}
        else:
            params = {'cmd':RobotClient._JNTRMOVE_WO_CHK, 'params':[[math.radians(ax1), \
                                                                     math.radians(ax2), \
                                                                     math.radians(ax3), \
                                                                     math.radians(ax4), \
                                                                     math.radians(ax5), \
                                                                     math.radians(ax6)], \
                                                                    float(speed), \
                                                                    float(acct), \
                                                                    float(dacct)]}

        with self._lock:
            msg = json.dumps(params).encode('ascii')
            if self._sock.send(msg) <= 0:
                print("tx error\n")
                return False
            buf = self._sock.recv(self._N_RCVBUF)

        return self.chkRes(params['cmd'], buf)

    def cprmove(self, x, y, z, rz, ry, rx, speed, acct, dacct):
        params = {'cmd':RobotClient._CPRMOVE, 'params':[[x / 1000.0, y / 1000.0, z / 1000.0, math.radians(rz), \
                                                         math.radians(ry), math.radians(rx)], speed / 1000.0, float(acct), float(dacct)]}

        with self._lock:
            msg = json.dumps(params).encode('ascii')
            if self._sock.send(msg) <= 0:
                print("tx error\n")
                return False
            buf = self._sock.recv(self._N_RCVBUF)

        return self.chkRes(params['cmd'], buf)

    def cprplan(self, dx, dy, dz, drz, dry, drx, speed, acct, dacct):
        params = {'cmd':RobotClient._CPRPLAN, 'params':[[dx / 1000.0, \
                                                         dy / 1000.0, \
                                                         dz / 1000.0, \
                                                         math.radians(drz), \
                                                         math.radians(dry), \
                                                         math.radians(drx), \
                                                         ], \
                                                        speed / 1000.0, \
                                                        float(acct), \
                                                        float(dacct)]}

        with self._lock:
            msg = json.dumps(params).encode('ascii')
            if self._sock.send(msg) <= 0:
                print("tx error\n")
                return False
            buf = self._sock.recv(self._N_RCVBUF)

        return self.chkRes(params['cmd'], buf)

    def cprplan_w_sp(self, x, y, z, rz, ry, rx, posture, rbcoord, \
                     dx, dy, dz, drz, dry, drx, speed, acct, dacct):
        params = {'cmd':RobotClient._CPRPLAN_W_SP, 'params':[[x / 1000.0, \
                                                              y / 1000.0, \
                                                              z / 1000.0, \
                                                              math.radians(rz), \
                                                              math.radians(ry), \
                                                              math.radians(rx), \
                                                              int(posture), \
                                                              int(rbcoord), \
                                                              ], \
                                                             [dx/1000.0,\
                                                       dy/1000.0,\
                                                       dz/1000.0,\
                                                       math.radians(drz),\
                                                       math.radians(dry),\
                                                       math.radians(drx)
                                                      ], \
                                                             speed/1000.0, \
                                                             float(acct), \
                                                             float(dacct)]}

        with self._lock:
            msg = json.dumps(params).encode('ascii')
            if self._sock.send(msg) <= 0:
                print("tx error\n")
                return False
            buf = self._sock.recv(self._N_RCVBUF)

        return self.chkRes(params['cmd'], buf)

    def suspendm(self, tmout):
        params = {'cmd':RobotClient._SUSPENDM, 'params':[float(tmout)]}

        with self._lock:
            msg = json.dumps(params).encode('ascii')
            if self._sock.send(msg) <= 0:
                print("tx error\n")
                return False
            buf = self._sock.recv(self._N_RCVBUF)

        return self.chkRes(params['cmd'], buf)

    def resumem(self):
        params = {'cmd':RobotClient._RESUMEM, 'params':[]}

        with self._lock:
            msg = json.dumps(params).encode('ascii')
            if self._sock.send(msg) <= 0:
                print("tx error\n")
                return False
            buf = self._sock.recv(self._N_RCVBUF)

        return self.chkRes(params['cmd'], buf)

    def getmt(self, bx, by, bz, brz, bry, brx, posture, rbcoord, multiturn, str_x, str_y, str_z, str_rz, str_ry, str_rx):
        if (multiturn & 0xFF000000) == 0xFF000000:
            ik_solver_option = 0x00000000

        params = {'cmd':RobotClient._GETMT, 'params':[[bx / 1000.0, by / 1000.0, bz / 1000.0, \
                                                       math.radians(brz), math.radians(bry), math.radians(brx), int(posture), \
                                                       int(rbcoord), int(multiturn)], \
                                                      [str_x, str_y, str_z, str_rz, str_ry, str_rx]]}

        with self._lock:
            msg = json.dumps(params).encode('ascii')
            if self._sock.send(msg) <= 0:
                print("tx error\n")
                return False
            buf = self._sock.recv(self._N_RCVBUF)

        return self.chkRes(params['cmd'], buf)

    def relbrk(self, bitfield):
        params = {'cmd':RobotClient._RELBRK, 'params':[int(bitfield)]}

        with self._lock:
            msg = json.dumps(params).encode('ascii')
            if self._sock.send(msg) <= 0:
                print("tx error\n")
                return False
            buf = self._sock.recv(self._N_RCVBUF)

        return self.chkRes(params['cmd'], buf)

    def clpbrk(self, bitfield):
        params = {'cmd':RobotClient._CLPBRK, 'params':[int(bitfield)]}

        with self._lock:
            msg = json.dumps(params).encode('ascii')
            if self._sock.send(msg) <= 0:
                print("tx error\n")
                return False
            buf = self._sock.recv(self._N_RCVBUF)

        return self.chkRes(params['cmd'], buf)

    def arcmove(self, px, py, pz, prz, pry, prx, pposture, prbcoord,\
                      ex, ey, ez, erz, ery, erx, eposture, erbcoord,\
                      speed, acct, dacct,\
                      orientation):
        params = {'cmd':RobotClient._ARCMOVE, 'params':[\
        [px/1000.0,py/1000.0,pz/1000.0,\
         math.radians(prz),math.radians(pry),math.radians(prx),
         int(pposture),int(prbcoord)],\
        [ex/1000.0,ey/1000.0,ez/1000.0,\
         math.radians(erz),math.radians(ery),math.radians(erx),
         int(eposture),int(erbcoord)],\
        float(speed)/1000.0,float(acct),float(dacct),\
        int(orientation) ]}

        with self._lock:
            msg = json.dumps(params).encode('ascii')
            if self._sock.send(msg) <= 0:
                print("tx error\n")
                return False
            buf = self._sock.recv(self._N_RCVBUF)

        return self.chkRes(params['cmd'], buf)

    def cirmove(self, p1x, p1y, p1z, p1rz, p1ry, p1rx, p1posture, p1rbcoord,\
                      p2x, p2y, p2z, p2rz, p2ry, p2rx, p2posture, p2rbcoord,\
                      speed, acct, dacct,\
                      orientation):
        params = {'cmd':RobotClient._CIRMOVE, 'params':[\
        [p1x/1000.0,p1y/1000.0,p1z/1000.0,\
         math.radians(p1rz),math.radians(p1ry),math.radians(p1rx),
         int(p1posture),int(p1rbcoord)],\
        [p2x/1000.0,p2y/1000.0,p2z/1000.0,\
         math.radians(p2rz),math.radians(p2ry),math.radians(p2rx),
         int(p2posture),int(p2rbcoord)],\
        float(speed)/1000.0,float(acct),float(dacct),\
        int(orientation) ]}

        with self._lock:
            msg = json.dumps(params).encode('ascii')
            if self._sock.send(msg) <= 0:
                print("tx error\n")
                return False
            buf = self._sock.recv(self._N_RCVBUF)

        return self.chkRes(params['cmd'], buf)

    def mmark(self):
        params = {'cmd':RobotClient._MMARK, 'params':[]}

        with self._lock:
            msg = json.dumps(params).encode('ascii')
            if self._sock.send(msg) <= 0:
                print("tx error\n")
                return False
            buf = self._sock.recv(self._N_RCVBUF)

        retlist = self.chkRes(params['cmd'], buf)
        if retlist[0] == True:
            for i in range(6):
                retlist[i] = math.degrees(float(retlist[i]))
        return retlist

    def setvenv(self, venv_type, ts, te):
        params = {'cmd':RobotClient._SETVENV, 'params':[int(venv_type), float(ts), float(te)]}
        print(json.dumps(params))

        with self._lock:
            msg = json.dumps(params).encode('ascii')
            if self._sock.send(msg) <= 0:
                print("tx error\n")
                return False
            buf = self._sock.recv(self._N_RCVBUF)

        return self.chkRes(params['cmd'], buf)


class _ZeusRobot(object):
    """
    ZeusRobot 클래스
    MCS와 통신하여 로봇의 모션 제어 수행

    Methods:
        __init__(self, host="192.168.0.23", port=12345): 클래스 생성자
        __del__(self): 클래스 소멸자
        __initialize(): 로봇 인스턴스 초기화

        [Public]
        show_version_mcs(self): MCS 버전 취득
        show_version_api(self): API 버전 취득
        open(self): 로봇 연결
        close(self): 로봇 연결 종료
        ioctrl(self, wordno, dataL, maskL, dataH, maskH): 컨트롤러 IO 제어
        is_open(self): 로봇 연결 상태 취득
        is_permitted(self): 로봇 제어 권한 획득 여부 취득
        is_moving(self): 로봇 모션 동작 상태 여부 취득
        is_paused(self): 로봇 모션 일시정지 상태 여부 취득
        is_async(self): 비동기 제어 상태 여부 취득
        get_servo_status(self): 서보 모터 상태 취득
        set_servo_off(self): 서보 모터 OFF (브레이크)
        get_system_status(self, type): MCS 비상정지 상태 정보 취득
        async_motion(self, sw): 비동기 제어 (sw=1: 활성화 / sw=2: 비활성화)
        wait_motion(self): 비동기 제어 중 모션 완료 대기
        stop(self): 로봇 모션 중단 (큐에 등록된 로봇 동작 명령 초기화)
        pause(self): 로봇 모션 일시정지
        resume(self): 로봇 모션 재개
        override(self, ovr): MotionParam 의 속도 관련 파라미터 재정의 [%] (1-100, int)
        set_motionparam(self, *args, **kwargs): 로봇 MotionParam 설정 [MotionParam 객체 또는 인자 값]
        get_motionparam(self): 로봇 MotionParam 취득
        clear_motionparam(self): 로봇의 MotionParam 초기화
        set_tooloffset(self, *args, **kwargs): 툴 오프셋 설정
        change_tool(self, tid): 툴 변경 [0-8]
        set_mdo(self, mdoid, portno, value, mode, distance): MDO 설정
        enable_mdo(self, bitfield): MDO 활성화
        disable_mdo(self, bitfield): MDO 비활성화
        get_position(self): 현재 로봇 엔드이펙터 위치 정보를 Position 타입 데이터로 취득
        get_joint(self): 현재 로봇 암 각도 정보를 Position 타입 데이터로 취득
        Joint2Position(self, *jnt): Joint 타입 데이터를 Position 타입으로 변환
        Position2Joint(self, *pos): Position 타입 데이터를 Joint 타입으로 변환
        adjust_mt(self, pos, str_x, str_y, str_z, str_rz, str_ry, str_rx): multiturn 값 조정 (좌표를 문자열로 변환 시의 근접 값)
        set_use_mt(flag): multiturn 사용 여부 플래그

        move(self, *cmd): 로봇 이동 모션 (Joint or PTP)
        home(self): 로봇 Home 위치 이동 모션
        move_line(self, *cmd): 로봇 직선 이동 모션 (Linear)
        move_optline(self, *cmd): 로봇 최적 직선 이동 모션 (Optimized Linear)
        move_rel_tool(self, *args, **kwargs): 로봇 Tool 좌표계 기준 상대이동 모션
        move_rel_jnt(self, *cmd): 로봇 Joint 기준 상대이동 모션
        move_rel_line(self, *cmd): 로봇 Cartesian 좌표계 기준 직선 상대이동 모션 (Linear)
        move_arc: 로봇 원호 모션
        move_circle: 로봇 원 동작

        [Internal]
        __acq_permission(self): 로봇 제어 권한 요청
        __rel_permission(self): 로봇 제어 권한 릴리즈
        __changeMotionParam: MotionParam 변경
        _syssts: MCS 시스템 상태 정보 취득
        __plsmove: 입력된 펄스값으로 Joint 이동 모션
        __mtrmove: 입력된 모터값으로 Joint 상대이동 모션
        _jntmove: move 메서드 내 Joint 모션 wrapper 메서드
        __jntmove: 입력된 Joint 값으로 이동 모션
        _ptpmove: move 메서드 내 PTP 모션 wrapper 메서드
        __ptpmove: 입력된 Cartesian 좌표계 값으로 PTP 이동 모션
        __ptpmove_mt: 입력된 Cartesian 좌표계 값으로 PTP 이동 모션 (multiturn 반영)
        _cpmove: Linear 모션 wrapper 메서드
        __cpmove: 입력된 Cartesian 좌표계 값으로 직선 이동 모션 (등속도)
        _optcpmove: Optimized Linear 모션 wrapper 메서드
        __optcpmove: 입력된 Cartesian 좌표계 값으로 최적 직선 이동 모션 (구간별 최고속도로 이동)
    """

    def __init__(self, host="192.168.0.23", port=12345):
        self._isOpen = False  # 로봇 오픈 상태
        self._isMoving = False  # 로봇 모션 진행 상태
        self._isPause = False  # 로봇 모션 일시 정지 상태
        self._isPermit = False  # 로봇 조작 권한 취득 상태
        self._isError = False  # 로봇 에러 상태
        self._isAsync = False  # 로봇 비동기 제어 모드 상태
        self._isConnected = False  # 이더넷 케이블 연결 상태

        # internal attributes
        self.__ovr = 1.0  # MotionParam Override 비율
        self.__mpdef = _MotionParam().mp2list()  # MotionParam 기본값
        self.__mp = self.__mpdef  # MotionParam
        self.__mpovr = self.__mpdef  # MotionParam (Override 적용)
        self.__first_parameter_update = True  # 모션 파라미터 초기 업데이트 플래그

        self._host = host
        self._port = port

        # 이더넷 연결 상태 확인 소켓 (8001 포트)
        self.s_hb = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s_hb.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.s_hb.connect((self._host, 8001))
        self.s_hb.settimeout(2)
        self._isConnected = True

        # 이더넷 연결 상태 확인 스레드
        self.thread_heartbeat_stop = threading.Event()
        self.th_heartbeat = threading.Thread(target=self.thread_heartbeat)  # TEST용 230619
        self.th_heartbeat.setDaemon(True)  # TEST용 230619
        self.th_heartbeat.start()  # TEST용 230619

        # 로봇 클라이언트
        self.__rblib = RobotClient(self._host, self._port)
        self.__rblib_sys = RobotClient(self._host, self._port)  # Stop, Pause, Resume 제어용 클라이언트
        
        # 공유메모리 API, 서보상태 변수
        self._shm = ZeusShm()
        self.shm_update_counter = -1
        self.shm_wait_counter = 0
        self.servo_status = None
        self.emo_status  = None

        self.__initialize()

    def __initialize(self):
        res = self.open(check_servo=False)
        if res[0] == False:
            raise ZeusRobotException(res[1], res[2], "__initialize")

        # # TEST용 ZC 상태 체크 (ZSP는 ZC 시스템 관리자의 영향을 받지 않으므로 제거할 수 있으면 제거)
        # res = self.ioctrl(130, 0, 0xffffffff, 0, 0xffffffff)
        # if res[0] == False:
        #     raise ZeusRobotException(res[1], res[2], "__initialize")
        # st = (res[1] >> 4) & 0x0F
        # if st >= 10:
        #     raise ZeusRobotException(ERR_ZERO_ROBOT, 2, "__initialize")

        self.close()

    def __del__(self):
        try:
            self.__rblib_sys.abortm()
            self.__rblib_sys.close()
            self.__rblib.rel_permission()
            self.__rblib.close()
        except:
            pass

    # def __del__(self):
    #     try:
    #         self.__rblib_sys.close()
    #         self.__rblib.abortm()
    #         self.__rblib.rel_permission()
    #     except:
    #         pass
    #     self.__rblib.close()

    def thread_heartbeat(self):
        while True:
            if not self.thread_heartbeat_stop.is_set():
                # print("CHECK")
                try:
                    msg = "OK"
                    data = self.s_hb.recv(1024).decode()
                    if data != msg:
                        raise socket.error
                except:
                    self._isConnected = False
                    self.s_hb.close()
                    self.thread_heartbeat_stop.set()
            else:
                try:
                    self.s_hb = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    self.s_hb.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
                    self.s_hb.connect((self._host, 8001))
                    self._isConnected = True
                    self.thread_heartbeat_stop.clear()
                except:
                    pass
            time.sleep(0.1)

    def show_version_mcs(self):
        res = self.__rblib.version()
        if res[0] == False:
            raise ZeusRobotException(res[1], res[2], "show_version_mcs")
        return res

    def show_version_api(self):
        return __version__

    def open(self, check_servo = True, check_zsp = True):
        if check_zsp:
            if not self._check_zsp_ready():
                raise ZeusRobotException(ERR_ZERO_ROBOT, 12, "open")

        if check_servo:
            self._check_svsts()

        if not self._isOpen:
            ret = self.__rblib.open(3)
            if ret:
                time.sleep(1)
                ret = self.__rblib_sys.open(3)
                if ret:
                    self._isOpen = True
                    self.__acq_permission()

                    res = self.__rblib.changetool(0)
                    if res[0] == False:
                        raise ZeusRobotException(res[1], res[2], "open")
                    res = self.__rblib.asyncm(2)
                    if res[0] == False:
                        raise ZeusRobotException(res[1], res[2], "open")
                    self.__rel_permission()
                    return [True]
                else:
                    raise ZeusRobotException(ERR_ZERO_ROBOT, 3, "open")
            else:
                raise ZeusRobotException(ERR_ZERO_ROBOT, 4, "open")
        else:
            self._isOpen = True
            return [True]

    def close(self):
        if self._isOpen:
            try:
                self.__rblib_sys.abortm()
                self.__rblib_sys.close()
                self.__rblib.rel_permission()
                self.__rblib.close()
            except Exception as e:
                raise ZeusRobotException(ERR_ZERO_ROBOT, 5, "close", e)

            self._isOpen = False
            return True
        else:
            try:
                self.__rblib_sys.abortm()
                self.__rblib_sys.close()
                self.__rblib.rel_permission()  # 에러 방지 차원에서 호출
                self.__rblib.close()
            except:
                pass
            return True

    def __acq_permission(self):
        res = self.__rblib.acq_permission()
        if res[0] == False:
            raise ZeusRobotCriticalException(res[1], res[2], "__acq_permission")
        return res

    def __rel_permission(self):
        res = self.__rblib.rel_permission()
        if res[0] == False:
            raise ZeusRobotException(res[1], res[2], "__rel_permission")
        return res

    def ioctrl(self, wordno, dataL, maskL, dataH, maskH):
        res = self.__rblib.ioctrl(wordno, dataL, maskL, dataH, maskH)
        if res[0] == False:
            raise ZeusRobotException(res[1], res[2], "ioctrl")
        return res

    def is_open(self):
        return self._isOpen

    def is_permitted(self):
        return self._isPermit

    def is_moving(self):
        return self._isMoving

    def is_paused(self):
        return self._isPause

    def is_async(self):
        return self._isAsync

    def get_servo_status(self):
        res = self.ioctrl(128, 0, 0xffffffff, 0, 0xffffffff)
        if res[0] == False:
            raise ZeusRobotException(res[1], res[2], "get_servo_status")
        if zeus_common._bitflag(res[1], 1):  # Emergency Stop
            return -1
        if zeus_common._bitflag(res[1], 0):  # Servo ON
            return 1
        return 0  # Servo OFF

    def set_servo_off(self):
        self.__acq_permission()
        res = self.__rblib.svctrl(2)
        self.__rel_permission()
        if res[0] == False:
            raise ZeusRobotException(res[1], res[2], "set_servo_off")
        else:
            return True

    def get_system_status(self, type):
        res = self.__syssts(type)
        if not res[0]:
            raise ZeusRobotException(res[1], res[2], "get_system_status")
        return res

    def async_motion(self, enable):
        res = zeus_common._chkparam(enable, p_type=bool)
        if not res[0]:
            raise ZeusRobotException(ERR_ZERO_ROBOT, 1, "async_motion")

        self.__acq_permission()
        if enable:
            res = self.__rblib.asyncm(1)
        elif not enable:
            res = self.__rblib.asyncm(2)
        self.__rel_permission()
        if not res[0]:
            raise ZeusRobotException(res[1], res[2], "async_motion")
        else:
            if enable:
                self._isAsync = True
            elif not enable:
                self._isAsync = False
            return True

    def wait_motion(self):
        try:
            self._check_svsts()
        except ZeusRobotException as e:
            raise e

        self.__acq_permission()
        res = self.__rblib.joinm()
        self.__rel_permission()
        if res[0] == False:
            raise ZeusRobotException(res[1], res[2], "wait_motion")
        else:
            return True

    def stop(self):
        try:
            self._check_svsts()
        except ZeusRobotException as e:
            raise e

        res = self.__rblib_sys.abortm()
        if res[0] == False:
            raise ZeusRobotException(res[1], res[2], "stop")
        else:
            return True

    def pause(self, timeout):
        try:
            self._check_svsts()
        except ZeusRobotException as e:
            raise e

        res = self.__rblib_sys.suspendm(timeout)
        if res[0] == False:
            raise ZeusRobotException(res[1], res[2], "pause")
        else:
            return True

    def resume(self):
        try:
            self._check_svsts()
        except ZeusRobotException as e:
            raise e
        
        res = self.__rblib_sys.resumem()
        if res[0] == False:
            raise ZeusRobotException(res[1], res[2], "resume")
        else:
            return True

    def override(self, ovr):
        res = zeus_common._chkparam(ovr, p_type=[int, float], min=1, max=100)
        if not res[0]:
            raise ZeusRobotException(ERR_ZERO_ROBOT, 1, "override")

        # __mpovr = [lin_speed, jnt_speed, acctime, dacctime, posture, passm, overlap, zone, pose_speed, ik_solver_option]
        self.__ovr = float(ovr) / 100.
        self.__mpovr = [x * self.__ovr for x in self.__mp[:2]] + \
                       self.__mp[2:8] + [self.__mp[8] * self.__ovr] + [self.__mp[9]]
        return True

    def set_motionparam(self, *args, **kwargs):
        if len(args) == 1 and isinstance(args[0], _MotionParam):
            self.__mpdef = args[0].mp2list()
            res = self.__changeMotionParam(args[0])
            if res[0] == False:
                raise ZeusRobotException(res[1], res[2], "set_motionparam")
            else:
                return True
        else:
            mp = _MotionParam(*args, **kwargs)
            self.__mpdef = mp.mp2list()
            res = self.__changeMotionParam(mp)
            if res[0] == False:
                raise ZeusRobotException(res[1], res[2], "set_motionparam")
            else:
                return True

    def get_motionparam(self):
        try:
            mp = _MotionParam(self.__mp)
        except Exception as e:
            raise ZeusRobotException(ERR_ZERO_ROBOT, 6, "get_motionparam", e)
        return mp

    def clear_motionparam(self):
        try:
            mp = _MotionParam(self.__mp)
            mp.clear()
            self.__mp = mp.mp2list()
        except Exception as e:
            raise ZeusRobotException(ERR_ZERO_ROBOT, 7, "clear_motionparam", e)
        return True

    def set_tooloffset(self, *args, **kwargs):
        p = zeus_common._args([0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                              ['id', 'offx', 'offy', 'offz', 'offrz', 'offry', 'offrx'],
                              [int, float, float, float, float, float, float],
                              *args, **kwargs)
        if p[0] == False:
            raise ZeusRobotException(ERR_ZERO_ROBOT, 1, "set_tooloffset")
        else:
            self.__acq_permission()
            res = self.__rblib.settool(p[1], p[2], p[3], p[4], p[5], p[6], p[7])
            self.__rel_permission()
            if res[0] == False:
                raise ZeusRobotException(res[1], res[2], "set_tooloffset")

            return res

    def change_tool(self, tid):
        res = zeus_common._chkparam(tid, p_type=int, min=0, max=8)
        if res[0] == False:
            raise ZeusRobotException(ERR_ZERO_ROBOT, 1, "change_tool")
        else:
            self.__acq_permission()
            res = self.__rblib.changetool(tid)
            self.__rel_permission()
            if res[0] == False:
                raise ZeusRobotException(res[1], res[2], "change_tool")
        return True

    def set_mdo(self, mdoid, portno, value, mode, distance):
        res = zeus_common._chkparam(mdoid, p_type=int, min=1, max=8)
        if res[0] == False:
            raise ZeusRobotException(ERR_ZERO_ROBOT, 1, "set_mdo")
        res = zeus_common._chkparam(portno, p_type=int, min=0)
        if res[0] == False:
            raise ZeusRobotException(ERR_ZERO_ROBOT, 1, "set_mdo")
        res = zeus_common._chkparam(value, p_type=int, min=0, max=1)
        if res[0] == False:
            raise ZeusRobotException(ERR_ZERO_ROBOT, 1, "set_mdo")
        res = zeus_common._chkparam(mode, p_type=int, min=1, max=2)
        if res[0] == False:
            raise ZeusRobotException(ERR_ZERO_ROBOT, 1, "set_mdo")
        res = zeus_common._chkparam(distance, p_type=[int, float], min=0.0)
        if res[0] == False:
            raise ZeusRobotException(ERR_ZERO_ROBOT, 1, "set_mdo")

        self.__acq_permission()
        res = self.__rblib.set_mdo(mdoid, portno, value, mode, distance)
        self.__rel_permission()
        if res[0] == False:
            raise ZeusRobotException(res[1], res[2], "set_mdo")
        return True

    def enable_mdo(self, bitfield):
        res = zeus_common._chkparam(bitfield, p_type=int, min=0, max=255)
        if res[0] == False:
            raise ZeusRobotException(ERR_ZERO_ROBOT, 1, "enable_mdo")

        self.__acq_permission()
        res = self.__rblib.enable_mdo(bitfield)
        self.__rel_permission()
        if res[0] == False:
            raise ZeusRobotException(res[1], res[2], "enable_mdo")
        return True

    def disable_mdo(self, bitfield):
        res = zeus_common._chkparam(bitfield, p_type=int, min=0, max=255)
        if res[0] == False:
            raise ZeusRobotException(ERR_ZERO_ROBOT, 1, "disable_mdo")

        self.__acq_permission()
        res = self.__rblib.disable_mdo(bitfield)
        self.__rel_permission()
        if res[0] == False:
            raise ZeusRobotException(res[1], res[2], "disable_mdo")
        return True

    def get_position(self):
        res = self.__rblib.mark_mt()
        if res[0] == False:
            raise ZeusRobotException(res[1], res[2], "get_position")
        else:
            return _Position(res[1:7], _BASE, res[7], res[9])

    def get_joint(self):
        res = self.__rblib.jmark()
        if res[0] == False:
            raise ZeusRobotException(res[1], res[2], "get_joint")
        else:
            return _Joint(res[1:7])

    def Joint2Position(self, *jnt):
        v = []
        for m in jnt:
            if isinstance(m, list):
                for c in m:
                    if isinstance(c, _Joint):
                        a = c.jnt2list()
                        b = self.__rblib.j2r_mt(a[0], a[1], a[2], a[3], a[4], a[5], 1)
                        if b[0] == True:
                            v.append(_Position(b[1:7], _BASE, b[7], b[9]))
                        else:
                            raise ZeusRobotException(b[1], b[2], "Joint2Position")
                    else:
                        raise ZeusRobotException(ERR_ZERO_ROBOT, 1, "Joint2Position")
            else:
                if isinstance(m, _Joint):
                    a = m.jnt2list()
                    b = self.__rblib.j2r_mt(a[0], a[1], a[2], a[3], a[4], a[5], 1)
                    if b[0] == True:
                        v.append(_Position(b[1:7], _BASE, b[7], b[9]))
                    else:
                        raise ZeusRobotException(b[1], b[2], "Joint2Position")
                else:
                    raise ZeusRobotException(ERR_ZERO_ROBOT, 1, "Joint2Position")

        if len(v) > 1:
            return v
        else:
            return v[0]

    def Position2Joint(self, *pos):
        _ik_solver_option = self.__mp[9]
        v = []
        for m in pos:
            if isinstance(m, list):
                for c in m:
                    if isinstance(c, _Position):
                        a = c._position(True)
                        b = self.__rblib.r2j_mt(a[0], a[1], a[2], a[3], a[4], a[5], a[7], 1, a[8], _ik_solver_option)
                        if b[0] == True:
                            v.append(_Joint(b[1:7]))
                        else:
                            raise ZeusRobotException(b[1], b[2], "Position2Joint")
                    else:
                        raise ZeusRobotException(ERR_ZERO_ROBOT, 1, "Position2Joint")
            else:
                if isinstance(m, _Position):
                    a = m._position(True)
                    b = self.__rblib.r2j_mt(a[0], a[1], a[2], a[3], a[4], a[5], a[7], 1, a[8], _ik_solver_option)
                    if b[0] == True:
                        v.append(_Joint(b[1:7]))
                    else:
                        raise ZeusRobotException(b[1], b[2], "Position2Joint")
                else:
                    raise ZeusRobotException(ERR_ZERO_ROBOT, 1, "Position2Joint")
        if len(v) > 1:
            return v
        else:
            return v[0]

    def adjust_mt(self, pos, str_x, str_y, str_z, str_rz, str_ry, str_rx):
        b = pos._position(True)
        res = self.__rblib.getmt(b[0], b[1], b[2], b[3], b[4], b[5], b[7], 1, b[8], str_x, str_y, str_z, str_rz, str_ry,
                                 str_rx)
        if res[0] == False:
            raise ZeusRobotException(res[1], res[2], "adjust_mt")
        else:
            return int(res[1])

    def set_use_mt(self, flag):
        global _use_mt
        _use_mt = bool(flag)

    def _check_shm_update_counter(self):
        """ _check_svsts 호출 시 공유 메모리 업데이트가 정상적으로 이루어지고 있는지 업데이트 카운터를 체크

        Raises:
            ZeusRobotException: 공유 메모리 업데이트 실패 예외 발생
        """
        while True:
            tmp_shm_update_counter = int(self._shm.read(0x0008, 1)[0])
            if self.shm_update_counter < tmp_shm_update_counter:
                self.shm_update_counter = tmp_shm_update_counter
                self.shm_wait_counter = 0
                break
            else:
                self.shm_wait_counter += 1
                time.sleep(0.01)
                if self.shm_wait_counter > 20:
                    self.shm_wait_counter = 0
                    raise ZeusRobotException(10, 24, "_check_shm_update_counter")
            
    def _check_svsts(self):
        self._check_shm_update_counter()
        
        self.servo_status = self._shm.read(0x3260, 1) # ON : 4
        self.emo_status = self._shm.read(0x3266, 1) # OFF : 0
        
        if self.emo_status[0] == RobotClient._EMO_ON:
            if self.servo_status[0] == RobotClient._SVSTS_ON:
                raise ZeusRobotException(10, 22, "_check_svsts")  # 실제로 불가능한 케이스
            elif self.servo_status[0] == RobotClient._SVSTS_OFF:
                raise ZeusRobotException(10, 22, "_check_svsts")
        else:  # RobotClient._EMO_OFF
            if self.servo_status[0] == RobotClient._SVSTS_ON:
                pass
            elif self.servo_status[0] == RobotClient._SVSTS_OFF:
                raise ZeusRobotException(10, 23, "_check_svsts")

    def _check_zsp_ready(self):
        """ ZSP의 상태가 Servo_Off_Ready/Ready/Run 상태인지 확인 """
        self._check_shm_update_counter()
        self.system_status = self._shm.read(0x3274, 1)
        if self.system_status[0] == 2 or self.system_status[0] == 3 or self.system_status[0] == 4:
            return True
        else:
            return False

    def move(self, *cmd):
        try:
            self._check_svsts()
        except ZeusRobotException as e:
            raise e

        self.__mp = self.__mpdef[:]
        motion_id = []
        for m in cmd:
            if isinstance(m, list):
                for c in m:
                    if isinstance(c, _Position):
                        res = self._ptpmove(c)
                        if res[0] == False:
                            raise ZeusRobotException(res[1], res[2], "move")
                        else:
                            motion_id.append(res[1])
                    elif isinstance(c, _Joint):
                        res = self._jntmove(c)
                        if res[0] == False:
                            raise ZeusRobotException(res[1], res[2], "move")
                        else:
                            motion_id.append(res[1])
                    elif isinstance(c, _MotionParam):
                        res = self.__changeMotionParam(c)
                        if res[0] == False:
                            raise ZeusRobotException(res[1], res[2], "move")
                        else:
                            motion_id.append(res[1])
                    else:
                        raise ZeusRobotException(ERR_ZERO_ROBOT, 1, "move")
            else:
                if isinstance(m, _Position):
                    res = self._ptpmove(m)
                    if res[0] == False:
                        raise ZeusRobotException(res[1], res[2], "move")
                    else:
                        motion_id.append(res[1])
                elif isinstance(m, _Joint):
                    res = self._jntmove(m)
                    if res[0] == False:
                        raise ZeusRobotException(res[1], res[2], "move")
                    else:
                        motion_id.append(res[1])
                elif isinstance(m, _MotionParam):
                    res = self.__changeMotionParam(m)
                    if res[0] == False:
                        raise ZeusRobotException(res[1], res[2], "move")
                else:
                    raise ZeusRobotException(ERR_ZERO_ROBOT, 1, "move")
        return [True] + motion_id

    def home(self):
        try:
            self._check_svsts()
        except ZeusRobotException as e:
            raise e

        res = self._jntmove(_Joint(0, 0, 0, 0, 0, 0))
        if res[0] == False:
            raise ZeusRobotException(res[1], res[2], "home")
        return res

    def move_line(self, *cmd):
        try:
            self._check_svsts()
        except ZeusRobotException as e:
            raise e

        self.__mp = self.__mpdef[:]
        motion_id = []
        for m in cmd:
            if isinstance(m, list):
                for c in m:
                    if isinstance(c, _Position) or isinstance(c, _Joint):
                        res = self._cpmove(c)
                        if res[0] == False:
                            raise ZeusRobotException(res[1], res[2], "move_line")
                        else:
                            motion_id.append(res[1])
                    elif isinstance(c, _MotionParam):
                        res = self.__changeMotionParam(c)
                        if res[0] == False:
                            raise ZeusRobotException(res[1], res[2], "move_line")
                        else:
                            motion_id.append(res[1])
                    else:
                        raise ZeusRobotException(ERR_ZERO_ROBOT, 1, "move_line")
            else:
                if isinstance(m, _Position) or isinstance(m, _Joint):
                    res = self._cpmove(m)
                    if res[0] == False:
                        raise ZeusRobotException(res[1], res[2], "move_line")
                    else:
                        motion_id.append(res[1])
                elif isinstance(m, _MotionParam):
                    res = self.__chMotion(m)
                    if res[0] == False:
                        raise ZeusRobotException(res[1], res[2], "move_line")
                    else:
                        motion_id.append(res[1])
                else:
                    raise ZeusRobotException(ERR_ZERO_ROBOT, 1, "move_line")
        return [True] + motion_id

    def move_optline(self, *cmd):
        try:
            self._check_svsts()
        except ZeusRobotException as e:
            raise e

        self.__mp = self.__mpdef[:]
        motion_id = []
        for m in cmd:
            if isinstance(m, list):
                for c in m:
                    if isinstance(c, _Position) or isinstance(c, _Joint):
                        res = self._optcpmove(c)
                        if res[0] == False:
                            raise ZeusRobotException(res[1], res[2], "move_optline")
                        else:
                            motion_id.append(res[1])
                    elif isinstance(c, _MotionParam):
                        res = self.__changeMotionParam(c)
                        if res[0] == False:
                            raise ZeusRobotException(res[1], res[2], "move_optline")
                        else:
                            motion_id.append(res[1])
                    else:
                        raise ZeusRobotException(ERR_ZERO_ROBOT, 1, "move_optline")
            else:
                if isinstance(m, _Position) or isinstance(m, _Joint):
                    res = self._optcpmove(m)
                    if res[0] == False:
                        raise ZeusRobotException(res[1], res[2], "move_optline")
                    else:
                        motion_id.append(res[1])
                elif isinstance(m, _MotionParam):
                    res = self.__chMotion(m)
                    if res[0] == False:
                        raise ZeusRobotException(res[1], res[2], "move_optline")
                    else:
                        motion_id.append(res[1])
                else:
                    raise ZeusRobotException(ERR_ZERO_ROBOT, 1, "move_optline")
        return [True] + motion_id

    def move_rel_tool(self, *args, **kwargs):
        try:
            self._check_svsts()
        except ZeusRobotException as e:
            raise e

        p = zeus_common._args([0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                              ['dx', 'dy', 'dz', 'drz', 'dry', 'drx'],
                              [float, float, float, float, float, float],
                              *args, **kwargs)
        if p[0] == False:
            raise ZeusRobotException(ERR_ZERO_ROBOT, 1, "move_rel_tool")
        else:
            _speed = self.__mpovr[0]
            _acct = self.__mpovr[2]
            _dacct = self.__mpovr[3]

            self.__acq_permission()
            res = self.__rblib.trmove(p[1], p[2], p[3], p[4], p[5], p[6], _speed, _acct, _dacct)
            self.__rel_permission()
            if res[0] == False:
                raise ZeusRobotException(res[1], res[2], "move_rel_tool")
            else:
                return res

    def move_rel_jnt(self, *args, **kwargs):
        try:
            self._check_svsts()
        except ZeusRobotException as e:
            raise e

        p = zeus_common._args([0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                              ['dj1', 'dj2', 'dj3', 'dj4', 'dj5', 'dj6'],
                              [float, float, float, float, float, float],
                              *args, **kwargs)
        if p[0] == False:
            raise ZeusRobotException(ERR_ZERO_ROBOT, 1, "move_rel_jnt")
        else:
            _speed = self.__mpovr[1]
            _acct = self.__mpovr[2]
            _dacct = self.__mpovr[3]

            self.__acq_permission()
            res = self.__rblib.jntrmove(p[1], p[2], p[3], p[4], p[5], p[6], _speed, _acct, _dacct)
            self.__rel_permission()
            if res[0] == False:
                raise ZeusRobotException(res[1], res[2], "move_rel_jnt")
            else:
                return res

    def move_rel_line(self, *args, **kwargs):
        try:
            self._check_svsts()
        except ZeusRobotException as e:
            raise e

        p = zeus_common._args([0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                              ['dx', 'dy', 'dz', 'drz', 'dry', 'drx'],
                              [float, float, float, float, float, float],
                              *args, **kwargs)
        if p[0] == False:
            raise ZeusRobotException(ERR_ZERO_ROBOT, 1, "move_rel_line")
        else:
            _speed = self.__mpovr[0]
            _acct = self.__mpovr[2]
            _dacct = self.__mpovr[3]

            self.__acq_permission()
            res = self.__rblib.cprmove(p[1], p[2], p[3], p[4], p[5], p[6], _speed, _acct, _dacct)
            self.__rel_permission()
            if res[0] == False:
                raise ZeusRobotException(res[1], res[2], "move_rel_line")
            else:
                return res

    def move_arc(self, pos1, pos2, orientation):
        try:
            self._check_svsts()
        except ZeusRobotException as e:
            raise e

        if not isinstance(pos1, _Position):
            raise ZeusRobotException(ERR_ZERO_ROBOT, 1, "move_arc")
        if not isinstance(pos2, _Position):
            raise ZeusRobotException(ERR_ZERO_ROBOT, 1, "move_arc")
        res = zeus_common._chkparam(orientation, p_type=int, min=0, max=2)
        if not res[0]:
            raise ZeusRobotException(ERR_ZERO_ROBOT, 1, "move_arc")


        _speed = self.__mpovr[0]
        _acct = self.__mpovr[2]
        _dacct = self.__mpovr[3]

        _cx, _cy, _cz, _crz, _cry, _crx, _, _cps_1 = self.get_position().pos2list()[0:8]
        _x1, _y1, _z1, _rz1, _ry1, _rx1, _, _ps1 = pos1._position()[0:8]
        _x2, _y2, _z2, _rz2, _ry2, _rx2, _, _ps2 = pos2._position()[0:8]
        if _cps_1 != _ps1 or _cps_1 != _ps2:
            raise ZeusRobotException(ERR_ZERO_ROBOT, 8, "move_arc")

        self.__acq_permission()
        res = self.__rblib.arcmove(
            _x1, _y1, _z1, _rz1, _ry1, _rx1, _ps1, 1,
            _x2, _y2, _z2, _rz2, _ry2, _rx2, _ps2, 1,
            _speed, _acct, _dacct, orientation)
        self.__rel_permission()
        if res[0] == False:
            raise ZeusRobotException(res[1], res[2], "move_arc")
        else:
            return res

    def move_circle(self, pos1, pos2, orientation):
        try:
            self._check_svsts()
        except ZeusRobotException as e:
            raise e

        if not isinstance(pos1, _Position):
            raise ZeusRobotException(ERR_ZERO_ROBOT, 1, "move_arc")
        if not isinstance(pos2, _Position):
            raise ZeusRobotException(ERR_ZERO_ROBOT, 1, "move_arc")
        res = zeus_common._chkparam(orientation, p_type=int, min=0, max=1)
        if not res[0]:
            raise ZeusRobotException(ERR_ZERO_ROBOT, 1, "move_arc")

        _speed = self.__mpovr[0]
        _acct = self.__mpovr[2]
        _dacct = self.__mpovr[3]

        _x1, _y1, _z1, _rz1, _ry1, _rx1, _, _ps1 = pos1._position()[0:8]
        _x2, _y2, _z2, _rz2, _ry2, _rx2, _, _ps2 = pos2._position()[0:8]
        self.__acq_permission()
        res = self.__rblib.cirmove(
            _x1, _y1, _z1, _rz1, _ry1, _rx1, _ps1, 1,
            _x2, _y2, _z2, _rz2, _ry2, _rx2, _ps2, 1,
            _speed, _acct, _dacct, orientation)
        self.__rel_permission()
        if res[0] == False:
            raise ZeusRobotException(res[1], res[2], "move_circle")
        else:
            return res

    # Internal Methods
    def __changeMotionParam(self, param):
        if not isinstance(param, _MotionParam):
            raise ZeusRobotException(ERR_ZERO_ROBOT, 1, "__changeMotionParam")
        else:
            # Check parameter update
            new_mp = param.mp2list()

            update_overlap = False
            update_passm = False
            update_zone = False
            update_slspeed = False

            if new_mp[6] != self.__mp[6]:  # Check overlap update
                update_overlap = True
            if new_mp[5] != self.__mp[5]:  # Check passm update
                update_passm = True
            if new_mp[7] != self.__mp[7]:  # Check zone update
                update_zone = True
            if new_mp[8] != self.__mp[8]:  # Check slspeed update
                update_slspeed = True

            if self.__first_parameter_update:
                self.__first_parameter_update = False
                update_overlap = True
                update_passm = True
                update_zone = True
                update_slspeed = True

            self.__mp = new_mp

            if self.__mp[8] < 1.0:
                self.__mp[8] = 1.0

            # __mpovr = [lin_speed, jnt_speed, acctime, dacctime, posture, passm, overlap, zone, pose_speed, ik_solver_option]
            self.__mpovr = [x * self.__ovr for x in self.__mp[:2]] + \
                           self.__mp[2:8] + [self.__mp[8] * self.__ovr] + [self.__mp[9]]
            self.__acq_permission()
            if update_overlap:
                res = self.__rblib.overlap(self.__mp[6])
                if res[0] == False:
                    raise ZeusRobotException(res[1], res[2], "__changeMotionParam")

            if update_passm:
                res = self.__rblib.passm(self.__mp[5])
                if res[0] == False:
                    raise ZeusRobotException(res[1], res[2], "__changeMotionParam")
            if update_zone:
                res = self.__rblib.zone(self.__mp[7])
                if res[0] == False:
                    raise ZeusRobotException(res[1], res[2], "__changeMotionParam")

            if update_slspeed:
                res = self.__rblib.slspeed(self.__mp[8])
                if res[0] == False:
                    raise ZeusRobotException(res[1], res[2], "__changeMotionParam")
            self.__rel_permission()
            return [True]

    def __syssts(self, type):
        return self.__rblib.syssts(type)

    def __plsmove(self, ax1, ax2, ax3, ax4, ax5, ax6, speed, acct, dacct):
        """ Private """
        return self.__rblib.plsmove(ax1, ax2, ax3, ax4, ax5, ax6, speed, acct, dacct)

    def __mtrmove(self, ax1, ax2, ax3, ax4, ax5, ax6, speed, acct, dacct):
        """ Private """
        return self.__rblib.mtrmove(ax1, ax2, ax3, ax4, ax5, ax6, speed, acct, dacct)

    def _jntmove(self, param):
        _ax1, _ax2, _ax3, _ax4, _ax5, _ax6 = param.jnt2list()[0:6]
        _speed = self.__mpovr[1]
        _acct = self.__mpovr[2]
        _dacct = self.__mpovr[3]

        self._isMoving = True
        self.__acq_permission()
        res = self.__jntmove(_ax1, _ax2, _ax3, _ax4, _ax5, _ax6, _speed, _acct, _dacct)
        self.__rel_permission()
        self._isMoving = False
        if res[0] == False:
            raise ZeusRobotException(res[1], res[2], "_jntmove")
        else:
            return res

    def __jntmove(self, ax1, ax2, ax3, ax4, ax5, ax6, speed, acct, dacct):
        return self.__rblib.jntmove(ax1, ax2, ax3, ax4, ax5, ax6, speed, acct, dacct)

    def _ptpmove(self, param):
        _x, _y, _z, _rz, _ry, _rx = param._position()[0:6]
        if param.pos[7] == -1:
            _posture = self.__mpovr[4]
        else:
            _posture = param.pos[7]
        _multiturn = param.pos[8]
        _rbcoord = 1
        _speed = self.__mpovr[1]
        _acct = self.__mpovr[2]
        _dacct = self.__mpovr[3]
        _ik_solver_option = self.__mpovr[9]

        # TBD
        # if self.accel_limit:
        #     _speed = self.convert_accel_ptp(_x, _y, _z, _rz, _ry, _rx, _posture,
        #                                     _rbcoord, _multiturn, _ik_solver_option, _speed, _acct, _dacct)

        self._isMoving = True
        self.__acq_permission()
        if _use_mt:
            res = self.__ptpmove_mt(_x, _y, _z, _rz, _ry, _rx, _posture, _rbcoord, _multiturn, _ik_solver_option,
                                    _speed,
                                    _acct, _dacct)
        else:
            res = self.__ptpmove(_x, _y, _z, _rz, _ry, _rx, _posture, _rbcoord, _speed, _acct, _dacct)
        self.__rel_permission()
        self._isMoving = False

        if res[0] == False:
            raise ZeusRobotException(res[1], res[2], "_ptpmove")
        else:
            return res

    def __ptpmove(self, x, y, z, rz, ry, rx, posture, rbcoord, speed, acct, dacct):
        return self.__rblib.ptpmove(x, y, z, rz, ry, rx, posture, rbcoord, speed, acct, dacct)

    def __ptpmove_mt(self, x, y, z, rz, ry, rx, posture, rbcoord, multiturn, ik_solver_option, speed, acct, dacct):
        return self.__rblib.ptpmove_mt(x, y, z, rz, ry, rx, posture, rbcoord, multiturn, ik_solver_option, speed, acct,
                                       dacct)

    def _cpmove(self, param):
        if isinstance(param, _Position):
            _x, _y, _z, _rz, _ry, _rx = param._position()[0:6]
            if param.pos[7] == -1:
                _posture = self.__mpovr[4]
            else:
                _posture = param.pos[7]
        elif isinstance(param, _Joint):
            p = self.Joint2Position(param).pos
            _x, _y, _z, _rz, _ry, _rx = p[0:6]
            _posture = p[7]
        else:
            raise ZeusRobotException(ERR_ZERO_ROBOT, 1, "_cpmove")

        _rbcoord = 1
        _speed = self.__mpovr[0]
        _acct = self.__mpovr[2]
        _dacct = self.__mpovr[3]

        # TBD
        # if self.accel_limit:
        #     _speed = self.convert_accel_cp(_x, _y, _z, _rz, _ry, _rx, _posture,
        #                                    _rbcoord, _speed, _acct, _dacct)

        self._isMoving = True
        self.__acq_permission()
        res = self.__cpmove(_x, _y, _z, _rz, _ry, _rx, _posture, _rbcoord, _speed, _acct, _dacct)
        self.__rel_permission()
        self._isMoving = False
        if res[0] == False:
            raise ZeusRobotException(res[1], res[2], "_cpmove")
        return res

    def __cpmove(self, x, y, z, rz, ry, rx, posture, rbcoord, speed, acct, dacct):
        return self.__rblib.cpmove(x, y, z, rz, ry, rx, posture, rbcoord, speed, acct, dacct)

    def _optcpmove(self, param):
        if isinstance(param, _Position):
            _x, _y, _z, _rz, _ry, _rx = param._position()[0:6]
            if param.pos[7] == -1:
                _posture = self.__mpovr[4]
            else:
                _posture = param.pos[7]
        elif isinstance(param, _Joint):
            p = self.Joint2Position(param).pos
            _x, _y, _z, _rz, _ry, _rx = p[0:6]
            _posture = p[7]
        else:
            raise ZeusRobotException(ERR_ZERO_ROBOT, 1, "_optcpmove")

        _rbcoord = 1
        _speed = self.__mpovr[1]
        _acct = self.__mpovr[2]
        _dacct = self.__mpovr[3]

        # TBD
        # if self.accel_limit:
        #     _speed = self.convert_accel_optcp(_x, _y, _z, _rz, _ry, _rx, _posture,
        #                                       _rbcoord, _speed, _acct, _dacct)

        self._isMoving = True
        self.__acq_permission()
        res = self.__optcpmove(_x, _y, _z, _rz, _ry, _rx, _posture, _rbcoord, _speed, _acct, _dacct)
        self.__rel_permission()
        self._isMoving = False

        if res[0] == False:
            raise ZeusRobotException(res[1], res[2], "_optcpmove")
        return res

    def __optcpmove(self, x, y, z, rz, ry, rx, posture, rbcoord, speed, acct, dacct):
        u"""Private (非公開)"""
        return self.__rblib.optcpmove(x, y, z, rz, ry, rx, posture, rbcoord, speed, acct, dacct)


class _Base(object):
    """
    Base 클래스
    월드 좌표계를 정의.
    월드 좌표계의 Position, Coordinate 클래스에서 사용하는 더미 클래스

    Methods:
        get_I_matrix(self): 단위 행렬을 반환
        eulerangle(self): 오일러 각([0.0, 0.0, 0.0] 벡터)을 반환

    Example:
        _BASE = _Base()
    """

    def __init__(self):
        self.__I = zeus_common._matI(4)

    def get_I_matrix(self):
        '''
        단위 행렬을 반환
        :return: list
        '''
        return self.__I

    def eulerangle(self):
        '''
        [0.0, 0.0, 0.0] 벡터를 반환
        :return: list
        '''
        return [0.0, 0.0, 0.0]

_BASE = _Base()

class _ParentContainer(object):
    """
    ParentContainer 클래스
    Position, Coordinate 클래스의 부모 클래스

    Attributes:
        pos(list): 좌표계 파라미터 [x, y, z, rz, ry, rx, parent].
                   상속받은 클래스의 self.pos 속성에 초기값으로 적용됨

    Methods:
        matrix(self): pos 값을 행렬 형태로 반환

    """
    pos = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, _BASE]  # 상속받은 클래스의 self.pos 속성에 초기값으로 적용됨

    def __init__(self):
        pass

    def matrix(self):
        m = zeus_common._matEuler(self.pos[3], self.pos[4], self.pos[5])
        m = zeus_common._mdotm(zeus_common._matShift(self.pos[0], self.pos[1], self.pos[2]), m)
        m = zeus_common._mdotm(self.pos[6].get_I_matrix(), m)
        return m


class _Position(_ParentContainer):
    """
    Position 클래스
    직교 좌표계에서의 교시점을 정의

    Attributes:
        pos: 교시점 파라미터 [x, y, z, rz, ry, rx, posture, parent, multiturn]

    Methods:
        __param_position(self, *args, **kwargs): 파라미터 해석
        _position(self): 교시점을 리스트 형식으로 반환
        has_mt(self): multiturn 여부를 반환
        pos2list(self):	교시점을 리스트 형식으로 반환
        pos2dict(self):	교시점을 딕셔너리 형식으로 반환
        copy(self):	Position 객체를 복사하여 반환
        clear(self): 교시점 초기화
        replace(self, *args, **kwargs): 교시점을 치환하여 반환
        offset(self, *args, **kwargs): 교시점 쉬프트 (새로운 객체를 반환)
        shift(self, *args, **kwargs): 교시점 쉬프트 (기존 객체를 갱신하여 반환)

    """
    __defpos = [0., 0., 0., 0., 0., 0., _BASE, -1, 0xFF000000]  # pos 속성의 초기값

    def __init__(self, *args, **kwargs):
        """
        Poistion 객체 생성
        Args:
            x(float): 위치 (월드좌표계 X 좌표)
            y(float): 위치 (월드좌표계 Y 좌표)
            z(float): 위치 (월드좌표계 Z 좌표)
            rz(float): 방향 (Z-Y-X 오일러 각도의 Rz 자세)
            ry(float): 방향 (Z-Y-X 오일러 각도의 Ry 자세)
            rx(float): 방향 (Z-Y-X 오일러 각도의 Rx 자세)
            parent(_Coordinate or _Base): 위치, 방향 데이터를 월드좌표계로 변환하기 위한 변환 행렬
            posture(int): 로봇 암의 자세 (0-7)
            multiturn(int): multiturn 값
        """
        self.pos = _Position.__defpos
        self.__param_position(*args, **kwargs)

    def __param_position(self, *args, **kwargs):
        """
        Position 파라미터 값을 설정하는 내부 메서드
        Args:
            *args : 파라미터 값
            **kwargs : 키를 포함한 파라미터 값

        Returns:
            bool : 실행 여부
        """
        p = zeus_common._args(self.pos,
                              ['x', 'y', 'z', 'rz', 'ry', 'rx', 'parent', 'posture', 'multiturn'],
                              [float, float, float, float, float, float, None, int, int],
                              *args, **kwargs)
        if p[0] == False:
            raise PositionException(ERR_ZERO_POSITION, 1, "__param_position", p[1])
        else:
            self.pos = p[1:]
            if isinstance(self.pos[6], int):
                self.pos[8] = self.pos[7]
                self.pos[7] = self.pos[6]
                self.pos[6] = _Position.__defpos[6]
            _Position.__defpos = self.pos
            return True

    def _position(self, force_use_mt=False):
        """
        부모 좌표계로 변환된 교시점을 리스트 타입으로 반환
        Args:
            force_use_mt: multiturn 사용 강제 옵션

        Returns:
            list : 교시점
        """
        if isinstance(self.pos[6], _Base):
            if _use_mt or force_use_mt:
                return self.pos
            else:
                return self.pos[:8]
        try:
            mp = zeus_common._mdotm(zeus_common._matShift(self.pos[0],
                                                          self.pos[1], self.pos[2]),
                                    zeus_common._matEuler(self.pos[3], self.pos[4], self.pos[5]))
            mw = self.pos[6].matrix()
            m = zeus_common._mdotm(mw, mp)

            if _use_mt or force_use_mt:
                return [m[0][3], m[1][3], m[2][3]] + zeus_common._eulMatrix(m) + [self.pos[6], self.pos[7], self.pos[8]]
            else:  # _not_mt
                return [m[0][3], m[1][3], m[2][3]] + zeus_common._eulMatrix(m) + [self.pos[6], self.pos[7]]
        except Exception as e:
            raise PositionException(ERR_ZERO_POSITION, 2, "_position", e)

    def has_mt(self):
        """
        multiturn 값을 갖는지 여부를 반환
        Returns:
            bool : multitrn 파라미터 여부 반환
        """
        if (self.pos[8] & 0xFF000000) == 0xFF000000:
            return False
        else:
            return True

    def pos2list(self):
        """
        교시점을 리스트 타입으로 반환
        Returns:
            list : 교시점
        """
        if _use_mt:
            return self.pos[:]
        else:
            return self.pos[:8]

    def pos2dict(self):
        """
        교시점을 딕셔너리 타입으로 반환
        Returns:
            dict : 교시점
        """
        if _use_mt:
            k = ['x', 'y', 'z', 'rz', 'ry', 'rx', 'parent', 'posture', 'multiturn']
        else:  # _not_mt
            k = ['x', 'y', 'z', 'rz', 'ry', 'rx', 'parent', 'posture']
        return dict(zip(k, self.pos))

    def copy(self):
        """
        동일한 정보를 가진 Position 객체를 반환
        Returns:
            _Position : 메서드를 호출한 Position 객체의 클론 객체
        """
        return _Position(self.pos[:])

    def clear(self):
        """
        교시점 데이터 초기화 (self.pos, _Position.__defpos)

        Returns:
            None
        """
        self.pos = [0., 0., 0., 0., 0., 0., _BASE, -1, 0xFF000000]
        _Position.__defpos = [0., 0., 0., 0., 0., 0., _BASE, -1, 0xFF000000]

    def replace(self, *args, **kwargs):
        """
        Position 파라미터 성분 변경
        Args:
            *args: 변경 값
            **kwargs: 키를 포함한 변경 값

        Returns:
            _Position : 파라미터 값이 변경된 Position 객체
        """
        self.__param_position(*args, **kwargs)
        return self

    def offset(self, *args, **kwargs):
        """
        좌표 값을 시프트한 새로운 오브젝트를 반환 (인자로 받은 오브젝트는 변경되지 않음)
        Args:
            *args: 시프트 값
            **kwargs: 키를 포함한 시프트 값

        Returns:
            _Position : 값이 시프트 된 새로운 Position 객체
        """
        p = self.copy()
        return p.shift(*args, **kwargs)

    def shift(self, *args, **kwargs):
        """
        오브젝트의 좌표 값을 시프트 (인자로 받은 오브젝트를 갱신하여 반환)
        Args:
            *args: 시프트 값
            **kwargs: 시프트 값

        Returns:
            _Position : 값이 시프트 된 인자로 받은 Position 객체
        """
        p = zeus_common._args([0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                              ['dx', 'dy', 'dz', 'drz', 'dry', 'drx'],
                              [float, float, float, float, float, float],
                              *args, **kwargs)
        if p[0] == False:
            raise PositionException(ERR_ZERO_POSITION, 1, "shift", p[1])
        else:
            self.pos[0:6] = [self.pos[i] + p[i + 1] for i in range(6)]
            return self


class _Joint(object):
    """
    Joint 클래스
    로봇 각 축의 교시점을 정의

    Attributes:
        pos: 교시점 파라미터 [x, y, z, rz, ry, rx, posture, parent, multiturn]

    Methods:
        __param_joint(self, *args, **kwargs): 파라미터 해석
        replace(self, *args, **kwargs): 교시점을 치환하여 반환
        jnt2list(self):	교시점을 리스트 형식으로 반환
        jnt2dict(self):	교시점을 딕셔너리 형식으로 반환
        copy(self):	Joint 객체를 복사하여 반환
        clear(self): 교시점 초기화
        offset(self, *args, **kwargs): 교시점 쉬프트 (새로운 객체 반환)
        shift(self, *args, **kwargs): 교시점 쉬프트 (기존 객체 갱신)
    """
    __defjnt = [0., 0., 0., 0., 0., 0.]  # jnt 속성의 초기값

    def __init__(self, *args, **kwargs):
        """
        Joint 객체 생성
        Args:
            j1(float): J1 각도 [deg]
            j2(float): J2 각도 [deg]
            j3(float): J3 각도 [deg]
            j4(float): J4 각도 [deg]
            j5(float): J5 각도 [deg]
            j6(float): J6 각도 [deg]
        """
        self.jnt = _Joint.__defjnt
        self.__param_joint(*args, **kwargs)

    def __param_joint(self, *args, **kwargs):
        """
        Joint 파라미터 값을 설정하는 내부 메서드
        Args:
            *args : 파라미터 값
            **kwargs : 키를 포함한 파라미터 값

        Returns:
            bool : 실행 여부
        """
        p = zeus_common._args(self.jnt,
                              ['j1', 'j2', 'j3', 'j4', 'j5', 'j6'],
                              [float, float, float, float, float, float],
                              *args, **kwargs)
        if p[0] == False:
            raise JointException(ERR_ZERO_JOINT, 1, "__param_joint", p[1])
        else:
            self.jnt = p[1:]
            _Joint.__defjnt = self.jnt
            return True

    def jnt2list(self):
        """
        교시점을 리스트 타입으로 반환
        Returns:
            list : 교시점
        """
        return self.jnt[:]

    def jnt2dict(self):
        """
        교시점을 딕셔너리 타입으로 반환
        Returns:
            dict : 교시점
        """
        k = ['j1', 'j2', 'j3', 'j4', 'j5', 'j6']
        return dict(zip(k, self.jnt[:]))

    def copy(self):
        """
        동일한 정보를 가진 Position 객체를 반환
        Returns:
            _Position : 메서드를 호출한 Position 객체의 클론 객체
        """
        return _Joint(self.jnt[:])

    def clear(self):
        """
        교시점 데이터 초기화 (self.pos, Position.__defpos)

        Returns:
            None
        """
        self.jnt = [0., 0., 0., 0., 0., 0.]
        _Position.__defjnt = [0., 0., 0., 0., 0., 0.]

    def replace(self, *args, **kwargs):
        """
        Position 파라미터 성분 변경
        Args:
            *args: 변경 값
            **kwargs: 키를 포함한 변경 값

        Returns:
            _Position : 파라미터 값이 변경된 Position 객체
        """
        self.__param_joint(*args, **kwargs)
        return self

    def offset(self, *args, **kwargs):
        """
        좌표 값을 시프트한 새로운 오브젝트를 반환 (인자로 받은 오브젝트는 변경되지 않음)
        Args:
            *args: 시프트 값
            **kwargs: 키를 포함한 시프트 값

        Returns:
            _Position : 값이 시프트 된 새로운 Position 객체
        """
        p = self.copy()
        return p.shift(*args, **kwargs)

    def shift(self, *args, **kwargs):
        """
        오브젝트의 좌표 값을 시프트 (인자로 받은 오브젝트를 갱신하여 반환)
        Args:
            *args: 시프트 값
            **kwargs: 시프트 값

        Returns:
            _Position : 값이 시프트 된 인자로 받은 Position 객체
        """
        p = zeus_common._args([0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                              ['dj1', 'dj2', 'dj3', 'dj4', 'dj5', 'dj6'],
                              [float, float, float, float, float, float],
                              *args, **kwargs)
        if p[0] == False:
            raise JointException(ERR_ZERO_JOINT, 1, "shift", p[1])
        else:
            self.jnt[0:6] = [self.jnt[i] + p[i + 1] for i in range(6)]
            return self


class _Coordinate(_ParentContainer):
    """
    직교 좌표계에 정의된 Coordinate 클래스

    Attributes:
        pos: 좌표계 파라미터 [x, y, z, rz, ry, rx, parent]

    Methods:
        __param_coordinate(self, *args, **kwargs): 파라미터 해석
        coord2list(self): 좌표계를 리스트 타입으로 반환
        coord2dict(self): 좌표계를 딕셔너리 타입으로 반환
        world2base(): 월드좌표계를 베이스좌표계로 변환
        base2world(): 베이스좌표계를 월드좌표계로 변환
        copy(self):	좌표계 객체를 복사하여 반환
        clear(self): 좌표계 초기화
        replace(self, *args, **kwargs): 좌표계를 치환하여 반환
        shift(self, *args, **kwargs): 좌표계 쉬프트 (기존 객체를 갱신하여 반환)
        inv(self): 좌표계를 역변환하여 반환
    """
    __defpos = [0., 0., 0., 0., 0., 0., _BASE, -1, 0xFF000000]  # pos 속성의 초기값

    def __init__(self, *args, **kwargs):
        """
        Coordinate 객체 생성
        Args:
            x(float): 위치 (월드좌표계 X 좌표)
            y(float): 위치 (월드좌표계 Y 좌표)
            z(float): 위치 (월드좌표계 Z 좌표)
            rz(float): 방향 (Z-Y-X 오일러 각도의 Rz 자세)
            ry(float): 방향 (Z-Y-X 오일러 각도의 Ry 자세)
            rx(float): 방향 (Z-Y-X 오일러 각도의 Rx 자세)
            parent(_Coordinate or _Base): 위치, 방향 데이터를 월드좌표계로 변환하기 위한 변환 행렬
        """
        self.pos = _Coordinate.__defpos
        self.__param_coordinate(*args, **kwargs)

    def __param_coordinate(self, *args, **kwargs):
        p = zeus_common._args(self.pos,
                              ['x', 'y', 'z', 'rz', 'ry', 'rx', 'parent'],
                              [float, float, float, float, float, float, None],
                              *args,
                              **kwargs)

        if p[0] == False:
            raise CoordinateException(ERR_ZERO_COORDINATE, 1, "__param_coordinate", p[1])
        else:
            self.pos = p[1:]
            if not isinstance(self.pos[6], _ParentContainer) and not isinstance(self.pos[6], _Base):
                raise CoordinateException(ERR_ZERO_COORDINATE, 2, "__param_coordinate")
            _Coordinate.__defpos = self.pos
            return True

    def coord2list(self):
        return self.pos[:]

    def coord2dict(self):
        k = ['x', 'y', 'z', 'rz', 'ry', 'rx', 'parent']
        return dict(zip(k, self.pos))

    def world2base(self, wx, wy, wz, wrz, wry, wrx):
        try:
            mp = zeus_common._mdotm(zeus_common._matShift(wx, wy, wz), zeus_common._matEuler(wrz, wry, wrx))
            mw = zeus_common._minv(self.matrix())
            m = zeus_common._mdotm(mw, mp)
        except Exception as e:
            raise CoordinateException(ERR_ZERO_COORDINATE, 3, "world2base", e)
        return [m[0][3], m[1][3], m[2][3]] + zeus_common._eulMatrix(m)

    def base2world(self, bx, by, bz, brz, bry, brx):
        try:
            mp = zeus_common._mdotm(zeus_common._matShift(bx, by, bz), zeus_common._matEuler(brz, bry, brx))
            mw = self.matrix()
            m = zeus_common._mdotm(mw, mp)
        except Exception as e:
            raise CoordinateException(ERR_ZERO_COORDINATE, 4, "base2world", e)
        return [m[0][3], m[1][3], m[2][3]] + zeus_common._eulMatrix(m)

    def copy(self):
        p = _Coordinate(self.pos[:])
        return p

    def clear(self):
        self.pos = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, _BASE]
        _Coordinate.__defpos = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, _BASE]

    def replace(self, *args, **kwargs):
        self.__param_coordinate(*args, **kwargs)
        return self

    def shift(self, *args, **kwargs):
        p = zeus_common._args([0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                              ['dx', 'dy', 'dz', 'drz', 'dry', 'drx'],
                              [float, float, float, float, float, float],
                              *args,
                              **kwargs)
        if p[0] == False:
            raise CoordinateException(ERR_ZERO_COORDINATE, 1, "shift", p[1])
        else:
            self.pos[0:6] = [self.pos[i] + p[i + 1] for i in range(6)]
            return self

    def inv(self):
        try:
            m = zeus_common._minv(self.matrix())
            mw = [m[0][3], m[1][3], m[2][3]] + zeus_common._eulMatrix(m)
            p = _Coordinate(mw[0:6], _BASE)
        except Exception as e:
            raise CoordinateException(ERR_ZERO_COORDINATE, 5, "inv")
        return p


class _MotionParam(object):
    """
    MotionParam 클래스
    로봇 모션 파라미터 정의

    Methods:
        __param_mp(self, *args, **kwargs):	파라미터 해석
        __list2mp(self, mp): 리스트로 주어진 모션파라미터를 MotionParameter에 저장
        mp2list(self): 모션파라미터를 리스트 형식으로 반환
        mp2dict(self):	모션파라미터를 딕셔너리 형식으로 반환
        copy(self,*args, **kwargs):	MotionParam 객체를 복사하여 반환
        clear(self): 모션파라미터 초기화
        set_default(self, *args, **kwargs):	모션파라미터 Default 값을 변경
        set_motionparam(self, *args, **kwargs):	파라미터 설정

    """
    __default = [5.0, 5.0, 0.4, 0.4, 2, 2, 0.0, 100, 20.0, 0x11111111]

    def __init__(self, *args, **kwargs):
        """
        MotionParam 객체 생성
        Args:
            lin_speed (float): Linear interpolation을 기반으로 한 Cartesian 좌표계에서의 직선 운동 모션 속도. [mm/s] Default:5.0
            jnt_speed (float): Cartesian 좌표계의 PTP motion, Joint 모션의 속도 비율. [%] Default:5.0
            acctime (float): 최대 속도까지 가속하는 데 소요되는 시간을 설정. [sec] Default:0.4
            dacctime (float): 속도 0까지 감속하는 데 소요되는 시간을 설정. [sec] Default:0.4
            posture (int): 로봇 암의 자세 (0-7). 암의 위치와 Joint 값에 의해 정의됨. Default:2
            passm (int): pass 모션 파라미터. ON인 경우, 연속 모션 사이의 대기 시간을 무시함. (ON:1, OFF:2) Default:2
            overlap (float): overlap 모션 파라미터. asyncm 활성화 상태에서 타겟에 설정된 거리만큼 접근하면 다음 타겟 모션을 겹쳐서 수행하기 시작함. [mm] Default:0.0
            zone (int): 위치 고정(settling) 범위 파라미터. 타겟에 파라미터에 설정한 pulse 이내로 도달한 경우 위치 결정 완료 판정.  [pulse] Default:100
            pose_speed (float): 자세 보간 모션의 속도 비율.[%] Default:20 (100% = 45deg/s)
            ik_solver_option (int): 각 Joint의 회전 방향 플래그 [bitflag] Default:0x11111111
                                    0x11[0~3][0~3][0~3][0~3][0~3][0~3] : J6~J1 설정값
                                    0 : 최단 경로
                                    1 : multiturn 파라미터 설정 값 사용
                                    2 : +방향 회전
                                    3 : -방향 회전
        """
        self.__list2mp(_MotionParam.__default)
        self.__param_mp(*args, **kwargs)

    def __param_mp(self, *args, **kwargs):
        p = zeus_common._args(self.mp2list(),
                              ['lin_speed', 'jnt_speed', 'acctime', 'dacctime', 'posture',
                               'passm', 'overlap', 'zone', 'pose_speed', 'ik_solver_option'],
                              [float, float, float, float, int, int, float, int, float, int],
                              *args, **kwargs)
        if p[0] == False:
            raise MotionParamException(ERR_ZERO_MOTIONPARAM, 1, "__param_mp", p[1])
        else:
            self.__list2mp(p[1:])
            return True

    def __list2mp(self, mp):
        res = zeus_common._chkparam(mp[0], p_type=[int, float], min=0.0)
        if res[0] == False:
            raise MotionParamException(res[1], res[2], "__list2mp")
        else:
            self.lin_speed = mp[0]

        res = zeus_common._chkparam(mp[1], p_type=[int, float], min=0.0, max=100.0)
        if res[0] == False:
            raise MotionParamException(res[1], res[2], "__list2mp")
        else:
            self.jnt_speed = mp[1]

        res = zeus_common._chkparam(mp[2], p_type=[int, float], min=0.0)
        if res[0] == False:
            raise MotionParamException(res[1], res[2], "__list2mp")
        else:
            self.acctime = mp[2]

        res = zeus_common._chkparam(mp[3], p_type=[int, float], min=0.0)
        if res[0] == False:
            raise MotionParamException(res[1], res[2], "__list2mp")
        else:
            self.dacctime = mp[3]

        res = zeus_common._chkparam(mp[4], p_type=int, min=-1, max=7)
        if res[0] == False:
            raise MotionParamException(res[1], res[2], "__list2mp")
        else:
            self.posture = mp[4]

        res = zeus_common._chkparam(mp[5], p_type=int, min=1, max=2)
        if res[0] == False:
            raise MotionParamException(res[1], res[2], "__list2mp")
        else:
            self.passm = mp[5]

        res = zeus_common._chkparam(mp[6], p_type=[int, float], min=0.0)
        if res[0] == False:
            raise MotionParamException(res[1], res[2], "__list2mp")
        else:
            self.overlap = mp[6]

        res = zeus_common._chkparam(mp[7], p_type=int, min=1)
        if res[0] == False:
            raise MotionParamException(res[1], res[2], "__list2mp")
        else:
            self.zone = mp[7]

        res = zeus_common._chkparam(mp[8], p_type=[int, float], min=1.0)
        if res[0] == False:
            raise MotionParamException(res[1], res[2], "__list2mp")
        else:
            self.pose_speed = mp[8]

        res = zeus_common._chkparam(mp[9], p_type=int, min=0)
        if res[0] == False:
            raise MotionParamException(res[1], res[2], "__list2mp")
        else:
            self.ik_solver_option = mp[9]

        return True

    def mp2list(self):
        return [self.lin_speed, self.jnt_speed, self.acctime,
                self.dacctime, self.posture, self.passm, self.overlap, self.zone, self.pose_speed,
                self.ik_solver_option]

    def mp2dict(self):
        k = ['lin_speed', 'jnt_speed', 'acctime', 'dacctime', 'posture',
             'passm', 'overlap', 'zone', 'pose_speed', 'ik_solver_option']
        return dict(zip(k, self.mp2list()))

    def copy(self, *args, **kwargs):
        p = _MotionParam(self.mp2list()[:])
        return p.motionparam(*args, **kwargs)

    def clear(self):
        try:
            self.__list2mp(_MotionParam.__default)
        except Exception as e:
            raise MotionParamException(ERR_ZERO_MOTIONPARAM, 2, "clear", e)

        return True

    def set_default(self, *args, **kwargs):
        p = zeus_common._args(_MotionParam.__default,
                              ['lin_speed', 'jnt_speed', 'acctime', 'dacctime', 'posture',
                               'passm', 'overlap', 'zone', 'pose_speed', 'ik_solver_option'],
                              [float, float, float, float, int, int, float, int, float, int],
                              *args, **kwargs)
        if p[0] == False:
            raise MotionParamException(ERR_ZERO_MOTIONPARAM, 1, p[1])
        else:
            _MotionParam.__default = p[1:]
            return True

    def set_motionparam(self, *args, **kwargs):
        try:
            self.__param_mp(*args, **kwargs)
        except Exception as e:
            raise MotionParamException(ERR_ZERO_MOTIONPARAM, 3, e)

        return True


if __name__ == '__main__':
    try:
        # region 시작
        rb = RobotClient("192.168.0.23", 12345)

        # open
        k = input('\nopen')
        print(rb.open())

        # # _NOP
        # input('\n_NOP')
        # print(rb.nop())
        # endregion

        #region Motion Planning 계열
        # # _PTPPLAN
        # input('\n_PTPPLAN')
        # print(rb.jntmove(0,0,90,0,90,0,50,0.4,0.4))
        # print(rb.ptpplan(110,-370,570,90,0,180,7,-1,50,0.4,0.4))

        # # _CPPLAN
        # input('\n_CPPLAN')
        # print(rb.jntmove(0,0,90,0,90,0,50,0.4,0.4))
        # print(rb.cpplan(130,-370,670,90,0,180,7,-1,50,0.4,0.4))

        # # _PTPPLAN_W_SP
        # input('\n_PTPPLAN_W_SP')
        # print(rb.jntmove(0,0,90,0,90,0,50,0.4,0.4))
        # print(rb.ptpplan_w_sp(90, -370, 570, 90,0,180,7,-1, 110,-370,570,90,0,180,7,-1,50,0.4,0.4))

        # # _CPPLAN_W_SP
        # input('\n_CPPLAN_W_SP')
        # print(rb.jntmove(0,0,90,0,90,0,50,0.4,0.4))
        # print(rb.cpplan_w_sp(120, -370, 570, 90,0,180,7,-1, 130,-370,670,90,0,180,7,-1,50,0.4,0.4))

        # # _OPTCPPLAN
        # input('\n_OPTCPPLAN')
        # print(rb.optcpplan(110,-380,560, 80, 10, 170, 7, -1, 50, 0.4, 0.4))

        # # _PTPPLAN_MT
        # input('\n_PTPPLAN_MT')
        # print(rb.jntmove(0,0,90,0,90,0,50,0.4,0.4))
        # print(rb.ptpplan_mt(110,-370,570,90,0,180,7,-1,0xFF000000, 0x11111111,50,0.4,0.4))

        # # _PTPPLAN_W_SP_MT
        # input('\n_PTPPLAN_W_SP_MT')
        # print(rb.jntmove(0,0,90,0,90,0,50,0.4,0.4))
        # print(rb.ptpplan_w_sp_mt(90, -360, 550, 90,0,180,7,-1,0xFF000000, 0x11111111, 110,-370,570,90,0,180,7,-1,0xFF000000, 0x11111111,50,0.4,0.4))

        # # _CPRPLAN
        # input('\n_CPRPLAN')
        # print(rb.jntmove(0,0,90,0,90,0,50,0.4,0.4))
        # print(rb.cprplan(1,1,1,1,1,1,50,0.4,0.4))

        # # _CPRPLAN_W_SP
        # input('\n_CPRPLAN_W_SP')
        # print(rb.jntmove(0,0,90,0,90,0,50,0.4,0.4))
        # print(rb.cprplan_w_sp(100,-370,570,90,0,180,7,1,1,1,1,1,1,1,50,0.4,0.4))
        #endregion

        # region MOVE 계열
        # _PLSMOVE, _MTRMOVE, _JNTMOVE, _JNTRMOVE, _JNTRMOVE_WO_CHK, _PTPMOVE, _PTPMOVE_MT,
        # _CPMOVE, _CPRMOVE, _OPTCPMOVE, _TRMOVE, _ARCMOVE, _CIRMOVE
        # # _PLSMOVE
        # input('\n_PLSMOVE')
        # print(rb.plsmove(100,100,100,100,100,100,70,0.4,0.4))
        #
        # # _MTRMOVE
        # input('\n_MTRMOVE 1')
        # print(rb.mtrmove(1,1,1,1,1,1,70,0.4,0.4))
        #
        # # _JNTMOVE
        # input('\n_JNTMOVE')
        # print(rb.jntmove(0,0,90,0,90,0,70,0.4,0.4))
        #
        # # _JNTRMOVE
        # input('\n_JNTRMOVE')
        # print(rb.jntmove(0,0,90,0,90,0,50,0.4,0.4))
        # print(rb.jntrmove(1,1,1,1,1,1,50,0.4,0.4))
        #
        # # _JNTRMOVE_WO_CHK
        # input('\n_JNTRMOVE_WO_CHK')
        # print(rb.jntmove(0,0,90,0,90,0,50,0.4,0.4))
        # print(rb.jntrmove_wo_chk(1,1,1,1,1,1,50,0.4,0.4))  # w/o soft limit checking

        # # _PTPMOVE
        # input('\n_PTPMOVE')
        # print(rb.ptpmove(101,-371,571,91,-1,181,7,-1,70,0.4,0.4))
        #
        # # _PTPMOVE_MT
        # input('\n_PTPMOVE_MT')
        # print(rb.jntmove(0,0,90,0,90,0,50,0.4,0.4))
        # print(rb.ptpmove_mt(110,-380,560, 80, 10, 170, 7, -1, 0xFF000000, 0x11111111, 50, 0.4, 0.4))
        #
        # # _CPMOVE
        # input('\n_CPMOVE')
        # print(rb.ptpmove(100,-370,570,90,-1,180,7,-1,70,0.4,0.4))
        #
        # # _CPRMOVE
        # input('\n_CPRMOVE')
        # print(rb.jntmove(0,0,90,0,90,0,50,0.4,0.4))
        # print(rb.cprmove(1,1,1,1,1,1,50,0.4,0.4))
        #
        # # _OPTCPMOVE
        # input('\n_OPTCPMOVE')
        # print(rb.optcpmove(110,-380,560, 80, 10, 170, 7, -1, 50, 0.4, 0.4))
        #
        # # _TRMOVE
        # input('\n_TRMOVE')
        # print(rb.trmove(1,1,1,1,1,1,70,0.4,0.4))
        #
        # # _ARCMOVE # (경유점, 끝점)
        # input('\n_ARCMOVE')
        # print(rb.jntmove(0,0,90,0,90,0,50,0.4,0.4))
        # print(rb.arcmove(200,-420,570,90,0,180,7,-1,300,-370,570,90,0,180,7,1,100,0.4,0.4,0))
        #
        # # _CIRMOVE # 시작점으로부터 두 점을 지나는 원
        # input('\n_CIRMOVE')
        # print(rb.jntmove(0,0,90,0,90,0,50,0.4,0.4))
        # print(rb.cirmove(150,-370,570,90,0,180,7,-1,100,-320,570,90,0,180,7,1,100,0.4,0.4,0))
        # endregion
        # region파라미터 설정, 큐 관리 계열
        # # _SET_TOOL
        # input('\n_SET_TOOL')
        # print(rb.settool(1,1,1,1,1,1,1))
        #
        # # _CHANGE_TOOL
        # input('\n_CHANGE_TOOL 1')
        # print(rb.changetool(1))
        #
        # input('\n_CHANGE_TOOL 0')
        # print(rb.changetool(0))
        #
        # # _ASYNCM
        # input('\n_ASYNCM ON')
        # print(rb.asyncm(1))
        # input('\n_ASYNCM READ')
        # print(rb.asyncm(0))
        #
        # input('\n_ASYNCM OFF')
        # print(rb.asyncm(2))
        # input('\n_ASYNCM READ')
        # print(rb.asyncm(0))
        #
        # # _PASSM
        # input('\n_PASSM ON')
        # print(rb.passm(1))
        # input('\n_PASSM READ')
        # print(rb.passm(0))
        #
        # input('\n_PASSM OFF')
        # print(rb.passm(2))
        # input('\n_PASSM READ')
        # print(rb.passm(0))
        #
        # # _OVERLAP
        # input('\n_OVERLAP')
        # print(rb.overlap(30))
        #
        # # _IOCTRL
        # input('\n_IOCTRL WRITE')
        # print(rb.ioctrl(130, 0x00000000, 0x0000ffff, 0, 0xffffffff))
        #
        # input('\n_IOCTRL READ')
        # print(rb.ioctrl(130, 0, 0xffffffff, 0, 0xffffffff))
        #
        # input('\n_IOCTRL WRITE')
        # print(rb.ioctrl(130, 0xffff0000, 0x0000ffff, 0, 0xffffffff))
        #
        # input('\n_IOCTRL READ')
        # print(rb.ioctrl(130, 0, 0xffffffff, 0, 0xffffffff))
        #
        # # _ZONE
        # input('\n_ZONE')
        # print(rb.zone(100))
        #
        # # _SLSPEED
        # input('\n_SLSPEED')
        # print(rb.slspeed(5))
        # print(rb.jntmove(0,0,90,0,90,0,70,0.4,0.4))
        # ts = time.time()
        # print(rb.cprmove(0,0,0,10,10,10,100,0.4,0.4))
        # print('tact time:', time.time()-ts)
        #
        # print(rb.slspeed(100))
        # print(rb.jntmove(0,0,90,0,90,0,70,0.4,0.4))
        # ts = time.time()
        # print(rb.cprmove(0, 0, 0, 10, 10, 10, 100, 0.4, 0.4))
        # print('tact time:', time.time()-ts)
        #
        # # _ABORTM
        # input('\n_ABORTM')
        # rb.asyncm(1)
        # rb.jntmove(0,0,0,0,0,0,10,0.4,0.4)
        # rb.jntmove(0,0,90,0,90,0,10,0.4,0.4)
        # rb.jntmove(0,0,0,0,0,0,10,0.4,0.4)
        # cnt=0
        # while cnt < 300:
        #     cnt+=1
        #     print('queue:', rb.syssts(5)[1])
        #     time.sleep(0.01)
        # print(rb.abortm())
        # rb.asyncm(2)
        #
        # # _JOINM
        # input('\n_JOINM')
        # rb.asyncm(1)
        # rb.jntmove(0,0,0,0,0,0,10,0.4,0.4)
        # rb.jntmove(0,0,90,0,90,0,10,0.4,0.4)
        # print(rb.joinm())
        # rb.jntmove(0,0,0,0,0,0,10,0.4,0.4)
        # rb.asyncm(2)
        # print()
        #
        # # _SUSPENDM, _RESUMEM : 확인이 어려움
        #input('\n_SUSPENDM')


        
        # # _SET_MDO
        # input('\n_SET_MDO')
        # print(rb.set_mdo(1, 16, 1, 1, 30))
        # print(rb.set_mdo(2, 16, 0, 2, 30))
        # input('\_ENABLE_MDO')
        # print(rb.enable_mdo(3))
        # print(rb.jntmove(0, 0, 0, 0, 0, 0, 10, 0.4, 0.4))
        # print(rb.jntmove(0, 0, 30, 0, 30, 0, 10, 0.4, 0.4))
        # print(rb.jntmove(0, 0, 0, 0, 0, 0, 10, 0.4, 0.4))
        # print(rb.jntmove(0, 0, 30, 0, 30, 0, 10, 0.4, 0.4))
        # input('\n_DISABLE_MDO')
        # print(rb.disable_mdo(3))
        #
        # # _FSCTRL  # PRDEF setting is needed.
        # input('\n_FSCTRL')
        # print(rb.fsctrl(1))
        # print(rb.fsctrl(2))
        # print(rb.fsctrl(3))
        # print(rb.fsctrl(4))
        # print(rb.fsctrl(5))
        # endregion
        # region MARK  계열
        # # _MARK
        # input('\n_MARK')
        # print(rb.mark())
        #
        # # _JMARK
        # input('\n_JMARK')
        # print(rb.jmark())
        #
        # # _PMARK
        # input('\n_PMARK')
        # rb.asyncm(1)
        # rb.jntmove(0,0,0,0,0,0,10,0.4,0.4)
        # rb.jntmove(0,0,90,0,90,0,10,0.4,0.4)
        # rb.jntmove(0,0,0,0,0,0,10,0.4,0.4)
        # while rb.syssts(5)[1] !=0:
        #     print('curpos :', rb.pmark(3))
        #     print('cmd :', rb.pmark(2))
        #     print('fb :', rb.pmark(1))
        #     print('goal:',rb.pmark(4))
        #     time.sleep(0.1)
        # print(rb.abortm())
        # rb.asyncm(2)
        #
        # # _MARK_MT
        # input('\n_MARK_MT')
        # print(rb.mark_mt())
        #
        # # _MMARK  # MCS 버전 업데이트 필요. 모터 값 확인
        # input('\n_MMARK')
        # rb.asyncm(2)
        # print(rb.mmark())
        # endregion
        # region 변환 계열
        # # _J2R
        # input('\n_J2R')
        # print(rb.j2r(0,0,90,0,90,0,-1))
        #
        # # _R2J
        # input('\n_R2J')
        # print(rb.r2j(100,-370,570,90,0,180,3,-1,0xFF000000, 0x11111111))
        # input('\n_R2J')
        # print(rb.r2j(100,-370,570,90,0,180,3,-1,0x00FFFFFF, 0x11111111))
        # input('\n_R2J')
        # print(rb.r2j(100,-370,570,90,0,180,3,-1,0x00FFFFFF, 0x11000000))
        # input('\n_R2J')
        # print(rb.r2j(100,-370,570,90,0,180,3,-1,0x00111111, 0x11111111))
        # input('\n_R2J')
        # print(rb.r2j(100,-370,570,90,0,180,3,-1,0x00111111, 0x11000000))
        #
        # # _J2R_MT
        # input('\n_J2R_MT')
        # print(rb.j2r_mt(0,0,90,0,90,0,-1))
        #
        # # _R2J_MT
        # input('\n_R2J_MT')
        # print(rb.r2j_mt(100,-370,570,90,0,180,3,-1,0xFF000000, 0x11111111))
        # input('\n_R2J')
        # print(rb.r2j_mt(100,-370,570,90,0,180,3,-1,0x00FFFFFF, 0x11111111))
        # input('\n_R2J')
        # print(rb.r2j_mt(100,-370,570,90,0,180,3,-1,0x00FFFFFF, 0x11000000))
        # input('\n_R2J')
        # print(rb.r2j_mt(100,-370,570,90,0,180,3,-1,0x00111111, 0x11111111))
        # input('\n_R2J')
        # print(rb.r2j_mt(100,-370,570,90,0,180,3,-1,0x00111111, 0x11000000))
        # endregion
        # region 시스템 설정, 모니터링 계열
        # # _VERSION
        # input('\n_VERSION')
        # print(rb.version())
        #
        # # _ENCRST  # Encoder Reset (enc_reset.py에서 호출됨) can't execute on simulation
        # input('\n_ENCRST')
        # print(rb.encrst(63))
        #
        # # _SAVEPARAMS  # HWDEF 파일 갱신(?) # can't execute on simulation
        # input('\n_SAVEPARAMS')
        # print(rb.saveparams())
        #
        # # _CALCPLSOFFSET
        # rb.jntmove(0, 0, 90, 0, 90, 0, 10, 0.4, 0.4)
        # input('\n_CALCPLSOFFSET 1')
        # print(rb.calcplsoffset(1,63))
        # input('\n_CALCPLSOFFSET 2')
        # print(rb.calcplsoffset(2, 63))
        # input('\n_CALCPLSOFFSET 3')
        # print(rb.calcplsoffset(3, 63))
        # input('\n_CALCPLSOFFSET 4')
        # print(rb.calcplsoffset(4, 63))
        # input('\n_CALCPLSOFFSET 5')
        # print(rb.calcplsoffset(5, 63))
        # input('\n_CALCPLSOFFSET 6')
        # print(rb.calcplsoffset(6, 63))  # can't execute on simulation
        #
        # # _SET_LOG_LEVEL
        # input('\n_SET_LOG_LEVEL -1')
        # print(rb.set_log_level(-1))
        # input('\n_SET_LOG_LEVEL 4')
        # print(rb.set_log_level(4))
        # input('\n_SET_LOG_LEVEL 3')
        # print(rb.set_log_level(3))
        # input('\n_SET_LOG_LEVEL 2')
        # print(rb.set_log_level(2))
        # input('\n_SET_LOG_LEVEL 1')
        # print(rb.set_log_level(1))
        # input('\n_SET_LOG_LEVEL 0')
        # print(rb.set_log_level(0))
        #
        # # _SYSCTRL
        # input('\n_SYSCTRL 1 0')
        # print(rb.sysctrl(1, 0))
        # input('\n_SYSCTRL 1 1')
        # print(rb.sysctrl(1, 1))
        # input('\n_SYSCTRL 0x8000 0xdead')
        # print(rb.sysctrl(0x8000, 0xdead))
        # input('\n_SYSCTRL 0x8000 0xeeee')
        # print(rb.sysctrl(0x8000, 0xeeee))
        # input('\n_SYSCTRL 0x8000 0x8001')
        # print(rb.sysctrl(0x8000, 0x8001))
        #
        # # _GETMT  # Need to check how to use
        # input('\n_GETMT')
        # print(rb.getmt())
        #
        # # _SVSW
        # input('\n_SVSW off')
        # print(rb.svctrl(2))
        # input('\n_SVSW on')
        # print(rb.svctrl(1))
        # input('\n_SVSW off')
        # print(rb.svctrl(2))
        #
        # # _RELBRK  # can't execute on simulation
        # input('\n_RELBRK')
        # print(rb.relbrk(0x111111))
        #
        # # _CLPBRK  # can't execute on simulation. 강제 브레이크
        # input('\n_CLPBRK')
        # print(rb.clpbrk(0x111111))
        #
        # # _SYSSTS
        # input('\n_SYSSTS 0')
        # print(rb.syssts(0)[1])
        # input('\n_SYSSTS 1')
        # print(rb.syssts(1))
        # input('\n_SYSSTS 2')
        # print(rb.syssts(2))
        # input('\n_SYSSTS 3')
        # print(rb.syssts(3))
        # input('\n_SYSSTS 4')
        # print(rb.syssts(4))
        # input('\n_SYSSTS 5')
        # print(rb.syssts(5))
        # input('\n_SYSSTS 6')
        # print(rb.syssts(6))
        # input('\n_SYSSTS 7')
        # print(rb.syssts(7))
        # input('\n_SYSSTS 8')
        # print(rb.syssts(8))
        #
        # # _SETVENV
        # input('\n_SETVENV')
        # print(rb.setvenv())
        #
        # endregion

        # region 종료
        k = input('\nclose')
        res = rb.close()
        print(res)
        # endregion

    except Exception as e:
        print(e)
        try:
            rb.close()
        except Exception:
            pass