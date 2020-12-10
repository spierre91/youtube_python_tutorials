class SpotifyUsers:
    def __init__(self, name, email, premium):
        self.name = name 
        self.email = email
        self.premium = premium 
    def isPremium(self):
        if self.premium:
            print(f'{self.name} is a premium user')
        else:
            print(f'{self.name} is not a premium user')


user1 = SpotifyUsers('Sarah Phillips', 'sphillips@gmail.com', True)
user2 = SpotifyUsers('Todd Grant', 'tgrant@gmail.com', False)


print(user1.name)
print(user2.name)

print(user1.email)
print(user2.email)

print(user1.premium)
print(user2.premium)


user1.isPremium()

user2.isPremium()
