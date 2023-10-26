import typing
from universal_object_pool import ObjectPool, AbstractObject
from threadpool_executor_shrink_able import BoundedThreadPoolExecutor
import threading
import time

"""
编码中有时候需要使用一种创建代价很大的对象，而且这个对象不能被多线程同时调用他的操作方法，

比如mysql连接池，socket连接池。
很多这样的例子例典型如mysql的插入，如果多线程高并发同时操作同一个全局connection去插入，很快就会报错了。
那么你可能会为了解决这个问题的方式有如下：

1.你可能这么想，操作mysql的那个函数里面每一次都临时创建mysql连接，函数的末尾关闭coonection，
  这样频繁创建和摧毁连接，无论是服务端还是客户端开销cpu和io高出很多。

2.或者不使用方案1，你是多线程的函数里面用一个全局connection，但是每一个操作mysql的地方都加一个线程锁，
  使得不可能线程1和线程2同时去操作这个connction执行插入，如果假设插入耗时1秒，那么100线程插入1000次要1000秒。

正确的做法是使用mysql连接池库。如果设置开启的连接池中的数量是大于100，100线程插入1000次只需要10秒，节省时间100倍。
mysql连接池已经有知名的连接池包了。如果没有大佬给我们开发mysql连接池库或者一个小众的需求还没有大神针对这个耗时对象开发连接池。
那么可以使用 ObjectPool 实现对象池，连接池就是对象池的一种子集，connection就是pymysql.Connection类型的对象，连接也是对象。
这是万能对象池，所以可以实现webdriver浏览器池。对象并不是需要严格实实在在的外部cocket或者浏览器什么的，也可以是python语言的一个普通对象。
只要这个对象创建代价大，并且它的核心方法是非线程安全的，就很适合使用对象池来使用它。

"""

"""
此模块演示一般常规性任意对象的池化
"""


class Core:  # 一般假设这是个三方包大神写的包里面的某个重要公有类,你需要写的是用has a 模式封装他，你当然也可以使用is a模式来继承它并加上clean_up before_back_to_queue 方法。
    def insert(self, x):
        time.sleep(0.5)
        print(f'插入 {x}')

    def close(self):
        print('关闭连接')


class MockSpendTimeObject(AbstractObject):

    def __init__(self, ):
        time.sleep(0.1)  # 模拟创建对象耗时

        s = 0  # 模拟创建对象耗费cpu
        for j in range(10000 * 500):
            s += j

        self.conn = self.core_obj = Core()  # 这个会造成obj.xx  自动调用 obj.core_obj.xx，很好用。

        self._lock = threading.Lock()

    def do_sth(self, x):
        with self._lock:
            self.conn.insert(x)
            print(f' {x} 假设做某事同一个object只能同时被一个线程调用此方法，是排他的')

    def clean_up(self):
        self.core_obj.close()

    def before_back_to_queue(self, exc_type, exc_val, exc_tb):
        pass


if __name__ == '__main__':
    pool = ObjectPool(object_type=MockSpendTimeObject, object_pool_size=40).set_log_level(10)


    def use_object_pool_run(y):
        """ 第1种 使用对象池是正解"""
        # with ObjectContext(pool) as mock_obj:
        #     mock_obj.do_sth(y)
        with pool.get() as mock_obj:  # type:typing.Union[MockSpendTimeObject,Core]
            # mock_obj.insert(y)  # 可以直接使用core_obj的方法
            mock_obj.do_sth(y)


    def create_object_every_times_for_run(y):
        """第2种 多线程函数内部每次都采用临时创建对象，创建对象代价大，导致总耗时很长"""
        mock_obj = MockSpendTimeObject()
        mock_obj.do_sth(y)


    global_mock_obj = MockSpendTimeObject()
    global_mock_obj.insert(6666)  # 自动拥有self.core_object的方法。


    def use_globle_object_for_run(y):
        """
        第3种 ，多线程中，使用全局唯一对象。少了创建对象的时间，但是操作是独占时间排他的，这种速度是最差的。
        """
        global_mock_obj.do_sth(y)


    t1 = time.perf_counter()
    threadpool = BoundedThreadPoolExecutor(50)

    for i in range(1000):  # 这里随着函数的调用次数越多，对象池优势越明显。假设是运行10万次，三者耗时差距会更大。
        # 这里演示三种调用，1是多线程里用使用对象池 2是使用多线程函数内部每次临时创建关闭对象 3是多线程函数内部使用全局唯一对象。

        threadpool.submit(use_object_pool_run, i)  # 6秒完成
        # threadpool.submit(create_object_every_times_for_run, i)  # 82秒完成
        # threadpool.submit(use_globle_object_for_run, i)  # 耗时100秒

    threadpool.shutdown()
    print(time.perf_counter() - t1)

    time.sleep(100)
