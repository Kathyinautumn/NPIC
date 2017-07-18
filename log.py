import logging

# this is for setting the route for saving the file
LOG_FILENAME = "/Users/zhangqiushui/Desktop/NPIC/final_design/log.txt"
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename='myapp.log',
                    filemode='w')

logging.debug('This is debug message')
logging.info('This is info message')
logging.warning('This is warning message')

# Create logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# this is for setting the file
fh = logging.FileHandler('monitor.log')
fh.setLevel(logging.INFO)

# this is for setting the CMD
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
ch.setFormatter(formatter)

logger.addHandler(fh)
logger.addHandler(ch)
