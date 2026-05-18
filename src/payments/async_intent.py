async def create_payment_intent_async(amount, currency='USD'):
    return {'id': 'pi_async_demo', 'amount': amount, 'currency': currency}

