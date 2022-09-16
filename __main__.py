import connexion
from waitress import serve

def main():
    print("Welcome Sridhar!")
    create_server()

def create_server():
    print("Server Here!")

    app = connexion.App(__name__,specification_dir='./swagger/')
    app.add_api("swagger.yaml", arguments={'title': 'Sridhar API Server'})

    serve(app, host="localhost", port=1234)


if __name__ == "__main__":
    main()