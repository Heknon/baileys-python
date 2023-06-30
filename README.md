# Goal

The goal of this project is to provide a well-written API for interacting with WhatsApp through a live-socket client.

The API will be written in Python.


# Architecture

There are a few main components that the system will be made up of:
1. Authentication
2. Protocol Communication
3. Event Handling

These are ranked in order of abstraction and as such should be implemented into the system in said order.
Each stage must have the previous stage in order to be implemented well.

# Resources

1. https://github.com/sigalor/whatsapp-web-reveng - How to implement the WA WebSocket protocol.
