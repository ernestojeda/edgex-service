class Service:
    def hello(self, name):
        print(f'Hello {name}')

    def smile(self, name):
        print(f"{name}, thanks for the smile")

if __name__ == "__main__":
    print("Starting up your service...")

    s = Service()
    s.hello('world')
    s.smile('Fred')