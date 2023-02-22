import os

SECRET_KEY_DJANGO = 'django-insecure-a_#rjw9b$=4r12cm!xi!24mu43bm49zhk3z^vgkd5ehr2h=7yvk@&'

def secret():
    return os.environ['SECRET_KEY_DJANGO']


Password_noise = 'L435mhys2bNqu87hpYmax'