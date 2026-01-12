"""
Service Layer 테스트
CalculatorService 클래스 테스트
"""

import pytest
from src.service import CalculatorService
from src.domain import CalculationResult


class TestCalculatorService:
    """CalculatorService 테스트"""
    
    @pytest.fixture
    def service(self):
        """테스트용 CalculatorService 인스턴스"""
        return CalculatorService()
    
    # 기본 연산 테스트
    def test_addition(self, service):
        """덧셈 테스트"""
        result = service.calculate(3, '+', 5)
        assert result.is_success is True
        assert result.result == 8
        assert result.operand1 == 3
        assert result.operand2 == 5
        assert result.operator == '+'
    
    def test_subtraction(self, service):
        """뺄셈 테스트"""
        result = service.calculate(10, '-', 3)
        assert result.is_success is True
        assert result.result == 7
    
    def test_multiplication(self, service):
        """곱셈 테스트"""
        result = service.calculate(4, '*', 5)
        assert result.is_success is True
        assert result.result == 20
    
    def test_division(self, service):
        """나눗셈 테스트"""
        result = service.calculate(10, '/', 3)
        assert result.is_success is True
        assert result.result == 3  # 정수 나눗셈
    
    # 예외 처리 테스트
    def test_division_by_zero(self, service):
        """0으로 나누기 예외 테스트"""
        result = service.calculate(5, '/', 0)
        assert result.is_success is False
        assert "0으로 나눌 수 없습니다" in result.error_message
    
    def test_invalid_operator(self, service):
        """잘못된 연산자 테스트"""
        result = service.calculate(5, '%', 2)
        assert result.is_success is False
        assert "지원하지 않는 연산자" in result.error_message
    
    # 연산자 관리 테스트
    def test_get_available_operators(self, service):
        """사용 가능한 연산자 목록 테스트"""
        operators = service.get_available_operators()
        assert '+' in operators
        assert '-' in operators
        assert '*' in operators
        assert '/' in operators
        assert len(operators) == 4
    
    def test_get_operation_name(self, service):
        """연산 이름 조회 테스트"""
        assert service.get_operation_name('+') == '덧셈'
        assert service.get_operation_name('-') == '뺄셈'
        assert service.get_operation_name('*') == '곱셈'
        assert service.get_operation_name('/') == '나눗셈'
        assert service.get_operation_name('%') is None
    
    def test_is_valid_operator(self, service):
        """연산자 유효성 검증 테스트"""
        assert service.is_valid_operator('+') is True
        assert service.is_valid_operator('-') is True
        assert service.is_valid_operator('*') is True
        assert service.is_valid_operator('/') is True
        assert service.is_valid_operator('%') is False
        assert service.is_valid_operator('**') is False
    
    # 기존 테스트 케이스와의 호환성 테스트
    def test_existing_test_cases(self, service):
        """기존 테스트 케이스 검증"""
        # 1 + 10 = 11
        result = service.calculate(1, '+', 10)
        assert result.is_success is True
        assert result.result == 11
        
        # 0 + 1 = 1
        result = service.calculate(0, '+', 1)
        assert result.is_success is True
        assert result.result == 1
        
        # -1 + (-10) = -11
        result = service.calculate(-1, '+', -10)
        assert result.is_success is True
        assert result.result == -11
        
        # 5 - 2 = 3
        result = service.calculate(5, '-', 2)
        assert result.is_success is True
        assert result.result == 3
        
        # -5 * -3 = 15
        result = service.calculate(-5, '*', -3)
        assert result.is_success is True
        assert result.result == 15
        
        # 0 * 10 = 0
        result = service.calculate(0, '*', 10)
        assert result.is_success is True
        assert result.result == 0
        
        # 5 / 2 = 2 (정수 나눗셈)
        result = service.calculate(5, '/', 2)
        assert result.is_success is True
        assert result.result == 2
        
        # -10 / 2 = -5
        result = service.calculate(-10, '/', 2)
        assert result.is_success is True
        assert result.result == -5
        
        # 0 / 0 = 오류
        result = service.calculate(0, '/', 0)
        assert result.is_success is False
        assert "0으로 나눌 수 없습니다" in result.error_message
    
    def test_result_formatting(self, service):
        """결과 포맷팅 테스트"""
        result = service.calculate(3, '+', 5)
        assert result.format_expression() == "3 + 5 = 8"
        
        result = service.calculate(10, '/', 0)
        assert "오류" in result.format_expression()
    
    # OCP(Open-Closed Principle) 테스트
    def test_extensibility(self, service):
        """확장성 테스트 - 새로운 연산 추가"""
        from src.domain import Operation
        
        # 나머지 연산 추가 (확장 예제)
        class Modulo(Operation):
            def execute(self, a, b):
                if b == 0:
                    raise ArithmeticError("0으로 나눌 수 없습니다")
                return a % b
            def get_symbol(self):
                return '%'
            def get_name(self):
                return '나머지'
        
        # 새 연산 등록
        service.register_operation(Modulo())
        
        # 등록된 연산 사용
        result = service.calculate(10, '%', 3)
        assert result.is_success is True
        assert result.result == 1
        
        # 연산자 목록에 추가되었는지 확인
        assert '%' in service.get_available_operators()
        assert service.get_operation_name('%') == '나머지'


class TestCalculatorServiceIntegration:
    """CalculatorService 통합 테스트"""
    
    def test_complex_calculation_scenario(self):
        """복잡한 계산 시나리오 테스트"""
        service = CalculatorService()
        
        # 시나리오: (5 + 3) * 2 / 4
        # 단계별 계산
        result1 = service.calculate(5, '+', 3)  # 8
        assert result1.is_success is True
        
        result2 = service.calculate(result1.result, '*', 2)  # 16
        assert result2.is_success is True
        
        result3 = service.calculate(result2.result, '/', 4)  # 4
        assert result3.is_success is True
        assert result3.result == 4
    
    def test_error_recovery(self):
        """오류 복구 테스트"""
        service = CalculatorService()
        
        # 오류 발생
        result1 = service.calculate(10, '/', 0)
        assert result1.is_success is False
        
        # 이후 정상 계산 가능
        result2 = service.calculate(10, '/', 2)
        assert result2.is_success is True
        assert result2.result == 5
