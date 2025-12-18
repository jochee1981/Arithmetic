"""
Operations 패키지
모든 연산 클래스들을 export

Strategy Pattern:
각 연산을 독립적인 전략 객체로 구현하여
새로운 연산 추가 시 기존 코드 수정 없이 확장 가능
"""

from .addition import Addition
from .subtraction import Subtraction
from .multiplication import Multiplication
from .division import Division

__all__ = [
    'Addition',
    'Subtraction',
    'Multiplication',
    'Division'
]
