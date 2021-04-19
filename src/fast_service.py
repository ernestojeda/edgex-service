class FastService:
    '''
    This service does stuff super fast
    '''
    def super_fast(self, name):
        print(f'Going really super fast for {name}. Like for real.')


'''
This will start the service
'''
if __name__ == "__main__":
    print("Starting up your fast service...")

    fs = FastService()
    fs.super_fast('you')
