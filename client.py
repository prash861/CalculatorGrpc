import grpc

import calci_pb2 as pb2
import calci_pb2_grpc as pb2_grpc


channel = grpc.insecure_channel('localhost:50051')


stub = pb2_grpc.CalculatorStub(channel)
number = pb2.Number(value=float(input("Enter any Number to find its sqare root: ")))
response = stub.SquareRoot(number)
print(response.value)
