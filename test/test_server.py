# import unittest
# import threading
# import os,sys
# from server import *
# from network import *
# from _socketEchoServer import socketEchoServerMock
#
# class TestServer(unittest.TestCase):
#
#     @classmethod
#
#     def startActualServer(self):
#         print('a01')
#         est = threading.Thread(target=server_run)
#         est.daemon = True
#         est.start()
#         self.est = est
#         print('a2')
#
#
#     def test_threaded_client(self):
#         pass
#     def test_return_players(self):
#         ret = return_players()
#         assert ret == {}
#     def test_server_run(self):
#         print('a')
#         self.startActualServer()
#         print('b')
#         hostname = socket.gethostname()
#         net = Network(socket.gethostbyname(hostname))
#         assert net.client._closed == False
#         ret = net.send("test_str")
#         net.client.close()
#         assert net.client._closed == True
#         assert net.id == 'ok' # locking current behavior w/ test
#                               # even if i don't fully understand :p
#         net = Network(socket.gethostbyname(hostname))
#         assert net.client._closed == False
#         net.client.close()
#         assert net.client._closed == True
#         # connect
#         # should get 'ok'
#         #send empty data to close?
