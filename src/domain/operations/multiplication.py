"""
곱셈 연산 구현
Strategy Pattern의 구체적 전략 클래스
"""

from typing import Union
from ..operation import Operation


class Multiplication(Operation):
    """
    곱셈 연산을 수행하는 클래스
    
    SOLID 원칙:
    - SRP: 곱셈 연산만 담당
    - OCP: Operation 인터페이스를 구현하여 확장
    """
    
    def execute(self, a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
        """
        두 수의 곱을 계산합니다.
        
        Args:
            a: 첫 번째 숫자
            b: 두 번째 숫자
            
        Returns:
            두 수의 곱
            
        Examples:
            >>> mul = Multiplication()
            >>> mul.execute(-5, -3)
            15
            >>> mul.execute(0, 10)
            0
        """
        return a * b
    
    def get_symbol(self) -> str:
        """연산자 기호 반환"""
        return '*'
    
    def get_name(self) -> str:
        """연산 이름 반환"""
        return '곱셈'
