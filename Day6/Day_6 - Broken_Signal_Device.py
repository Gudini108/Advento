import os
import sys

with open(os.path.join(sys.path[0], "input.txt"), 'r') as f:
    signal = f.read()
    
letters_dict = dict(enumerate(signal, start=1))




def packet_message_scanner(input, packet_length):
    
    counter = 0                                                 # out switch, indicating when programm is supposed to end
    scanner_receiver = []                                       # our glorious Scan-O-Matic 9002!

    while counter != 1:                                         # untill counter is not True so to say, do the following:
        
        while len(scanner_receiver) < packet_length:            # while we did not see all 'packet length' letters on our 
                                                                # totally digital scanner screen, do this:
            for pos in range(1, len(input)+1):                  # take letter by letter from our input
                scanner_receiver.append(input[pos])             # and place it in our scanner
                
                if len(scanner_receiver) == packet_length:      # when we have all 4 letters in it
                    check_scanner = set(scanner_receiver)       # make it a set to remove all duplicate values from it
                    
                    if len(check_scanner) == packet_length:     # compare lengths of our set to number of distinct letters we need
                        print()
                        print('------STOP------')
                        print(f'{pos} characters were processed'\
                            'by scanner before the first marker'\
                            'was detected... beep-boop!')
                        print()
                        counter += 1                            # move up the counter to end our scanning
                    
                    else:
                        scanner_receiver.pop(0)                 # else - remove 1st item from our 'Scan-O-Matic 9002' and continue
                        

packet_message_scanner(letters_dict, 4)

packet_message_scanner(letters_dict, 14)