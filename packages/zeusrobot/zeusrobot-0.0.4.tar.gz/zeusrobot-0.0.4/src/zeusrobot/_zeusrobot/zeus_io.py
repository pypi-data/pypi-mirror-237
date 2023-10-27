import time
import threading

from . import zeus_rblib
from .zeus_error import *

# for module check
# import zeus_rblib
# from zeus_error import *

class _ZeusIO(object):
    """
    ZeusIO 클래스
    digital IO를 제어

    Methods:
        [Public]
        open(self, *args): 로봇 연결 초기화 (RobotClient 오픈)
        close(self): 로봇 연결 해제
        wait(self, adr, data, wait_time): 해당 어드레스의 IO가 data가 될때까지 wait_time 시간동안 대기
        dout(self, adr, data, delay=0): Digital Output 신호 제어
        din(self, *adr): Digital Input 신호 수신

        [Internal]
        _dout(self, adr, data): Digital Output 메서드
        _din(self, *adr): Digital Input 메서드
        _pars(self, st): 문자열을 체크하여 1, 0, *, n, s, d만이 포함된 문자열로 변환
        __senddata(self, col, d0int, m0int, d1int, m1int): Digital Output 데이터 전송
        __rcvd(self, col): col 주소의 64bit 데이터를 수신
        __replace(self, st, ch, n): 오른쪽에서 n번째 글자를 변경
        __bsNot(self, p): bitstream의 not 연산
        __bsAnd(self, p, q): bitstream의 and 연산
        __bs2i(self, st): bitstream 형식의 str 데이터를 int 형으로 반환
        __i2bs(self, n): integer -> 32자리 bit stream 으로 변환 (1 Word)
    """
    def __init__(self):
        self.__flag = 0
        self.__rb = None
        self.open()
        self._lock = threading.Lock()

    def __del__(self):
        if self.__flag == 1:
            if self.__rb is not None:
                self.__rb.close()
                self.__flag = 0

    def open(self, *args):
        """
        로봇 연결 초기화
        Args:
            *args: IP 주소(str), 포트 번호(int) 기본값 : '192.168.0.23', 12345

        Returns:
            bool : 수행 결과
        """
        self.__flag = 0
        try:
            if len(args) == 0:
                self.__rb = zeus_rblib.RobotClient('192.168.0.23', 12345)
                self.__rb.open(3)
                self.__flag = 1
            elif len(args) == 1:
                if isinstance(args[0], zeus_rblib.RobotClient):
                    self.__rb = args[0]
                    self.__flag = 0 # is'nt opened by IO
                elif isinstance(args[0], str):
                    self.__rb = zeus_rblib.RobotClient(args[0], 12345)
                    self.__rb.open()
                    self.__flag = 1
                else:
                    raise ZeusIOException(ERR_ZERO_IO, 1,"open")
            elif len(args) == 2:
                if isinstance(args[0],str) and isinstance(args[1],int):
                    self.__rb = zeus_rblib.RobotClient(args[0], args[1])
                    self.__rb.open()
                    self.__flag = 1
                else:
                    raise ZeusIOException(ERR_ZERO_IO, 1,"open")
            else:
                raise ZeusIOException(ERR_ZERO_IO, 1,"open")
        except Exception as e:
            raise ZeusIOException(ERR_ZERO_IO, 2, "open", e)

        return True

    def close(self):
        try:
            self.__flag == 1
            if self.__rb is not None:
                self.__rb.close()
                self.__flag = 0
        except Exception as e:
            raise ZeusIOException(ERR_ZERO_IO, 3, "close", e)

        return True

    def wait(self, adr, data, wait_time):
        """
        해당 어드레스의 IO가 data가 될때까지 wait_time 시간동안 대기
        Args:
            adr(int): input 포트의 시작 번호
            data(str): input 값. ex)'1001'
                * '1' = ON
                * '0' = OFF
            wait_time(float): 대기 시간

        Returns:

        """
        try:
            ts = time.time()
            while -1:
                dlen = len(data)
                if dlen == 1:  # '1' or '0'
                    dbit = self.din(adr)
                    getd = dbit
                    dat = self._pars(data)[1]
                else:
                    datar = self._pars(data)
                    mask = datar[2]
                    dat = datar[1]
                    getd = self.din(adr, adr + len(data) - 1)
                    dbit = self.__bsAnd(getd, self.__bsNot(mask))
                if dbit == dat:  # 읽어온 입력값 == wait 입력값
                    return [True, getd, time.time() - ts]
                time.sleep(0.05)
                if time.time() - ts >= wait_time:  # 대기 시간 초과 시
                    return [False, getd, time.time() - ts]
        except Exception as e:
            raise ZeusIOException(ERR_ZERO_IO, 4, "wait", e)

    def dout(self, adr, data, delay=0):
        """
        Digital Output 신호 제어
        Args:
            adr: output 포트의 시작 번호 (16-31)
            data: output 값. adr부터 LSB->MSB 순으로 대입 ex)'1001'
                * '1' = ON
                * '0' = OFF
            delay:

        Returns:

        Examples:
            1. 딜레이 미적용 시
            dout(16,'1001')
            * LSB가 시작 포트 번호에 해당하며, LSB->MSB 순서대로 할당
            * 16 : 1
            * 17 : 0
            * 18 : 0
            * 19 : 1

            2. 딜레이 적용 시
            dout(16, '1001', 1)
            함수 호출 이후 1초 뒤에 dout이 반영됨. (스레드 호출하고 종료되어 다음 스크립트 진행)
        """

        try:
            if delay == 0:
                self._dout(adr, data)
            elif delay > 0:
                self.__t = _DelayOut(self, adr, data, delay)
                self.__t.start()
        except Exception as e:
            raise ZeusIOException(ERR_ZERO_IO,5, "dout", e)

    def din(self, *adr):
        """
        Digital Input 신호 수신
        Args:
            *adr: input 포트 시작 번호, input 포트 끝 번호

        Returns:

        Examples:
            din(1) : 포트 1을 읽음
            din(1,4) : 포트 1부터 4까지 읽음
        """
        try:
            if len(adr) == 1:
                retval = self._din(adr[0])
                return retval
            elif len(adr) == 2:
                retval = self._din(adr[0], adr[1])
                return retval
            else:
                raise ZeusIOException(ERR_ZERO_IO,1, "din")
        except Exception as e:
            raise ZeusIOException(ERR_ZERO_IO,6, "din", e)

    def _dout(self, adr, data):
        """
        Digital Output 메서드
        Args:
            adr(int): output 포트 시작 번호
            data(str): output 값. adr부터 LSB->MSB 순으로 대입 ex)'1001'
                * '1' = ON
                * '0' = OFF

        Returns:
            bool : 성공 여부
        """
        with self._lock:
            da = data.replace(" ", "")  # str의 공백 제거 (입력의 편의를 위해 공백 문자 허용)
            row = adr % 32
            col = adr // 32
            dat = self._pars(da)
            dal = self.__replace("0" * 64, dat[1], row)
            cal = self.__replace("1" * 64, dat[2], row)
            d0 = dal[32:]
            c0 = cal[32:]
            d1 = dal[:32]
            c1 = cal[:32]
            d0int = int(d0, 2)
            c0int = int(c0, 2)
            d1int = int(d1, 2)
            c1int = int(c1, 2)

            res = self.__senddata(col, d0int, c0int, d1int, c1int)

        if res[0] == False:
            raise ZeusIOException(res[1], res[2], "_dout")

        return True

    def _din(self, *adr):
        """
        Digital Input 메서드
        Args:
            *adr: input 포트 시작 번호, input 포트 끝 번호

        Returns:
            string : 성공시 반환. 읽어온 input data
            Exception : 실패 시 예외 호출
        """
        with self._lock:
            try:
                col = adr[0] // 32  # word no 계산
                offset = col * 32
                row = 63 - (adr[0] - offset)  # LSB 기준으로 읽을 위치
                data = self.__rcvd(col)
            except Exception as e:
                raise ZeusIOException(ERR_ZERO_IO, 6, "_din", e)

        if len(adr) == 1:
            return data[row:row + 1]
        elif len(adr) == 2:
            row1 = 63 - (adr[1] - offset)
            if row1 >= 0:
                return data[row1:row + 1]
            else:
                raise ZeusIOException(ERR_ZERO_IO, 1, "_din")
        else:
            raise ZeusIOException(ERR_ZERO_IO, 1, "_din")

    def _pars(self, st):
        """
        문자열을 체크하여 1, 0, *, n, s, d만이 포함된 문자열로 변환
        Args:
            st(str): 문자열

        Returns:
            list : [결과문자열, data, mask]
        """
        if isinstance(st, str) and len(st) <= 32:  # 32개 까지만 가능
            if st[:2] == "0x" or st[:2] == "0X":  # 문자열 앞에 0x, 0X이 있으면 에러 (hexadecimal)
                raise ZeusIOException(ERR_ZERO_IO,1,"_pars")
            elif st[:2] == "0b":  # 문자열 앞에 0b 있으면 에러 (binary)
                raise ZeusIOException(ERR_ZERO_IO,1,"_pars")
            else:
                rslt = st
                dat = ""
                mask = ""
                for i in range(len(st) - 1, -1, -1):
                    if (st[i] != "0" and st[i] != "1" and st[i] != "*" and st[i] != "n" and
                            st[i] != "s" and st[i] != "d"):
                        rslt = self.__replace(rslt, "*", len(st) - i - 1)
                    if rslt[i] == "1":
                        dat = "1" + dat
                    else:
                        dat = "0" + dat

                    if rslt[i] == "*" or rslt[i] == "n" or rslt[i] == "s" or rslt[i] == "d":
                        mask = "1" + mask
                    else:
                        mask = "0" + mask
            return [rslt, dat, mask]
        else:
            raise ZeusIOException(ERR_ZERO_IO,1,"_pars")

    def __senddata(self, col, d0int, m0int, d1int, m1int):
        """
        digital output 데이터 전송
        Args:
            col:
            d0int: 32bit dataL
            m0int: 32bit maskL
            d1int: 32bit dataH
            m1int: 32bit maskH

        Returns:
            ioctrl 실행 결과
        """
        res = self.__rb.ioctrl(col, d0int, m0int, d1int, m1int)
        return res

    def __rcvd(self, col):
        """
        col 주소의 64bit 데이터를 수신
        Args:
            col(int): 시작 어드레스

        Returns:
            str : 64자리 비트스트림 데이터
        """
        dummy = 2 ** 32 - 1
        res = self.__rb.ioctrl(col, dummy, dummy, dummy, dummy)
        if res[0] == False:
            raise ZeusIOException(res[1], res[2], "__rcvd")

        return self.__i2bs(res[2]) + self.__i2bs(res[1])

    def __replace(self, st, ch, n):
        """
        오른쪽에서 n번째 글자를 변경
        Args:
            st(str): 원래 문자열
            ch(str): 대체할 문자열
            n(int): 대체할 비트 위치

        Returns:
            str : 변경된 문자열
        """
        if len(st) < n:
            stret = st
        else:
            num = len(st) - n
            num0 = len(st) - n - len(ch)
            stret = st[:(num0)] + ch + st[num:]
            stret = stret[-1 * len(st):]
        return stret

    def __bsNot(self, p):
        """
        bitstream의 not 연산
        Args:
            p(str): bitstream 형식의 str 데이터

        Returns:
            str : bitstream 형식의 str 데이터
        """
        return bin(self.__bs2i(p) ^ 2 ** 32 - 1)[-len(p):]

    def __bsAnd(self, p, q):
        """
        bitstream의 and 연산
        Args:
            p(str): bitstream 형식의 str 데이터
            q(str): bitstream 형식의 str 데이터

        Returns:
            str : bitstream 형식의 str 데이터
        """
        if len(p) > len(q):
            l = q
        else:
            l = p
        return bin(self.__bs2i("1" + p) & self.__bs2i("1" + q))[-len(l):]

    def __bs2i(self, st):
        """
        bitstream 형식의 str 데이터를 int 형으로 반환
        Args:
            st: bitstream 형식의 str 데이터

        Returns:
            int : int형으로 변환된 데이터
        """
        return int(st, 2)

    def __i2bs(self, n):
        """
        integer -> 32자리 bit stream 으로 변환 (1 Word)
        Args:
            n: 10진수 정수 (int)

        Returns:
            str : bit stream 형식의 데이터
        """
        p = format(n, "032b")
        return p[-(len(p)):]


class _DelayOut(threading.Thread):
    """
    dout_delay 기능을 구현한 클래스
    """
    def __init__(self, IO, adr, data, delay):
        threading.Thread.__init__(self)
        self.io = IO
        self.adr = adr
        self.data = data
        self.delay = delay
        self.lock_obj = threading.Lock()

    def run(self):
        """
        스레드 동작.
        delay 만큼 대기한 다음 dout 메서드 호출 후 스레드 종료
        Returns:

        """
        try:
            self.lock_obj.acquire()
            time.sleep(self.delay)
            self.io.dout(self.adr,self.data)
            time.sleep(1)
            self.lock_obj.release()
        except Exception as e:
            raise ZeusIOException(ERR_ZERO_IO, 7, "DelayOut.run", e)


if __name__ == "__main__":
    io = _ZeusIO()
    io.open()
    io.dout(16,'10101010')
    time.sleep(1)
    io.dout(16,'01010101')



