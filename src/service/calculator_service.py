"""
Calculator Service
비즈니스 로직을 담당하는 서비스 계층

SOLID 원칙 적용:
- SRP: 계산 로직만 담당
- OCP: 새로운 연산 추가 시 서비스 코드 수정 불필요
- DIP: Operation 추상화에 의존

Code Smell 제거:
- Switch Statement 제거 (if-elif 체인 → Strategy Pattern)
- Long Method 제거 (책임 분리)
"""

from typing import Union, Dict, Optional
from ..domain.operation import Operation
from ..domain.operations import Addition, Subtraction, Multiplication, Division
from ..domain.calculation_result import CalculationResult


class CalculatorService:
    """
    계산기 서비스 클래스 - 비즈니스 로직 담당
    
    Strategy Pattern을 사용하여 연산을 관리합니다.
    새로운 연산을 추가할 때 기존 코드를 수정할 필요가 없습니다 (OCP).
    """
    
    def __init__(self):
        """연산 전략들을 초기화하고 등록"""
        self._operations: Dict[str, Operation] = {}
        self._register_default_operations()
    
    def _register_default_operations(self):
        """
        기본 연산들을 등록합니다.
        
        Note:
            새로운 연산을 추가하려면 이 메서드에 등록만 하면 됩니다.
            calculate() 메서드를 수정할 필요가 없습니다 (OCP 준수).
        """
        operations = [
            Addition(),
            Subtraction(),
            Multiplication(),
            Division()
        ]
        
        for operation in operations:
            self.register_operation(operation)
    
    def register_operation(self, operation: Operation):
        """
        새로운 연산을 등록합니다 (OCP 적용).
        
        Args:
            operation: 등록할 연산 객체
            
        Example:
            >>> service = CalculatorService()
            >>> service.register_operation(Modulo())  # 새 연산 추가
        """
        symbol = operation.get_symbol()
        self._operations[symbol] = operation
    
    def get_available_operators(self) -> list[str]:
        """
        사용 가능한 연산자 목록을 반환합니다.
        
        Returns:
            연산자 기호 리스트
            
        Example:
            >>> service = CalculatorService()
            >>> service.get_available_operators()
            ['+', '-', '*', '/']
        """
        return list(self._operations.keys())
    
    def calculate(self, operand1: Union[int, float], operator: str, 
                  operand2: Union[int, float]) -> CalculationResult:
        """
        계산을 수행하고 결과를 반환합니다.
        
        Strategy Pattern을 사용하여 if-elif 체인을 제거했습니다.
        연산자에 해당하는 Operation 객체를 찾아 execute()를 호출합니다.
        
        Args:
            operand1: 첫 번째 피연산자
            operator: 연산자 기호
            operand2: 두 번째 피연산자
            
        Returns:
            CalculationResult 객체 (성공 또는 실패)
            
        Example:
            >>> service = CalculatorService()
            >>> result = service.calculate(3, '+', 5)
            >>> result.result
            8
            >>> result.is_success
            True
        """
        # 연산자 유효성 검증
        if operator not in self._operations:
            return CalculationResult.create_failure(
                operand1, operand2, operator,
                f"지원하지 않는 연산자입니다: {operator}"
            )
        
        # 연산 수행 (Strategy Pattern)
        try:
            operation = self._operations[operator]
            result = operation.execute(operand1, operand2)
            return CalculationResult.create_success(operand1, operand2, operator, result)
        except ArithmeticError as e:
            return CalculationResult.create_failure(
                operand1, operand2, operator,
                str(e)
            )
        except Exception as e:
            return CalculationResult.create_failure(
                operand1, operand2, operator,
                f"계산 중 오류가 발생했습니다: {str(e)}"
            )
    
    def get_operation_name(self, operator: str) -> Optional[str]:
        """
        연산자에 해당하는 연산 이름을 반환합니다.
        
        Args:
            operator: 연산자 기호
            
        Returns:
            연산 이름 또는 None
            
        Example:
            >>> service = CalculatorService()
            >>> service.get_operation_name('+')
            '덧셈'
        """
        if operator in self._operations:
            return self._operations[operator].get_name()
        return None
    
    def is_valid_operator(self, operator: str) -> bool:
        """
        연산자가 유효한지 검증합니다.
        
        Args:
            operator: 검증할 연산자 기호
            
        Returns:
            유효하면 True, 아니면 False
            
        Example:
            >>> service = CalculatorService()
            >>> service.is_valid_operator('+')
            True
            >>> service.is_valid_operator('%')
            False
        """
        return operator in self._operations
