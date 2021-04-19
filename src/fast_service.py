class FastService:
    '''
    This service does stuff super fast
    '''
    def fast(self, name):
        print(f'Going really super fast for {name}. Like for real.')


'''
This will start the service
'''
if __name__ == "__main__":
    print("Starting up your fast service...")

    fs = FastService()
    fs.fast('you')
