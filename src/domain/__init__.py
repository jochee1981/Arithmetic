"""
Domain 패키지
도메인 모델 계층

이 계층은 비즈니스 로직의 핵심 개념을 포함합니다:
- Operation: 연산 추상 인터페이스
- 구체적 연산 클래스들 (Addition, Subtraction, Multiplication, Division)
- CalculationResult: 계산 결과 Value Object
"""

from .operation import Operation
from .operations import Addition, Subtraction, Multiplication, Division
from .calculation_result import CalculationResult

__all__ = [
    'Operation',
    'Addition',
    'Subtraction',
    'Multiplication',
    'Division',
    'CalculationResult'
]
