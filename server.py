from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import bcrypt
from urllib.parse import parse_qs, urlparse
from database import Database

class NoteApiHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/users':
            self.send_response(200)
            self.send_header('content-type', 'application/json')
            self.end_headers()

            db = Database()
            users = db.fetch_all()

            self.wfile.write(json.dumps(users).encode())

        elif self.path.startswith('/users/'):
            user_name = str(self.path.split('/')[-1])
            db = Database()
            user = db.fetch_one(user_name)

            if user:
                self.send_response(200)
                self.send_header('content-type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps(user).encode())

            else:
                self.send_response(404)
                self.end_headers()

    def do_POST(self):
        if self.path == '/users':
            content_length = int(self.headers['content-Length'])
            post_data = self.rfile.read(content_length).decode('utf-8')
            data = json.loads(post_data)

            #data = parse_qs(post_data)
            # print("post_data: ", post_data)
            # print("data: ", data)

            username, password, firstname, lastname = "", "", "", ""
            gender, bloodtype, dateofbirth = "", "", ""
            address, city, province, postalcode = "", "", "", ""

            # username = data.get('username', [''])[0]
            # password = data.get('password', [''])[0]

            username = data["username"]
            password = data["password"]
            firstname = data["firstname"]
            lastname = data["lastname"]
            gender = data["gender"]
            bloodtype = data["bloodtype"]
            dateofbirth = data["dateofbirth"]
            address = data["address"]
            city = data["city"]
            province = data["province"]
            postalcode = data["postalcode"]

            password_bytes = password.encode('utf-8')
            salt = bcrypt.gensalt()
            hashed = bcrypt.hashpw(password_bytes, salt)

            # print("username: ", username)
            # print("password: ", password)
            # print("password: ", password_bytes)
            # print("dateofbirth: ", dateofbirth)
            # print("Salt :", salt)
            # print("Hashed: ", hashed)

            db = Database()
            db.create_user(username, hashed, firstname, lastname, gender, bloodtype, dateofbirth, address, city, province, postalcode)

            self.send_response(201)
            self.end_headers()

    def do_PUT(self):
        if self.path.startswith('/users/'):
            user_name = str(self.path.split('/')[-1])
            content_length = int(self.headers['content-Length'])
            put_data = self.rfile.read(content_length).decode('utf-8')
            data = json.loads(put_data) 

            username, password, firstname, lastname = "", "", "", ""
            gender, bloodtype, dateofbirth = "", "", ""
            address, city, province, postalcode = "", "", "", ""
            
            #print("post_data: ", put_data)
            #data = parse_qs(put_data)
            #print("data: ", data)

            username = data["username"]
            password = data["password"]
            firstname = data["firstname"]
            lastname = data["lastname"]
            gender = data["gender"]
            bloodtype = data["bloodtype"]
            dateofbirth = data["dateofbirth"]
            address = data["address"]
            city = data["city"]
            province = data["province"]
            postalcode = data["postalcode"]

            password_bytes = password.encode('utf-8')
            salt = bcrypt.gensalt()
            hashed = bcrypt.hashpw(password_bytes, salt)

            # print("username: ", username)
            # print("password: ", password)
            # print("password: ", password_bytes)
            # print("dateofbirth: ", dateofbirth)
            # print("Salt :", salt)
            # print("Hashed: ", hashed)

            db = Database()
            db.update_user(username, hashed, firstname, lastname, gender, bloodtype, dateofbirth, address, city, province, postalcode)

            self.send_response(200)
            self.end_headers()

    def do_DELETE(self):
        if self.path.startswith('/users/'):
            user_name = str(self.path.split('/')[-1])

            db = Database()
            db.delete_user(user_name)

            self.send_response(204)
            self.end_headers()


def run(server_class=HTTPServer, handler_class=NoteApiHandler, port=8080):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Starting server on port {port}")
    httpd.serve_forever()
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    print('Stopping httpd server..')


if __name__ == '__main__':
    run()