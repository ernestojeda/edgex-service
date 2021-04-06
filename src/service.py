class Service:
    def hello(self, name):
        print(f'Hello {name}')

if __name__ == "__main__":
    print("Starting up your service...")

    s = Service()
    s.hello('world')