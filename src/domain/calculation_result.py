"""
CalculationResult Value Object
계산 결과를 불변 객체로 캡슐화

SOLID 원칙:
- SRP: 계산 결과 데이터만 담당
- OCP: 새로운 결과 형식 추가 시 확장 가능
"""

from typing import Union
from dataclasses import dataclass


@dataclass(frozen=True)
class CalculationResult:
    """
    계산 결과를 담는 불변 Value Object
    
    Attributes:
        operand1: 첫 번째 피연산자
        operand2: 두 번째 피연산자
        operator: 연산자 기호
        result: 연산 결과
        is_success: 성공 여부
        error_message: 오류 메시지 (실패 시)
    """
    
    operand1: Union[int, float]
    operand2: Union[int, float]
    operator: str
    result: Union[int, float]
    is_success: bool = True
    error_message: str = ""
    
    def format_expression(self) -> str:
        """
        수식을 문자열로 포맷팅합니다.
        
        Returns:
            포맷팅된 수식 문자열
            
        Examples:
            >>> result = CalculationResult(3, 5, '+', 8)
            >>> result.format_expression()
            '3 + 5 = 8'
        """
        if self.is_success:
            return f"{self.operand1} {self.operator} {self.operand2} = {self.result}"
        else:
            return f"{self.operand1} {self.operator} {self.operand2} = 오류"
    
    def __str__(self) -> str:
        """문자열 표현"""
        return self.format_expression()
    
    @classmethod
    def create_success(cls, operand1: Union[int, float], operand2: Union[int, float],
                      operator: str, result: Union[int, float]) -> 'CalculationResult':
        """
        성공 결과를 생성하는 팩토리 메서드
        
        Args:
            operand1: 첫 번째 피연산자
            operand2: 두 번째 피연산자
            operator: 연산자 기호
            result: 연산 결과
            
        Returns:
            성공 상태의 CalculationResult
        """
        return cls(operand1, operand2, operator, result, is_success=True, error_message="")
    
    @classmethod
    def create_failure(cls, operand1: Union[int, float], operand2: Union[int, float],
                      operator: str, error_message: str) -> 'CalculationResult':
        """
        실패 결과를 생성하는 팩토리 메서드
        
        Args:
            operand1: 첫 번째 피연산자
            operand2: 두 번째 피연산자
            operator: 연산자 기호
            error_message: 오류 메시지
            
        Returns:
            실패 상태의 CalculationResult
        """
        return cls(operand1, operand2, operator, 0, is_success=False, error_message=error_message)
