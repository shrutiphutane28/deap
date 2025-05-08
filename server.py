from xmlrpc.server import SimpleXMLRPCServer
import threading

# Factorial function
def factorial(n):
    if n < 0:
        return "Factorial not defined for negative numbers"
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Shutdown function
def shutdown():
    print("Shutting down the server...")
    threading.Thread(target=server.shutdown).start()
    return "Server is shutting down."

# Create the server
server = SimpleXMLRPCServer(("localhost", 8000), allow_none=True)
print("Server is listening on port 8000...")

# Register functions
server.register_function(factorial, "factorial")
server.register_function(shutdown, "shutdown")

# Run the server
server.serve_forever()
