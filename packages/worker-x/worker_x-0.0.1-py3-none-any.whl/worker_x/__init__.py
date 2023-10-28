
from threading import Thread,Lock
import time
import ctypes


class ThreadData(list):
    lock = Lock()
    _i = -1
    def next(self, loop=False):
        with self.lock:
            if loop:
                self._i = (self._i + 1) % self.__len__()
            else:
                self._i += 1
            __i = self._i
        if __i < self.__len__():
            return super().__getitem__(__i)
        
class Worker(Thread):
    def __init__(self,target,list_args,daemon = None) -> None:
        super().__init__(daemon=daemon)
        self.target = target 
        if type(list_args) is list:
            self.list_args = ThreadData(list_args)
        else:
            self.list_args = list_args
        self.result = []

    def run(self):
        while item := self.list_args.next():
            if type(item) is tuple:
                self.result.append(self.target(*item))
            else:
                self.result.append(self.target(item))
    
    def join(self, timeout: float | None = None) -> None:
        super().join(timeout)
        return self.result

    def terminate(self):
        is_alive = False
        for _ in range(20):
            if self.is_alive():
                is_alive = True
                break
            time.sleep(0.1)
        if is_alive == False:
            return
        exc = ctypes.py_object(SystemExit)
        res = ctypes.pythonapi.PyThreadState_SetAsyncExc(
            ctypes.c_long(self.ident), exc)
        if res == 0:
            raise ValueError("nonexistent thread id")
        elif res > 1:
            ctypes.pythonapi.PyThreadState_SetAsyncExc(self.ident, None)
            raise SystemError("PyThreadState_SetAsyncExc failed")

class Pool():
    def __init__(self,thread:int,target,list_args:list,deamon=None) -> None:
        self.__inp = ThreadData(list_args)
        self.__out = []
        self.__thread_num = thread
        self.__thread = []
        self.target = target
        self.daemon = deamon

    
    def start(self):
        for _ in range(self.__thread_num):
            t = Worker(target=self.target,list_args=self.__inp,daemon=self.daemon)
            t.start()
            self.__thread.append(t)

    def join(self,timeout: float | None = None):
        time.sleep(timeout)
        if timeout is not None:
            for t in self.__thread:
                self.__out += t.join(0)
        else:
            for t in self.__thread:
                self.__out += t.join()        
        return self.__out
    
    def terminate(self):
        for t in self.__thread:
            t.terminate()    
            