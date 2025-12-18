"""
나눗셈 연산 구현
Strategy Pattern의 구체적 전략 클래스
"""

from typing import Union
from ..operation import Operation


class Division(Operation):
    """
    나눗셈 연산을 수행하는 클래스 (정수 나눗셈)
    
    SOLID 원칙:
    - SRP: 나눗셈 연산과 예외 처리만 담당
    - OCP: Operation 인터페이스를 구현하여 확장
    """
    
    def execute(self, a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
        """
        두 수의 정수 나눗셈을 계산합니다 (버림 처리).
        
        Args:
            a: 첫 번째 숫자 (피제수)
            b: 두 번째 숫자 (제수)
            
        Returns:
            정수 나눗셈 결과 (버림)
            
        Raises:
            ArithmeticError: 제수가 0일 때 발생
            
        Examples:
            >>> div = Division()
            >>> div.execute(5, 2)
            2
            >>> div.execute(-10, 2)
            -5
            >>> div.execute(0, 0)
            Traceback (most recent call last):
                ...
            ArithmeticError: 0으로 나눌 수 없습니다
        """
        if b == 0:
            raise ArithmeticError("0으로 나눌 수 없습니다")
        return a // b
    
    def get_symbol(self) -> str:
        """연산자 기호 반환"""
        return '/'
    
    def get_name(self) -> str:
        """연산 이름 반환"""
        return '나눗셈'
