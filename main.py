import os

def make_commit(days: int):
    if days < 1:
        # Push command
        return os.system('git push')
    else:
        dates = f'{days} days ago'

        with open('data.txt', 'a') as file:
            file.write(f'{dates} <-This was the commit for the day\n')

            #staging
            os.system('git add data.txt')

            # commit
            os.system('git commit --date="'+dates+'" -m "Daily commit"')

            return days * make_commit(days-1)

make_commit(2)

