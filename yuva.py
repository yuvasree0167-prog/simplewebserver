
            </tr>
            <tr>
                <td>3.</td>
                <td>Installed RAM</td>
                <td>16.0GB</td>
            </tr>
            <tr>
                <td>4.</td>
                <td>System type</td>
                <td>64 bit operating system</td>
            </tr>
            <tr>
                <td>5.</td>
                <td>Product ID</td>
                <td>00327-60000-0000-AA72</td>
            </tr>

        </table>
    </body>
</html>
"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',8000)
httpd = HTTPServer(server_address,myhandler)
print("my webserver is running...")
httpd.serve_forever()from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
<!DOCTYPE html>
<html>
    <body>
        <table border="1"cellpadding="20" cellspacing="5">
            <tr>
                <th colspan="3">LAPTOP DETAILS (YUVASREE)</td>
            </tr>
            <tr bgcolor="green">
                <th>S.NO</th>
                <th>DEVICE SPECIFICATION</th>
                <th>TYPE</th>
            </tr>
            <tr><td>1.</td>
                <td>Device name</td>
                <td>DESKTOP9MEG185</td>
            </tr>
            <tr>
                <td>2.</td>
                <td>Processor</td>
                <td>13 GEN INTEL i5</td>