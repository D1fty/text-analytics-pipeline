import os

def clean():
    DMF = 'del $TMPDIR/magick*'
    # count = 'find $TMPDIR -name "magick*" -maxdepth 1 -type f | wc -l'
    # total = os.system(count)
    os.system(DMF)
    # total = os.system(count)
