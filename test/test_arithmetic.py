"""
TC-AO-001: Arithmetic Operations Test
사칙연산 정확도 테스트
"""

import pytest
from src.arithmetic import Arithmetic


class TestArithmeticOperations:
    """기본 사칙연산 테스트"""
    
    def test_add_1_plus_10_should_return_11(self):
        """1 + 10 = 11"""
        arithmetic = Arithmetic()
        result = arithmetic.add(1, 10)
        assert result == 11
    
    def test_add_0_plus_1_should_return_1(self):
        """0 + 1 = 1"""
        arithmetic = Arithmetic()
        result = arithmetic.add(0, 1)
        assert result == 1
    
    def test_add_negative1_plus_negative10_should_return_negative11(self):
        """-1 + (-10) = -11"""
        arithmetic = Arithmetic()
        result = arithmetic.add(-1, -10)
        assert result == -11
    
    def test_subtract_5_minus_2_should_return_3(self):
        """5 - 2 = 3"""
        arithmetic = Arithmetic()
        result = arithmetic.subtract(5, 2)
        assert result == 3
    
    def test_multiply_negative5_by_negative3_should_return_15(self):
        """-5 * -3 = 15"""
        arithmetic = Arithmetic()
        result = arithmetic.multiply(-5, -3)
        assert result == 15
    
    def test_multiply_0_by_10_should_return_0(self):
        """0 * 10 = 0"""
        arithmetic = Arithmetic()
        result = arithmetic.multiply(0, 10)
        assert result == 0
    
    def test_divide_5_by_2_should_return_2(self):
        """5 / 2 = 2 (정수 나눗셈)"""
        arithmetic = Arithmetic()
        result = arithmetic.divide(5, 2)
        assert result == 2
    
    def test_divide_negative10_by_2_should_return_negative5(self):
        """-10 / 2 = -5"""
        arithmetic = Arithmetic()
        result = arithmetic.divide(-10, 2)
        assert result == -5
    
    def test_quotient_5_divide_2_should_return_2_5(self):
        """5 ÷ 2 = 2.5 (몫 계산, 소수점)"""
        arithmetic = Arithmetic()
        result = arithmetic.quotient(5, 2)
        assert result == 2.5
    
    def test_divide_0_by_0_should_throw_arithmetic_exception(self):
        """0 / 0 → ArithmeticException 예외 발생"""
        arithmetic = Arithmetic()
        with pytest.raises(ArithmeticError):
            arithmetic.divide(0, 0)

