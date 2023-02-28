######################################################################
# Author: Dr. Patrick Shepherd      TODO: Change this to your names
# Username: shepherdp               TODO: Change this to your usernames
#
# Assignment: T5: Buggy Fruit
# Purpose: A flawed birthday program
######################################################################
# Acknowledgements:
#   Original Author: Dr. Jan Pearce
#
# licensed under a Creative Commons
# Attribution-Noncommercial-Share Alike 3.0 United States License.
####################################################################################

def happyBirthday(name, age):
    '''
    Happy birthday function
    '''

    for i in range(age):
        print("Happy Birthday to you!")

        print(f"Happy Birthday, dear {name} !")

        print("Happy Birthday to you!")
def main():
    happyBirthday("Felix", 4)                                  # name and number of times to loop
main()

