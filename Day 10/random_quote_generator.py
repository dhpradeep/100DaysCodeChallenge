import random

def quotes():
    quotes = ['Stay hungry, Stay foolish', 'write code, change world']
    quote = random.choice(quotes)
    return quote

print(quotes())