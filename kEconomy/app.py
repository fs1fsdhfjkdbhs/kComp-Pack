from time import sleep as wait

# Re-run when code has ended
def main():
    # Money

    kCash = 0

    cmdLine = input('∂ec.do ')
    cmdWORK = "work"
    cmdWL = "wl"

    # Jobs

    no_job = True
    engineer = False
    therapist = False
    doctor = False
    janitor = False
    youTuber = False
    musician = False

    # Commands

    if cmdLine == cmdWL:
        print('To become engineer, type "wENG". \nTo become therapist, type "wTHE". \nTo become doctor, type "wDOC". \nTo become janitor, type "wJAN" \nTo become a YouTuber, type "wYT". \nTo become a musician, type "mMUS". \nTo resign from your job, type "wRE".')
        cJOB = input('')

        if cJOB == 'wENG':
            print('Congrats! You are now an engineer!')
            no_job = False
            engineer = True
            therapist = False
            doctor = False
            janitor = False
            youTuber = False
            musician = False
        main()
    if cmdLine == cmdWORK:
        if no_job:
            print('You do not have a job yet! Type "wl" to get hired for a job!')
            main()
        elif engineer:
            print('---Work as an engineer!---')
            ejob = input('Task: Count to 10! Make sure you have "," after every number! ')
            if ejob == "1, 2, 3, 4, 5, 6, 7, 8, 9, 10":
                print('Great job! You got ƒ250 kCash for your efforts!')
                kCash += 250
                print('kCash: {}'.format(kCash))
                main()
            else:
                print('Oh come on! You counted wrong! You can have ƒ20 kCash for your efforts though.')
                kCash += 20
                print('kCash: {}'.format(kCash))
                main()
        elif therapist:
            print('---Work as a therapist!---')
            print('Task: Try to help a su!cidal person.')
            print('Customer: Hi uh, I am a very su!cidal person and I want to kill myself, what should I do?')
            tjob = input('')
            if tjob == "":
                print('Oh come on! You failed to help the su!cidal person, you were payed ƒ12 kCash for trying though.')
                kCash += 12
                print('kCash: {}'.format(kCash))
                main()
# Code starts here!
main()
