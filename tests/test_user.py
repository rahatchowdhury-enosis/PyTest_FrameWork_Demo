import pytest


@pytest.mark.smoke
class TestUserSmoke:

    # --------------------------
    # Fund and Fee Tests
    # --------------------------

    # critical path: adding valid funds
    def test_add_funds(self, sample_user):
        sample_user.add_funds(50)
        assert sample_user.balance == 150


    # critical path: paying valid fee
    def test_pay_fee(self, sample_user):
        sample_user.pay_fee(30)
        assert sample_user.balance == 70



@pytest.mark.regression
class TestUserRegression:

    # --------------------------
    # Fund and Fee Tests
    # --------------------------

    # negative case: adding invalid funds
    def test_add_invalid_funds(self, sample_user):
        with pytest.raises(ValueError):
            sample_user.add_funds(-10)

    # negative case: insufficient balance
    def test_pay_fee_insufficient(self, sample_user):
        with pytest.raises(ValueError):
            sample_user.pay_fee(1000)

    # --------------------------
    # Additional edge / regression tests
    # --------------------------


    def test_add_funds_zero(self, sample_user):
        """Adding 0 funds should raise ValueError"""
        with pytest.raises(ValueError, match="Deposit must be positive"):
            sample_user.add_funds(0)


    def test_pay_fee_exact_balance(self, sample_user):
        """Paying a fee equal to current balance should set balance to 0"""
        sample_user.pay_fee(sample_user.balance)
        assert sample_user.balance == 0


    def test_multiple_adds_and_fees(self, sample_user):
        """Multiple adds and fee payments combined"""
        sample_user.add_funds(50)
        sample_user.pay_fee(30)
        sample_user.add_funds(20)
        sample_user.pay_fee(25)
        assert sample_user.balance == 115  # 100 +50 -30 +20 -25
