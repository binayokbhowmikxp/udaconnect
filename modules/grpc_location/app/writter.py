import grpc
import location_pb2
import location_pb2_grpc

"""
Sample implementation of a writer that can be used to write messages to gRPC.
"""

print("Sending sample payload...")

channel = grpc.insecure_channel("localhost:5005")
stub = location_pb2_grpc.LocationServiceStub(channel)

# Update this with desired payload
location1 = location_pb2.LocationMessage(
    person_id="8",
    latitude="25",
    longitude='-25',
)

location2 = location_pb2.LocationMessage(
    person_id="9",
    latitude="15",
    longitude='-15',
)

response1 = stub.Create(location1)
response2 = stub.Create(location2)
