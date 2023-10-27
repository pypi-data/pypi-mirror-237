"""
API 공용 메소드 라이브러리
"""
import math
import socket
import threading
import json
import os
import getpass
import sys
import builtins
import inspect
import datetime
from numpy import binary_repr

from .zeus_error import *

# # for module check
# from zeus_error import *

# region print문 오버로딩
def print(*args, **kwargs):
    try:
        # print to file
        frm = inspect.stack()[-1]  # 최상위 호출자의 프레임 정보를 가져옴
        mod = inspect.getmodule(frm[0])  # 모듈 정보를 가져옴
        filename = inspect.getsourcefile(mod).split('/')[-1]  # 모듈의 소스 파일명을 가져옴
        username = getpass.getuser()  # 사용자 계정명을 가져옴
        log_path = os.path.join("C:/Users/",username,"/AppData/Local/Zero Software Platform/Logs/userProgram/")
        if not os.path.exists(log_path):
            os.makedirs(log_path)
        logname = log_path + filename + '_output.txt'  # C:/Users/{username}/AppData/Local/Zero Software Platform/Logs/userProgram 폴더에 로그 파일 생성
        with open(logname, 'a', encoding='utf-8') as fout:
            current_time = datetime.datetime.now().strftime("[%Y/%m/%d %H:%M:%S]")
            if "ZeusRobot" in str(frm[-2]):
                # ZeusRobot import 시 호출된 print 문에 대한 별도 처리 필요한 경우 아래에 추가
                pass
            builtins.print(current_time, end=' ', file=fout)  # 타임 스탬프 기록
            builtins.print(*args, **kwargs, file=fout)
    except:
        pass
    finally:
        # orginal print
        builtins.print(*args, **kwargs)
# endregion

# region Matrix, Vector 연산
def _matI(_n):
    """
    단위 행렬 생성
    Args:
        _n (int): 단위 행렬의 차수

    Returns:
        list : nxn 단위 행렬
    """
    return [[1.0 if i == j else 0.0 for j in range(_n)] for i in range(_n)]

def _matEuler(rz, ry, rx):
    """
    ZYX-오일러 변환 행렬을 계산
    Args:
        rz: Roll
        ry: Pitch
        rx: Yaw

    Returns:
        list : 4x4 오일러 변환 행렬
    """
    cz = math.cos(math.radians(rz))
    sz = math.sin(math.radians(rz))
    cy = math.cos(math.radians(ry))
    sy = math.sin(math.radians(ry))
    cx = math.cos(math.radians(rx))
    sx = math.sin(math.radians(rx))

    return [[cy * cz, sx * sy * cz - cx * sz, sx * sz + cx * sy * cz, 0.],
            [cy * sz, sx * sy * sz + cx * cz, cx * sy * sz - sx * cz, 0.],
            [-sy, sx * cy, cx * cy, 0.],
            [0., 0., 0., 1.]]

def _minv(_m):
    """
    역행렬 계산
    Args:
        _m (list): nxn 정방 행렬

    Returns:
        list : 행렬 연산 결과
    """
    n = len(_m)  # 행렬의 차원
    for i in range(n):  # 행렬 크기 확인 (nxn)
        if not len(_m[i]) == n:
            raise Exception("matrix error")
    m = [[float(_m[i][j]) for j in range(n)] + [1.0 if j == i else 0.0 for j in range(n)] \
         for i in range(n)]
    # pivot 선택 (대각에 위치한 원소)
    for i in range(n):
        t = [abs(m[k][i]) for k in range(i, n)]
        m[i], m[t.index(max(t)) + i] = m[t.index(max(t)) + i], m[i]
        m[i] = [m[i][k] / m[i][i] for k in range(2 * n)]
        for j in range(i + 1, n):
            m[j] = [m[j][k] - m[i][k] * m[j][i] for k in range(2 * n)]
    for i in reversed(range(n)):
        for j in range(0, i):
            m[j] = [m[j][k] - m[i][k] * m[j][i] for k in range(2 * n)]
    return _mslice(m, 0, n, n, 2 * n)

def _mdotm(_m1, _m2):
    """
    두 행렬의 내적 연산 (dot product)
    Args:
        _m1 (list): nxm 행렬
        _m2 (list): mxl 행렬

    Returns:
        list : nxl 행렬

    """
    return [[_vdotv(_m1[r], [_m2[i][c] for i in range(len(_m2))])
             for c in range(len(_m2[0]))] for r in range(len(_m1))]

