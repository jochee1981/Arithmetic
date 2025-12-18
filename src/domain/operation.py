"""
Operation 추상 클래스
Strategy Pattern을 위한 기본 인터페이스

SOLID 원칙:
- SRP: 각 연산은 하나의 책임만 가짐
- OCP: 새로운 연산 추가 시 기존 코드 수정 없이 확장 가능
- LSP: 모든 구체적 연산은 Operation을 대체 가능
- ISP: 연산에 필요한 최소한의 인터페이스만 제공
- DIP: 상위 모듈은 추상화에 의존
"""

from abc import ABC, abstractmethod
from typing import Union


class Operation(ABC):
    """연산을 수행하는 추상 클래스 (Strategy Pattern)"""
    
    @abstractmethod
    def execute(self, a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
        """
        연산을 수행합니다.
        
        Args:
            a: 첫 번째 피연산자
            b: 두 번째 피연산자
            
        Returns:
            연산 결과
            
        Raises:
            ArithmeticError: 연산 중 오류 발생 시
        """
        pass
    
    @abstractmethod
    def get_symbol(self) -> str:
        """
        연산자 기호를 반환합니다.
        
        Returns:
            연산자 기호 (예: '+', '-', '*', '/')
        """
        pass
    
    @abstractmethod
    def get_name(self) -> str:
        """
        연산 이름을 반환합니다.
        
        Returns:
            연산 이름 (예: '덧셈', '뺄셈')
        """
        pass
