from ucall.rich_uring import Server

server = Server()

@server
def sum(a: int, b: int):
    print(a+b)
    return a + b

server.run() 