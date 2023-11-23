import server_pb2 as server_pb2
import server_pb2_grpc as server_pb2_grpc
from models.hello import Hello
import logging

logging.basicConfig(filename='logfile.log', level=logging.INFO)

class Greeter(server_pb2_grpc.GreeterServicer):
    def SayHello(self, request, context):
        nome = Hello(request.name)
        logging.info('recebendo request grpc')
        return server_pb2.HelloReply(message=Hello.mensagem(nome))
