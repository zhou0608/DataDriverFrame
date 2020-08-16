#coding=utf-8
import  logging,os
log_path=os.path.dirname(os.path.dirname(__file__))
log_format='%(asctime)s - %(levelname)s - %(filename)s -%(lineno)s- %(message)s'
date_format='%Y/%m/%d/%H:%M:%S'
logging.basicConfig(filename=log_path+'/log/FrameWork.log',level=logging.INFO,format=log_format,datefmt=date_format)
logger=logging.getLogger()

logger.debug('写入内容')