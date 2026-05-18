def create_payment_intent(amount: int, currency: str = "USD") -> dict:
    """Create a fake payment intent (demo only)."""
    return {"id": "pi_demo", "amount": amount, "currency": currency, "status": "requires_confirmation"}