def _mdotv(_m, _v):
    """
    행렬과 벡터의 내적 연산 (dot product)
    Args:
        _m (list): nxm 행렬
        _v (list): mx1 벡터

    Returns:
        list : nx1 행렬(벡터)
    """
    return [_vdotv(_m[r], _v) for r in range(len(_m))]

def _vdotv(_a, _b):
    """
    벡터와 벡터의 내적 연산 (dot product)
    Args:
        _a (list): nx1 벡터
        _b (list): nx1 벡터

    Returns:
        float : 내적 연산 결과 값
    """
    k = 0.0
    for i in range(len(_a)):
        k += _a[i] * _b[i]
    return k

def _vcrossv(_a, _b):
    """
    벡터와 벡터의 외적 연산 (cross product)
    Args:
        _a (list): 3x1 벡터
        _b (list): 3x1 벡터

    Returns:
        list : 외적 연산 결과 행렬
    """
    return [_a[1] * _b[2] - _a[2] * _b[1],
            _a[2] * _b[0] - _a[0] * _b[2],
            _a[0] * _b[1] - _a[1] * _b[0]]

def _vabs(v):
    """
    벡터의 크기 계산
    Args:
        v (list): 3x1 벡터

    Returns:
        float : 벡터의 크기
    """
    return math.sqrt(v[0] ** 2 + v[1] ** 2 + v[2] ** 2)

def _vnorm(v):
    """
    단위 벡터 취득
    Args:
        v (list): 3x1 벡터

    Returns:
        list : 단위 벡터
    """
    a = _vabs(v)
    return [v[0] / a, v[1] / a, v[2] / a]

def _vadd(v1, v2):
    """
    벡터의 합을 계산
    Args:
        v1 (list): [v1,v2,v3] 벡터
        v2 (list): [v1,v2,v3] 벡터

    Returns:
        list : 벡터 연산 결과
    """
    return [v1[k] + v2[k] for k in range(len(v1))]

def _vsub(v1, v2):
    """
    벡터의 차이를 계산
    Args:
        v1 (list): [v1,v2,v3] 벡터
        v2 (list): [v1,v2,v3] 벡터

    Returns:
        list : 벡터 연산 결과
    """
    return [v1[k] - v2[k] for k in range(len(v1))]

def _mslice(_m, _r0, _r1, _c0, _c1):
    """
    행렬을 분리
    Args:
        _m: 분리하고자 하는 행렬
        _r0 (int): 시작 행
        _r1 (int): 끝 행
        _c0 (int): 시작 열
        _c1 (int): 끝 열

    Returns:
        list : 지정된 범위의 행렬 요소를 반환
    """
    return [k[_c0:_c1] for k in _m[_r0:_r1]]

def _eulMatrix(m):
    """
    Affine 변환에서의 오일러 각
    Args:
        m (list): 행렬

    Returns:
        list : 오일러 각 3x1 행렬
    """
    M_PI = 3.1415926535897
    M_PI_2 = M_PI / 2.

    ry = math.asin(-m[2][0])
    if math.fabs(ry - M_PI_2) < 0.0000001:
        rz = math.atan2(m[1][1], m[0][1]) - M_PI_2
        ry = M_PI_2
        rx = 0.0
    elif math.fabs(ry + M_PI_2) < 0.0000001:
        rz = math.atan2(m[1][1], m[0][1]) - M_PI_2
        ry = -M_PI_2
        rx = 0.0
    else:
        rz = math.atan2(m[1][0], m[0][0])
        rx = math.atan2(m[2][1], m[2][2])

    return [math.degrees(rz), math.degrees(ry), math.degrees(rx)]

def _matShift(_x, _y, _z):
    """
    평행 이동 Affine 변환 행렬 생성
    Args:
        _x (float): 평행이동 x값
        _y (float): 평행이동 y값
        _z (float): 평행이동 z값

    Returns:
        list : 평행이동 Affine 변환 행렬
    """
    return [
        [1., 0., 0., _x],
        [0., 1., 0., _y],
        [0., 0., 1., _z],
        [0., 0., 0., 1.]
    ]

