from concurrent import futures
import logging
import grpc
import server_pb2 as server_pb2
import server_pb2_grpc as server_pb2_grpc
from services.hello import Greeter
port = "50051"
def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    server_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)
    server.add_insecure_port("[::]:" + port)
    server.start()
    print("Server started, listening on " + port)
    server.wait_for_termination()


if __name__ == "__main__":
    logging.basicConfig(filename='logfile.log', level=logging.INFO)
    logging.info(f'servidor iniciado na porta {port}')
    serve()
