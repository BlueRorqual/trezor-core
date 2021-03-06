# Automatically generated by pb2py
# fmt: off
import protobuf as p

from .StellarAssetType import StellarAssetType


class StellarManageOfferOp(p.MessageType):
    MESSAGE_WIRE_TYPE = 213
    FIELDS = {
        1: ('source_account', p.UnicodeType, 0),
        2: ('selling_asset', StellarAssetType, 0),
        3: ('buying_asset', StellarAssetType, 0),
        4: ('amount', p.SVarintType, 0),
        5: ('price_n', p.UVarintType, 0),
        6: ('price_d', p.UVarintType, 0),
        7: ('offer_id', p.UVarintType, 0),
    }

    def __init__(
        self,
        source_account: str = None,
        selling_asset: StellarAssetType = None,
        buying_asset: StellarAssetType = None,
        amount: int = None,
        price_n: int = None,
        price_d: int = None,
        offer_id: int = None,
    ) -> None:
        self.source_account = source_account
        self.selling_asset = selling_asset
        self.buying_asset = buying_asset
        self.amount = amount
        self.price_n = price_n
        self.price_d = price_d
        self.offer_id = offer_id
