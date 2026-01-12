"""
Domain Layer 테스트
Operation 클래스들과 CalculationResult 테스트
"""

import pytest
from src.domain import (
    Operation,
    Addition,
    Subtraction,
    Multiplication,
    Division,
    CalculationResult
)


class TestOperations:
    """연산 클래스들 테스트"""
    
    def test_addition_execute(self):
        """덧셈 연산 테스트"""
        add = Addition()
        assert add.execute(1, 10) == 11
        assert add.execute(0, 1) == 1
        assert add.execute(-1, -10) == -11
    
    def test_addition_metadata(self):
        """덧셈 메타데이터 테스트"""
        add = Addition()
        assert add.get_symbol() == '+'
        assert add.get_name() == '덧셈'
    
    def test_subtraction_execute(self):
        """뺄셈 연산 테스트"""
        sub = Subtraction()
        assert sub.execute(5, 2) == 3
        assert sub.execute(10, 15) == -5
    
    def test_subtraction_metadata(self):
        """뺄셈 메타데이터 테스트"""
        sub = Subtraction()
        assert sub.get_symbol() == '-'
        assert sub.get_name() == '뺄셈'
    
    def test_multiplication_execute(self):
        """곱셈 연산 테스트"""
        mul = Multiplication()
        assert mul.execute(-5, -3) == 15
        assert mul.execute(0, 10) == 0
    
    def test_multiplication_metadata(self):
        """곱셈 메타데이터 테스트"""
        mul = Multiplication()
        assert mul.get_symbol() == '*'
        assert mul.get_name() == '곱셈'
    
    def test_division_execute(self):
        """나눗셈 연산 테스트"""
        div = Division()
        assert div.execute(5, 2) == 2
        assert div.execute(-10, 2) == -5
    
    def test_division_by_zero(self):
        """0으로 나누기 예외 테스트"""
        div = Division()
        with pytest.raises(ArithmeticError, match="0으로 나눌 수 없습니다"):
            div.execute(0, 0)
    
    def test_division_metadata(self):
        """나눗셈 메타데이터 테스트"""
        div = Division()
        assert div.get_symbol() == '/'
        assert div.get_name() == '나눗셈'


class TestCalculationResult:
    """CalculationResult Value Object 테스트"""
    
    def test_success_result_creation(self):
        """성공 결과 생성 테스트"""
        result = CalculationResult.create_success(3, 5, '+', 8)
        assert result.operand1 == 3
        assert result.operand2 == 5
        assert result.operator == '+'
        assert result.result == 8
        assert result.is_success is True
        assert result.error_message == ""
    
    def test_failure_result_creation(self):
        """실패 결과 생성 테스트"""
        result = CalculationResult.create_failure(0, 0, '/', "0으로 나눌 수 없습니다")
        assert result.operand1 == 0
        assert result.operand2 == 0
        assert result.operator == '/'
        assert result.is_success is False
        assert result.error_message == "0으로 나눌 수 없습니다"
    
    def test_format_expression_success(self):
        """성공 결과 포맷팅 테스트"""
        result = CalculationResult.create_success(3, 5, '+', 8)
        assert result.format_expression() == "3 + 5 = 8"
    
    def test_format_expression_failure(self):
        """실패 결과 포맷팅 테스트"""
        result = CalculationResult.create_failure(0, 0, '/', "오류")
        assert result.format_expression() == "0 / 0 = 오류"
    
    def test_immutability(self):
        """불변성 테스트"""
        result = CalculationResult.create_success(3, 5, '+', 8)
        with pytest.raises(Exception):  # dataclass frozen=True로 인한 예외
            result.operand1 = 10
