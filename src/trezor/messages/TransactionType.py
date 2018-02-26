# Automatically generated by pb2py
import protobuf as p
from .TxInputType import TxInputType
from .TxOutputBinType import TxOutputBinType
from .TxOutputType import TxOutputType


class TransactionType(p.MessageType):
    FIELDS = {
        1: ('version', p.UVarintType, 0),
        2: ('inputs', TxInputType, p.FLAG_REPEATED),
        3: ('bin_outputs', TxOutputBinType, p.FLAG_REPEATED),
        4: ('lock_time', p.UVarintType, 0),
        5: ('outputs', TxOutputType, p.FLAG_REPEATED),
        6: ('inputs_cnt', p.UVarintType, 0),
        7: ('outputs_cnt', p.UVarintType, 0),
        8: ('extra_data', p.BytesType, 0),
        9: ('extra_data_len', p.UVarintType, 0),
        10: ('decred_expiry', p.UVarintType, 0),
    }

    def __init__(
        self,
        version: int = None,
        inputs: list = None,
        bin_outputs: list = None,
        lock_time: int = None,
        outputs: list = None,
        inputs_cnt: int = None,
        outputs_cnt: int = None,
        extra_data: bytes = None,
        extra_data_len: int = None,
        decred_expiry: int = None,
        **kwargs,
    ):
        self.version = version
        self.inputs = [] if inputs is None else inputs
        self.bin_outputs = [] if bin_outputs is None else bin_outputs
        self.lock_time = lock_time
        self.outputs = [] if outputs is None else outputs
        self.inputs_cnt = inputs_cnt
        self.outputs_cnt = outputs_cnt
        self.extra_data = extra_data
        self.extra_data_len = extra_data_len
        self.decred_expiry = decred_expiry
        p.MessageType.__init__(self, **kwargs)
