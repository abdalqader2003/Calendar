import emoji
from pystyle import*
print(Box.Lines('[+] emoji chat'))
Write.Print('[-] emoji chat \n ',Colors.purple_to_red, interval=0.1)
print(Box.Lines("<Program emoji chat>"))
e1 = emoji.emojize(':yellow_heart:')
e2 = emoji.emojize(':blue_heart:')
e3 = emoji.emojize(':red_heart:')
e4 = emoji.emojize(':purple_heart:')
e5 = emoji.emojize(':green_heart:')
emoji = [e1 , e2 , e3 , e4 , e5 ]
hi = ['welcome', 'hello' 'hi', 'welcome dear']
name = ['abood', 'natalia', 'hema', 'abd']
while True:
    chat = input('Enter your message : ')
    if chat == 'hello' :
        answer = random.choice(hi)
        answer_emo = random.choice(emoji)
        print(answer+ ' ' + answer_emo)
    elif chat == 'whats your nam'

    else:
        print(emoji.emojize('sorry : borken_heart'))
