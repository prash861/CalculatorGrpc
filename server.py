import grpc
from concurrent import futures
import time


import calci_pb2 as pb2
import calci_pb2_grpc as pb2_grpc


import calci


class CalculatorServicer(pb2_grpc.CalculatorServicer):
    def SquareRoot(self, request, context):
        response = pb2.Number()
        response.value = calci.square_root(request.value)
        return response


server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

pb2_grpc.add_CalculatorServicer_to_server(CalculatorServicer(), server)


print('Starting Server. Listening on port 50051.')
server.add_insecure_port('[::]:50051')
server.start()


try:
    while True:
        time.sleep(86400)
except KeyboardInterrupt:
    server.stop(0)
