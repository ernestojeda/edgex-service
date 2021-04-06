class Service:
    '''
    This will say hello
    '''
    def hello(self, name):
        print(f'Hello {name}')

    '''
    This function thinks your smile looks great
    '''
    def smile(self, name):
        print(f"{name}, thanks for the smile")

'''
This will start the service
'''
if __name__ == "__main__":
    print("Starting up your service...")

    s = Service()
    s.hello('world')
    s.smile('Fred')