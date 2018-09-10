import gc

from trezor import log
from trezor.messages import MessageType


async def sign_tx(ctx, msg):
    state = None

    while True:
        res, state = await sign_tx_step(ctx, msg, state)
        if msg.final_msg:
            break
        msg = await ctx.call(res, MessageType.MoneroTransactionSignRequest)

    return res


async def sign_tx_step(ctx, msg, state):
    gc.threshold(gc.mem_free() // 4 + gc.mem_alloc())
    if __debug__:
        log.debug(
            __name__,
            "f: %s a: %s thr: %s",
            gc.mem_free(),
            gc.mem_alloc(),
            gc.mem_free() // 4 + gc.mem_alloc(),
        )
        log.debug(__name__, "s: %s", state)
    gc.collect()

    from apps.monero.protocol.tsx_sign import TsxSigner

    if __debug__:
        log.debug(__name__, "f: %s a: %s", gc.mem_free(), gc.mem_alloc())
    gc.collect()

    signer = TsxSigner()
    await signer.wake_up(ctx, state, msg)
    del state

    res = await signer.sign(msg)
    gc.collect()

    if not await signer.should_purge():
        state = await signer.state_save()

    return res, state
