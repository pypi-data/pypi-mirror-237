import functools

import pydash.objects

from cardtool.card.cipher import encrypt_card
from cardtool.card.data import CardGen
from cardtool.card.dump import CardDumper
from cardtool.card.model import CardConfig, Key
from cardtool.card.pin import generate_pin_block
from cardtool.dukpt.cipher import DUKPTCipher
from cardtool.dukpt.key import generate_key
from cardtool.util.serialize import new_serializer


def bootstrap(config: CardConfig, fmt: str) -> CardDumper:
    data_keys: Key = pydash.objects.get(config.key, "data")
    pin_keys: Key = pydash.objects.get(config.key, "pin")
    data_cipher = DUKPTCipher(
        bdk=data_keys.bdk, ksn=data_keys.ksn, derive_key=generate_key
    )
    pin_cipher = DUKPTCipher(
        bdk=pin_keys.bdk, ksn=pin_keys.ksn, derive_key=generate_key
    )
    callable_cipher = functools.partial(encrypt_card, data_cipher, pin_cipher)
    card_generator = CardGen(generate_pin_block).generate_data
    callable_generator = functools.partial(
        card_generator, config.terminal, config.transaction
    )
    serializer = new_serializer(fmt)
    return CardDumper(callable_cipher, callable_generator, serializer)