def _matRotate(n, o, a):
    """
    3개의 벡터에 대한 회전 변환 행렬 생성
    Args:
        n (list): 변환된 강체 좌표계 x축 방향 벡터 (3x1) [n_x, n_y, n_z]
        o (list): 변환된 강체 좌표계 y축 방향 벡터 (3x1) [o_x, o_y, o_z]
        a (list): 변환된 강체 좌표계 z축 방향 벡터 (3x1) [a_x, a_y, a_z]

    Returns:
        list : 회전 변환 행렬
    """
    return [
        [n[0], o[0], a[0], 0],
        [n[1], o[1], a[1], 0],
        [n[2], o[2], a[2], 0],
        [0, 0, 0, 1]
    ]
# endregion

# region Bitflag, Argument, Parameter
def _bitflag(val, bit):
    """
    val을 이진수료 표현하고, bit에 해당하는 자리를 읽음
    Args:
        val (int): 10진수
        bit (int): 반환하고자 하는 비트 자리 수

    Returns:
        bool : 0이면 False, 1이면 True
    """
    if type(bit) != int:
      raise Exception("Error : zeus_common._bitflag : Invalid Parameter")

    return bool((val & (1 << bit)))

def _args(val, key, typ, *args, **kwargs):
    """ 
    Argument 설정
    Args:
        val (list): Argument 데이터 형태
        key (list): Key 값
        typ (list): 데이터 타입
        *args: 리스트 형태의 설정 값
        **kwargs: 딕셔너리 형태의 설정 값

    Returns:
        list : 설정된 Argument 리스트 반환
    """
    _v = dict(zip(key, val))
    _t = dict(zip(key, typ))
    i = 0

    def sub(v, k):
        if _t[k] == int:
            if type(v) != int:
                raise ValueError
            _v[k] = int(v)
        elif _t[k] == float:
            _v[k] = float(v)
        elif _t[k] == str:
            _v[k] = str(v)
        elif _t[k] == list:
            res = False
            for k in _t[k]:
                res = res or (type(v) == k)
        elif _t[k] == None:
            _v[k] = v
        else:
            if type(v) == _t[k]:
                _v[k] = v
            else:
                raise ValueError

    try:
        for a in args:
            if type(a) == list:
                for b in a:
                    if i < len(key):
                        sub(b, key[i])
                    i += 1
            else:
                if i < len(key):
                    sub(a, key[i])
                i += 1

        for k, v in kwargs.items():
            sub(v, k)
    except Exception as e:
        return [False, f"Error : zeus_common._args : {e}"]
    else:
        return [True] + [_v[j] for j in key]

def _chkparam(pram, **criteria):
    """
    파라미터의 타입 일치 여부 확인
    Args:
        pram: 확인하고자 하는 파라미터 변수
        **criteria: p_type(파라미터 타입), min(최소값), max(최대값)

    Returns:
        bool: 파라미터 타입 일치 여부
    """
    if "p_type" in criteria:
        t = criteria["p_type"]
        res = False
        if isinstance(t,list):
            for k in t:
                res = res or isinstance(pram,k)
        elif isinstance(t, type):
            res = (type(pram) == criteria["p_type"])
        if res == False:
            return [False, 1]

    if isinstance(pram,int) or isinstance(pram,float):
        if "min" in criteria:
            if pram < criteria["min"]:
                return [False, 2]

        if "max" in criteria:
            if pram > criteria["max"]:
                return [False, 2]
    return [True]
# endregion


