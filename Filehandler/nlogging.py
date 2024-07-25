import logging
#import logging.config
logging.basicConfig(filename="/var/tmp/applog", format='%(asctime)s %(message)s', filemode='w')
#logging.config.fileConfig('testlog')
logger = logging.getLogger()

logger.info('information messages')

'''
debug
info
warning
error
critical 

'''



