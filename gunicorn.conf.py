import multiprocessing

bind = "127.0.0.1:8081"
workers = 2
errorlog = '/mnt/magicshare/website/gunicorn.error.log'
#accesslog = './gunicorn.access.log'
#loglevel = 'debug'
proc_name = 'website'