class _SharedMemory(object):
    """
    SharedMemory 클래스
    공유 메모리 읽기/쓰기 기능 수행

    Methods:
        open(self): 공유메모리 통신을 위한 소켓 연결
        close(self): 공유메모리 통신을 위한 소켓 연결 종료
        shm_read(self, addr, num): 공유메모리의 특정 주소 데이터 취득
        shm_write(self, addr, num): 공유메모리의 유저 영역 주소에 데이터 기록
        shm_system_write(self, addr, num): 공유메모리의 시스템 영역 주소에 데이터 기록
    """
    _CHECK = 0
    _SHM_READ = 1
    _SHM_WRITE = 2
    _SHM_SYSTEM_WRITE = 3

    # _SHM_SYSTEM_WRITE Address
    _SYSINFO_ADDR1 = 0x0800
    _SYSINFO_ADDR2 = 0x0844

    def __init__(self, host = "192.168.0.23", port = 8000):
        self._host = host
        self._port = port
        self._sock = None
        self._lock = threading.Lock()

    def open(self):
        try:
            if self._sock is None:
                self._sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                self._sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
                self._sock.settimeout(1)
                self._sock.connect((self._host, self._port))
                self._sock.ioctl(socket.SIO_KEEPALIVE_VALS, (1, 10000, 3000))
        except Exception as e:
            raise SharedMemoryException(ERR_ZERO_SHM, 3, "open", e)

        return True

    def close(self):
        try:
            if self._sock is not None:
                self._sock.close()
                self._sock = None
        except Exception as e:
            raise SharedMemoryException(ERR_ZERO_SHM, 4,"close", e)

        return True

    def shm_read(self, addr, num):
        """
        Shared Memory 의 데이터를 읽음
        Args:
            addr(int): Shared Memory의 index (0x0100-0x3800)
            num(int, list[int]): addr 부터 읽고자 하는 데이터 개수 (int)

        Returns:
            str : comma로 구분된 string
        """
        res = _chkparam(addr, p_type=int, min=0x0100, max=0x3800)
        if res[0] == False:
            raise SharedMemoryException(ERR_ZERO_SHM, 2,"shm_read")

        res = _chkparam(num, p_type=int, max=256)
        if res[0] == False:
            raise SharedMemoryException(ERR_ZERO_SHM, 1,"shm_read")

        params = {'cmd': self._SHM_READ, 'params': [int(addr), int(num)]}

        try:
            self._lock.acquire()
            self._sock.send(json.dumps(params).encode('ascii'))
            buf = self._sock.recv(1024).decode().split(',')
            self._lock.release()
        except Exception as e:
            raise SharedMemoryException(ERR_ZERO_SHM, 5, "shm_read", e)

        if buf[1] == "":
            raise SharedMemoryException(ERR_ZERO_SHM, 2, "shm_read", f"Cannot Read from Address 0x{format(addr, '04x')}")

        return buf

    def shm_write(self, addr, num):
        """
        Shared Memory 에 데이터 쓰기
        Args:
            addr(int): Shared Memory의 index (0x1800-0x23F8)
                        0x1800-0x1BFC : 4-byte integer 데이터 저장 메모리 영역 (0x1800, 0x1804, 0x1808 ...)
                        0x1C00-0x23F8 : 8-byte float 데이터 저장 메모리 영역 (0x1C00, 0x1C08, 0x1C10 ...
                        (0x2400-0x2800은 Reserved Area로, 사용 제한)
            num(int or float, list[int or float]): addr에 쓰고자 하는 데이터 (int/float 혹은 이를 원소로 갖는 list 또는 tuple)

        Returns:

        """
        res = _chkparam(addr, p_type=int, min=0x1800, max=0x1BFC)
        if res[0] == True:  # int 범위에 해당하는 경우
            if addr % 4 != 0:
                raise SharedMemoryException(ERR_ZERO_SHM, 2, "shm_write")

            res = _chkparam(num, p_type=list)  # 리스트인지 체크
            if res[0] == True:  # 리스트이면
                if len(num) > 256:  # 리스트 길이 체크
                    raise SharedMemoryException(ERR_ZERO_SHM, 1, "shm_write", "limit of list length is 256")
                for i in range(len(num)):  # 리스트 길이 만큼 체크 반복
                    res = _chkparam(num[i], p_type=int)
                    if res[0] == False:
                        raise SharedMemoryException(ERR_ZERO_SHM, 1, "shm_write")
            else:  # 리스트가 아니면
                res = _chkparam(num, p_type=int)
                if res[0] == False:
                    raise SharedMemoryException(ERR_ZERO_SHM, 1, "shm_write", "limit of list length is 256")
        else:
            res = _chkparam(addr, p_type=int, min=0x1C00, max=0x23F8)
            if res[0] == True:  # float 범위에 해당하는 경우
                if addr % 8 != 0:
                    raise SharedMemoryException(ERR_ZERO_SHM, 2, "shm_write")

                res = _chkparam(num, p_type=list)  # 리스트인지 체크
                if res[0] == True:  # 리스트이면
                    if len(num) > 256:  # 리스트 길이 체크
                        raise SharedMemoryException(ERR_ZERO_SHM, 1, "shm_write", "limit of list length is 256")
                    for i in range(len(num)):  # 리스트 길이 만큼 체크 반복
                        res = _chkparam(num[i], p_type=[int,float])
                        if res[0] == False:
                            raise SharedMemoryException(ERR_ZERO_SHM, 1, "shm_write")

                else:  # 리스트가 아니면
                    res = _chkparam(num, p_type=[int,float])
                    if res[0] == False:
                        raise SharedMemoryException(ERR_ZERO_SHM, 1, "shm_write")
            else:
                res = _chkparam(addr, p_type=int, min=0x2400, max=0x27FC)
                if res[0] == True:
                    raise SharedMemoryException(ERR_ZERO_SHM, 2, "shm_write", "Reserved Area")
                else:
                    raise SharedMemoryException(ERR_ZERO_SHM, 1, "shm_write")

        params = {'cmd': self._SHM_WRITE, 'params': [int(addr), num]}

        try:
            self._lock.acquire()
            self._sock.send(json.dumps(params).encode('ascii'))
            buf = self._sock.recv(1024).decode()
            self._lock.release()
        except Exception as e:
            raise SharedMemoryException(ERR_ZERO_SHM, 6, "shm_write", e)

        return buf

    def shm_system_write(self, addr, num):
        """
        시스템 메모리 Write (System 관리 용도. 사용 금지)
        Args:
            addr(int):  _SYSINFO_ADDR1 : 0x0800
                        _SYSINFO_ADDR2 : 0x0844
            num(list): _SYSINFO_ADDR1 인 경우, [prog_name_default, prog_name, prog_pid] [str, str, int]
                       _SYSINFO_ADDR2 인 경우,  [run, stop, err_reset, pause, running, svon,
                                                emo, hw_error, sw_error, abs_lost, in_pause, error] (총 12개, int 타입)

        Returns:

        """

        if not (addr == self._SYSINFO_ADDR1 or addr == self._SYSINFO_ADDR2):
            raise SharedMemoryException(ERR_ZERO_SHM, 2, "shm_system_write",
                                        f"Error : _SharedMemory.shm_read : Cannot Write on Address 0x{format(addr, '04x')}"
                                        f"\nAccessable Address : 0x{format(self._SYSINFO_ADDR1, '04x')}(_SYSINFO_ADDR1) "
                                        f"/ 0x{format(self._SYSINFO_ADDR2, '04x')}(_SYSINFO_ADDR2)"
                                        )

        params = {'cmd': self._SHM_SYSTEM_WRITE, 'params': [int(addr), num]}

        try:
            self._lock.acquire()
            self._sock.send(json.dumps(params).encode('ascii'))
            buf = self._sock.recv(1024).decode()
            self._lock.release()
        except Exception as e:
            raise SharedMemoryException(ERR_ZERO_SHM, 6, "shm_system_write", e)

        return buf


