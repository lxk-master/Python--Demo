'''
一个函数里面又调用了另外一个函数,这就是函数嵌套调用
如果函数test2中,又调用了另外一个函数test1
    那么执行到调用test1函数时,会先把函数test1中的任务都执行完
    才会回到test2中调用函数test1的位置,继续执行后续的代码
'''