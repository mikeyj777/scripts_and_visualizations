from random import choice

name = input("\n\n\nHello, what is your name? ")
how_is_emma = input(f"\n\n\n\nHello {name}, How are you?  ")
if how_is_emma.lower() in ['good', 'fine', 'great', 'ok', 'okay']:
    print(f"\n\n\nI'm glad to hear that {name}! 😊")
else:
    print(f"\n\n\noh {name} I'm sorry to hear that. If you need to talk, I'm here for you. 💖")

iters = input('\n\n\nHow many times should I say your name?')

ten_random_emojis = [
    '😀', '😂', '😍', '😎', '🤔', '😢', '😡', '🥳', '🤗', '😴'
]

for count in range(int(iters)):
    # random_emoji = choice(ten_random_emojis)
    emoji = ten_random_emojis[count % len(ten_random_emojis)]
    print(f"#{count + 1} {name}! {emoji}")
