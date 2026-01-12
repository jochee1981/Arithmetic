"""
뺄셈 연산 구현
Strategy Pattern의 구체적 전략 클래스
"""

from typing import Union
from ..operation import Operation


class Subtraction(Operation):
    """
    뺄셈 연산을 수행하는 클래스
    
    SOLID 원칙:
    - SRP: 뺄셈 연산만 담당
    - OCP: Operation 인터페이스를 구현하여 확장
    """
    
    def execute(self, a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
        """
        두 수의 차를 계산합니다.
        
        Args:
            a: 첫 번째 숫자 (피감수)
            b: 두 번째 숫자 (감수)
            
        Returns:
            두 수의 차
            
        Examples:
            >>> sub = Subtraction()
            >>> sub.execute(5, 2)
            3
            >>> sub.execute(10, 15)
            -5
        """
        return a - b
    
    def get_symbol(self) -> str:
        """연산자 기호 반환"""
        return '-'
    
    def get_name(self) -> str:
        """연산 이름 반환"""
        return '뺄셈'
