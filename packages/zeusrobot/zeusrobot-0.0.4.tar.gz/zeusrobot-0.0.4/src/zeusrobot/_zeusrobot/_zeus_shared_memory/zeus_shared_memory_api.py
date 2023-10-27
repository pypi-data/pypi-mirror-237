#CSpell:ignore shmwin,_getframe
"""
Windows PC에서 공유메모리를 접근하기 위한 API
"""
import os
import sys
import mmap
import tempfile
import struct
import threading
from typing import Any,Union,Tuple,List

from .zeus_shared_memory_table import ZeusShmData
from .zeus_shared_memory_format import _shm_format, _shm_num_data

shm_format, shm_num_data = _shm_format, _shm_num_data


class ZeusShm:
    u"""Shared memory class for Windows"""

    _ZeusShmTable = ZeusShmData.ZeusShmTable
    _ZeusShmSize:int = ZeusShmData.ZeusShmSize
    _debug_out = False

    @classmethod
    def log(cls, *msg:Any) -> None:
        """Debug output
        """
        if cls._debug_out:
            print(*msg)

    def __init__(self, is_readonly:bool = True) -> None:
        """

        Args:
            is_readonly (bool, optional): Set False if write function is required. Defaults to True.

        Remark:
            Only system manager should use 'is_readonly = False' condition.
            
        """
        self.fp = None
        self.mm: Union[mmap.mmap, None] = None
        self.update_counter = 0
        self.lock = threading.Lock()
        self.is_read_only = is_readonly
        if os.name == "nt":
            tempdir = tempfile.gettempdir()
        else:
            tempdir = "/dev/shm"
        path = ".ZeusShmData"
        self.filepath = tempdir + os.sep + path
        self.log("* Shared file path:{}".format(self.filepath))
        self.log("* Shared memory size: {} bytes".format(self._ZeusShmSize))
        if is_readonly:
            self.fp = open(self.filepath, 'rb')
            self.mm = mmap.mmap(self.fp.fileno(), 0, access=mmap.ACCESS_READ)
        else:
            # Erase old data
            if not os.path.isfile(self.filepath) or os.path.getsize(self.filepath)!=self._ZeusShmSize:
                self.log("* Recreate shared memory file.")
                if os.path.isfile(self.filepath):
                    os.remove(self.filepath)
                self.fp = open(self.filepath, 'wb')
                self.fp.write(bytes([0]*self._ZeusShmSize))
                self.fp.close()
            self.fp = open(self.filepath, 'r+b')
            self.fp.seek(0)
            self.mm = mmap.mmap(self.fp.fileno(), 0, access=mmap.ACCESS_WRITE)
        self.log("{} success".format(sys._getframe().f_code.co_name))


    def __del__(self) -> None:
        self._close()


    def _close(self) -> None:
        if self.mm is not None:
            self.mm.close()
            del self.mm
            self.mm = None
        if self.fp is not None:
            self.fp.close()
            del self.fp
            self.fp = None
        self.log("{}".format(sys._getframe().f_code.co_name))


    def _search_index(self, address:int) -> int:
        find_idx = -1
        for idx in range(len(self._ZeusShmTable)):
            item = self._ZeusShmTable[idx]
            if item[0] == address:
                find_idx = idx
                break
        
        # for idx, item in enumerate(self._ZeusShmTable):
        #     if item[0] == address:
        #         find_idx = idx
        #         break

        if find_idx == -1:
            raise ValueError("Invalid address:0x{:04X}".format(address))
        return find_idx


    def _prepare_extract(self, begin_idx:int, n:int) -> Tuple[int,str,int]:
        target_size = 0
        pack_str = "<"
        for i in range(n):
            if begin_idx + i >= len(self._ZeusShmTable):
                break
            adr,size,_,unpack_ch,_ = self._ZeusShmTable[begin_idx + i]
            target_size += int(size)
            pack_str += unpack_ch
        return (target_size, pack_str)


    def _read_binary(self, begin_idx:int, size:int) -> bytes:
        if self.mm is None:
            return b""
        self.mm.seek(self._ZeusShmTable[begin_idx][2])
        byte_data = self.mm.read(size)
        #print("read all data:{}:{}".format(size,byte_data))
        return byte_data


    def _write_binary(self, begin_idx:int, data:bytes) -> None:
        if self.mm is None:
            return
        self.mm.seek(self._ZeusShmTable[begin_idx][2])
        self.mm.write(data)


    def _clear_all(self) -> None:
        """Clear all memory"""
        #print("_clear_all ({})".format(self.is_read_only), flush=True)
        if self.is_read_only:
            raise PermissionError("Current permission is ReadOnly.")
        zero_array = [0]*self._ZeusShmSize
        zero_data = bytes(zero_array)
        self._write_binary(0,zero_data)


    def read(self, address:int, n:int = 1) -> List[Any]:
        """Read data array from shared memory
        
        Args:
            address(int): Start address to write
            n(int): number of data (Default value is 1)
        
        Returns:
            List[Any]: Data array
        
        Remark:
            Read function is supposed to be used by any process.
        
        """
        if n<=0:
            raise IndexError("Invalid number value:{}".format(n))

        begin_idx = self._search_index(address)
        target_size, pack_str= self._prepare_extract(begin_idx,n)

        byte_data = self._read_binary(begin_idx,target_size)
        # print("read_binary idx={},target_size={},pack_str={},n={},len={}".format(
        #     begin_idx,target_size,pack_str,n,len(byte_data)))

        result = struct.unpack(pack_str,byte_data)
        result = [ x.rstrip(b'\x00').decode() if isinstance(x,bytes) else x for x in result]
        self.log("{}({},{})={}".format(sys._getframe().f_code.co_name,address,n,result))
        return result


    def write(self, address:int, data_list:List[Any]) -> None:
        """Write data array to shared memory

        Args:
            address(int): Start address to write
            data_list(List[Any]):Data array to be written 

        Remark:
            Write function is supposed to be used by only system manager.
            
        """
        if self.is_read_only:
            raise PermissionError("Current permission is ReadOnly.")
        if type(data_list) != list:
            raise TypeError("data_list must be list.")
        n = len(data_list)
        if n == 0:
            raise ValueError("data_list is empty.")

        begin_idx = self._search_index(address)
        _, pack_str = self._prepare_extract(begin_idx,n)
        #print("pack_str={}, data={}".format(pack_str,data_list))
        data_list = [x.encode() if isinstance(x,str) else x for x in data_list]
        #print("pack_str:{}".format(pack_str))
        #print("data:{}".format(data_list))
        pack_data = struct.pack(pack_str,*data_list)
        self._write_binary(begin_idx,pack_data)
        self.log("{}({},{})".format(sys._getframe().f_code.co_name,address,n))

#EOF
