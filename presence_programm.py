import psutil
from pypresence import Presence
import time

while True:
    client_id = int(input('Application id in ddp: '))  # application id in ddp

    if client_id == None:
        print('Enter application id in ddp')  # check for input id
        exit()
    else:
        RPC = Presence(client_id, pipe=0)  # some bullshit
        RPC.connect()  # connect to discord
        details = input('Description of your activity: ')  # presence text
        if details == '':
            print('Description required')
        else:
            state = input('What exactly are you doing: ')  #
            if state == '':
                large_image = input('Image link: ')  # image link
                if large_image == '':
                    while True:  # infinite loop
                        print(RPC.update(details=details))
                        # update presence
                        time.sleep(15)  # pause for 15 seconds
                else:
                    large_text = input('Image text: ')  # image text
                    if large_text is None:
                        print(RPC.update(details=details,
                                         large_image=large_image))
                    else:
                        print(RPC.update(details=details,
                                         large_image=large_image,
                                         large_text=large_text))
            else:
                large_image = input('Image link: ')  # image link
                if large_image == '':
                    while True:  # infinite loop
                        print(RPC.update(details=details,
                                         state=state))
                        # update presence
                        time.sleep(15)  # pause for 15 seconds
                else:
                    large_text = input('Image text: ')  # image text
                    if large_text is None:
                        print(RPC.update(details=details,
                                         state=state,
                                         large_image=large_image))
                    else:
                        print(RPC.update(details=details,
                                         large_image=large_image,
                                         large_text=large_text))

