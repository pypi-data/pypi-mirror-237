
import hashlib
from typing import Dict, Optional
import datetime
import json
from yfpay import http

from yfpay.models import CancelResult, Env, GoodsDetail, PayMethod, PayResult, PayType


class PayClient():

    def __init__(self, inst_no: str, mch_no: str, mch_key: str, 
                 appid: Optional[str] = None, env=Env.PRODUCTION, logger=None):
        '''
        param inst_no: 机构号
        param mch_no: 商户号
        param mch_key: 商户密钥
        param pay_type: weichat  alipay
        '''
        self.inst_no = inst_no
        self.mch_no = mch_no
        self.mch_key = mch_key
        self.appid = appid
        self.logger = logger
        self.env = env
        self.end_point = 'https://open.gdyfsk.com/yfpay' if env == Env.PRODUCTION else 'https://test.gdyfsk.com/api/yfpay'

    def sign(self, data: Dict):
        sorted_data = [(k, str(data[k]) if isinstance(data[k], int) else data[k])
                       for k in sorted(data.keys())]
        s = "&".join("=".join(kv) for kv in sorted_data if kv[1]!=None)
        s += "&key={0}".format(self.mch_key)
        return hashlib.md5(s.encode("utf-8")).hexdigest()

    def dump_json(self, data):
        return json.dumps(data, ensure_ascii=False)
    
    def fix_data(self, data:Dict):
        data = {k: v for k, v in data.items() if v != None}
        data['sign'] = self.sign(data)
        return data

    async def async_pay(self,
                        out_trade_no: str,
                        total_amount: int,
                        open_id: str,
                        description: str,
                        pay_type: PayType,
                        pay_method: PayMethod,
                        notify_url: Optional[str] = None,
                        pay_time: Optional[str] = None,
                        goods_detail: Optional[GoodsDetail] = None,
                        reqip: Optional[str] = None,
                        attach: Optional[str] = None,
                        ) -> PayResult:
        '''
        param out_trade_no: 商户订单号(在商户系统内唯一)
        param total_amount: 订单金额，单位为分
        param open_id: 用户标识（微信openid/支付宝userid）
        param description: 订单描述
        param pay_type: 支付类型
        param pay_method: 支付方式：JSAPI,小程序
        param notify_url: 回调地址（以http或https开头的完整url地址）
        param pay_time: 支付时间(yyyyMMddHHmmss)
        '''
        data = {
            "inst_no": self.inst_no,
            "mch_no": self.mch_no,
            "pay_type": pay_type.value,
            "pay_trace_no": out_trade_no,
            "pay_time": pay_time if pay_time else datetime.datetime.now().strftime('%Y%m%d%H%M%S'),
            "total_amount": str(total_amount),
            "notify_url": notify_url,
            "open_id": open_id,
            "order_body": description,
            "appid": self.appid,
            "attach": attach,
            "goods_detail": goods_detail,
            "reqip": reqip,
        }

        data = self.fix_data(data)
        data = self.dump_json(data)
        url = self.end_point + '/v3/minipay'
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
        }
        result = await http.post(url, data=data, headers=headers)
        if result.status_code != 200:
            raise Exception('支付失败')
        return PayResult.model_validate(result.json())
        
    async def async_cancel(self,refund_trace_no:str,refund_fee:int,out_trade_no:str,trade_no:str=None,pay_time=None):
        '''
        params refund_trace_no:请求流水号（系统方退款订单号）
        params refund_fee:退款金额，单位：分
        params out_trade_no: 商户订单号(在商户系统内唯一)
        params trade_no: 支付请求流水号（与支付订单号二选其一必传）
        '''
        url = self.end_point + '/v3/refundorder'
        data = {
            "inst_no": self.inst_no,
            "mch_no": self.mch_no,
            "refund_trace_no": refund_trace_no,
            "refund_fee": refund_fee,
            "trade_no": trade_no,
            "pay_trace_no": out_trade_no,
            "pay_time": pay_time if pay_time else datetime.datetime.now().strftime('%Y%m%d%H%M%S'),
        }
        data = self.fix_data(data)
        data = self.dump_json(data)
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
        }
        result = await http.post(url, data=data, headers=headers)
        if result.status_code != 200:
            raise Exception('請求失败')
        return CancelResult.model_validate(result.json())