if __name__ == "__main__":
    shm = _SharedMemory()
    shm.open()
    try:
        r = shm.shm_system_write(0x0101,1)
    except Exception as e:
        print(e)
    shm.close()

    # while True:
    #     input("close")
    #     shm.close()
    #     input("open")
    #     shm.open()
    #     shm.shm_write(0x1800, 0)
    #     time.sleep(0.01)
    #     shm.shm_read(0x1800,6)
    #     time.sleep(0.01)
    #     shm.shm_write(0x1800, [1,6])
    #     time.sleep(0.01)
    #     shm.shm_read(0x1800,6)

    # print(shm.shm_read(0x0120, 8))
    # time.sleep(0.5)
    # print(shm.shm_write(0x1C00, 100000.123456))
    # time.sleep(0.5)
    # ret=shm.shm_read(0x1C00, 1)
    # print(ret, type(ret))
    # time.sleep(0.5)
    #
    # print(shm.shm_write(0x1C01, 100000.123456))
    # time.sleep(0.5)
    # print(shm.shm_read(0x1C00, 1))
    # time.sleep(0.5)
    # print(shm.shm_read(0x1C01, 8))
    #
    # print(shm.shm_write(0x1C08, [4,4.4,3, 3.3, 2, 2.2, 1, 1.1]))
    # time.sleep(0.5)
    # print(shm.shm_read(0x1C00, 8))

    # while True:
    #     shm.shm_write(0x1800, 0)
    #     time.sleep(0.01)
    #     shm.shm_read(0x1800, 6)
    #     time.sleep(0.01)
    #     shm.shm_write(0x1800, [1,6])
    #     time.sleep(0.01)
    #     shm.shm_read(0x1800,6)
    #     time.sleep(0.01)
    #     shm.shm_system_write(shm._SYSINFO_ADDR1, ["", "ShmServer.py",0])
    #     time.sleep(0.01)
    # print(_matI(4))
    # print(_minv([[1,2,3],[4,5,6],[7,8,9]]))
    # print(_bitflag(255, 1))
    # print(_bitflag(255, 8))

