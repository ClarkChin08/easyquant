import easyquotation
import os
import easyquant
from easyquant import DefaultQuotationEngine, DefaultLogHandler, PushBaseEngine

print('easyquant 测试 DEMO')

broker = 'ht_client'

need_data = 'ht.json'
need_data = os.path.join(os.getcwd(), need_data)
print("client config file is {}".format(need_data))
quotation_engine = DefaultQuotationEngine

quotation_engine.PushInterval = 1

log_type = 'stdout'

log_filepath = ''

log_handler = DefaultLogHandler(name='测试', log_type=log_type, filepath=log_filepath)

m = easyquant.MainEngine(broker, need_data, quotation_engines=[quotation_engine], log_handler=log_handler)
# m.is_watch_strategy = True  # 策略文件出现改动时,自动重载,不建议在生产环境下使用
m.load_strategy()
m.start()
