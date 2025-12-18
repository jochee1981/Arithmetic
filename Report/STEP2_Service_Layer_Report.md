# STEP 2 완료: Service Layer 리팩토링 보고서

## 📋 개요

기존 콘솔 프로그램의 `calculate()` 함수를 Service Layer로 리팩토링했습니다.

---

## 🔴 리팩토링 전: Code Smell 분석

### 1. Switch Statement (if-elif 체인)

**main.py의 calculate() 함수:**

```python
def calculate(arithmetic, a, operator, b):
    """연산자를 기반으로 계산을 수행하는 함수"""
    if operator == '+':
        return arithmetic.add(a, b)
    elif operator == '-':
        return arithmetic.subtract(a, b)
    elif operator == '*':
        return arithmetic.multiply(a, b)
    elif operator == '/' or operator == '÷':
        try:
            return arithmetic.divide(a, b)
        except ArithmeticError as e:
            raise e
    else:
        raise ValueError(f"지원하지 않는 연산자: {operator}")
```

**문제점:**
- ❌ 새로운 연산자 추가 시 함수 수정 필요 (OCP 위반)
- ❌ if-elif 체인이 길어질수록 유지보수 어려움
- ❌ 연산 로직이 분산됨 (Feature Envy)

---

## 🟢 리팩토링 후: Strategy Pattern 적용

### Calculator Service 클래스

```python
class CalculatorService:
    def __init__(self):
        self._operations: Dict[str, Operation] = {}
        self._register_default_operations()
    
    def _register_default_operations(self):
        operations = [
            Addition(),
            Subtraction(),
            Multiplication(),
            Division()
        ]
        for operation in operations:
            self.register_operation(operation)
    
    def calculate(self, operand1, operator, operand2):
        # 연산자 검증
        if operator not in self._operations:
            return CalculationResult.create_failure(...)
        
        # Strategy Pattern: 연산 수행
        try:
            operation = self._operations[operator]
            result = operation.execute(operand1, operand2)
            return CalculationResult.create_success(...)
        except ArithmeticError as e:
            return CalculationResult.create_failure(...)
```

**개선 사항:**
- ✅ if-elif 체인 완전 제거
- ✅ 새로운 연산 추가 시 `register_operation()`만 호출 (OCP 준수)
- ✅ 각 연산이 독립적인 클래스로 캡슐화
- ✅ 예외 처리를 CalculationResult로 통합

---

## 🎯 SOLID 원칙 적용

### 1. SRP (Single Responsibility Principle) ✅

**CalculatorService의 단일 책임:**
- 연산 등록 및 관리
- 계산 실행 및 결과 반환

**기존 문제:**
- `main()` 함수가 입력, 계산, 출력 모두 담당

### 2. OCP (Open-Closed Principle) ✅

**새로운 연산 추가 예제:**

```python
# 나머지 연산 추가
class Modulo(Operation):
    def execute(self, a, b):
        if b == 0:
            raise ArithmeticError("0으로 나눌 수 없습니다")
        return a % b
    def get_symbol(self):
        return '%'
    def get_name(self):
        return '나머지'

# 서비스에 등록만 하면 끝!
service.register_operation(Modulo())

# 즉시 사용 가능
result = service.calculate(10, '%', 3)  # 1
```

**기존 방식:**
```python
# calculate() 함수를 수정해야 함
def calculate(arithmetic, a, operator, b):
    if operator == '+':
        ...
    elif operator == '%':  # 새로 추가
        return a % b       # 기존 코드 수정 필요!
```

### 3. DIP (Dependency Inversion Principle) ✅

```python
# CalculatorService는 구체적인 연산이 아닌
# Operation 추상화에 의존
self._operations: Dict[str, Operation] = {}
```

---

## 📊 테스트 결과

### 테스트 커버리지

```
test_service.py::TestCalculatorService
  ✅ test_addition
  ✅ test_subtraction
  ✅ test_multiplication
  ✅ test_division
  ✅ test_division_by_zero
  ✅ test_invalid_operator
  ✅ test_get_available_operators
  ✅ test_get_operation_name
  ✅ test_is_valid_operator
  ✅ test_existing_test_cases (기존 테스트 케이스 호환성)
  ✅ test_result_formatting
  ✅ test_extensibility (OCP 검증)

test_service.py::TestCalculatorServiceIntegration
  ✅ test_complex_calculation_scenario
  ✅ test_error_recovery

총 14개 테스트 모두 통과 ✅
```

### 기존 테스트 케이스 호환성

모든 기존 테스트 케이스가 Service Layer에서도 동일하게 동작:

| 테스트 케이스 | 기존 | Service Layer |
|--------------|------|---------------|
| 1 + 10 = 11 | ✅ | ✅ |
| 0 + 1 = 1 | ✅ | ✅ |
| -1 + (-10) = -11 | ✅ | ✅ |
| 5 - 2 = 3 | ✅ | ✅ |
| -5 * -3 = 15 | ✅ | ✅ |
| 0 * 10 = 0 | ✅ | ✅ |
| 5 / 2 = 2 | ✅ | ✅ |
| -10 / 2 = -5 | ✅ | ✅ |
| 0 / 0 = 오류 | ✅ | ✅ |

---

## 🚀 주요 개선 사항 요약

### Code Smell 제거

| Code Smell | 개선 전 | 개선 후 |
|-----------|---------|---------|
| Switch Statement | if-elif 체인 | Strategy Pattern |
| Long Method | main()이 모든 것 처리 | 계층별 분리 |
| Feature Envy | 연산 로직 분산 | 캡슐화 |
| Primitive Obsession | 문자열 연산자 | Operation 객체 |

### 확장성

```python
# 기존: 함수 수정 필요
def calculate(...):
    if operator == '+':
        ...
    elif operator == '%':  # 추가 시 여기 수정
        ...

# 개선: 클래스 추가만으로 확장
service.register_operation(NewOperation())  # 끝!
```

### 테스트 용이성

```python
# 기존: 전체 main() 함수를 테스트해야 함
# 개선: Service만 독립적으로 테스트 가능

def test_addition(service):
    result = service.calculate(3, '+', 5)
    assert result.result == 8
```

---

## 📈 다음 단계

**STEP 3: GUI 프레젠테이션 계층**
- PyQt6로 계산기 UI 구현
- MVP 패턴 적용
- CalculatorService를 Model로 사용

---

**작성일**: 2025년 12월 18일  
**버전**: 1.0.0
