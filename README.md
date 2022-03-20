# PyProxy

this is a very basic (and stupid) python udp proxy
program for symulating latency

---

## Usage

```bash
./proxy.py proxy_ip proxy_port server_ip server_port delay_time_seconds
```

pretty much does what you would expect it to do

---

## Other notes

this is a WIP program and is veeeeery hacky, just
made as a quick tool for testing network stuff in kinetikinesis
currently the client has to send data over to the server and 
the proxy has to send over data to the server for the connection
to be established

TODO:
fix that :)
