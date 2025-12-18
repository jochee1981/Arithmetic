# 테스트 케이스 요구사항 분류
_Exported on 12/17/2025 at 15:03:40 GMT+9 from Cursor (2.1.50)_

---

**User**

@Report/test_case.md 을 분석 해서 구현해야 할 기능을 기능/비기능 항목으로 구분해서 목록을 알려줘.

---

**Cursor**


`Report/test_case.md`를 분석해 기능/비기능 요구사항을 정리 중입니다.



`Report/test_case.md` 분석 결과, 구현해야 할 기능을 기능/비기능 요구사항으로 정리했습니다.

## 기능 요구사항 (Functional Requirements)

### 1. 덧셈 기능 (`add(a, b)`)
- 양수 덧셈: `1 + 10 = 11`
- 0 포함 덧셈: `0 + 1 = 1`
- 음수 덧셈: `-1 + (-10) = -11`
- 중요도: 중요

### 2. 뺄셈 기능 (`subtract(a, b)`)
- 양수 뺄셈: `5 - 2 = 3`
- 중요도: 중요

### 3. 곱셈 기능 (`multiply(a, b)`)
- 음수 곱셈: `-5 * -3 = 15`
- 0 곱셈: `0 * 10 = 0`
- 중요도: 보통/낮음

### 4. 정수 나눗셈 기능 (`divide(a, b)`)
- 정수 나눗셈(버림): `5 / 2 = 2`
- 음수 나눗셈: `-10 / 2 = -5`
- 중요도: 중요

### 5. 실수 나눗셈 기능 (`quotient(a, b)`)
- 소수점 포함 나눗셈: `5 ÷ 2 = 2.5`
- 중요도: 보통

### 6. 예외 처리
- 0으로 나누기: `0 / 0` 시 `ArithmeticError` 발생
- 중요도: 중요

---

## 비기능 요구사항 (Non-Functional Requirements)

### 1. 테스트 커버리지
- 모든 기능에 대한 테스트 케이스 작성 완료 (10개)
- 테스트 실행률: 100%
- RED 단계 완료 상태

### 2. 개발 방법론
- TDD 방식 준수 (RED → GREEN → REFACTOR)
- 현재 단계: RED 완료, GREEN 단계 대기

### 3. 코드 품질
- 클래스 기반 설계 (`Arithmetic` 클래스)
- 메서드별 명확한 책임 분리
- Docstring 포함

### 4. 데이터 타입 지원
- 정수 연산 지원 (int)
- 실수 연산 지원 (float)
- 음수 연산 지원

### 5. 예외 처리 표준
- Python 표준 예외 타입 사용 (`ArithmeticError`)
- 예외 상황 명확한 처리

### 6. 커밋 관리
- RED 단계 테스트 커밋 완료
- 각 단계별 커밋 이력 관리

---

## 구현 우선순위

### 높은 우선순위 (중요도: 중요)
1. `add(a, b)` - 덧셈
2. `subtract(a, b)` - 뺄셈
3. `divide(a, b)` - 정수 나눗셈
4. 예외 처리 (`0 / 0` → `ArithmeticError`)

### 중간 우선순위 (중요도: 보통)
5. `multiply(a, b)` - 곱셈
6. `quotient(a, b)` - 실수 나눗셈

### 낮은 우선순위 (중요도: 낮음)
7. 0 곱셈 엣지 케이스 (이미 곱셈 구현 시 포함됨)

---

현재 RED 단계가 완료되었으므로, GREEN 단계에서 위 기능들을 구현하면 됩니다.

---

**User**

구현 우선순위를 README.md 파일에 Green단계에서 해야 할 목록을 추가해줘.

---

**Cursor**


README.md를 확인하고 GREEN 단계 작업 목록을 추가합니다.



README.md에 GREEN 단계 작업 목록을 추가합니다.


```markdown
# Arithmetic Operations Module

## 프로젝트 개요

사칙연산 정확도 테스트를 위한 공통 모듈(Core Mathematical Module) 프로젝트입니다.
본 프로젝트는 TDD(Test-Driven Development) 방식인 RED-GREEN-REFACTOR 사이클을 따라 개발됩니다.

## 테스트 케이스 정보

- **테스트 케이스 ID**: TC-CMM-001 (Common Module / Core Mathematical Module)
- **기능 테스트 ID**: TC-AO-001 (Arithmetic Operations)
- **작성자**: 홍길동
- **승인자**: 박문수
- **문서 상태**: 최초 작성
- **버전**: v1.0
- **테스트 일자**: 2020-09-01
- **테스트 범위**: 공통 모듈

## 테스트 케이스

### 기본 사칙연산 테스트

| 테스트 케이스 | 예상값 | 중요도 | 상태 |
|--------------|--------|--------|------|
| 1 + 10 | 11 | 중요 | 성공 |
| 0 + 1 | 1 | 중요 | 성공 |
| 0 / 0 | 예외 발생 | 중요 | 성공 |
| -1 + (-10) | -11 | 보통 | 성공 |
| 5 - 2 | 3 | 중요 | 성공 |
| -5 * -3 | 15 | 보통 | 성공 |
| 5 / 2 | 2 | 중요 | 성공 |
| 5 ÷ 2 (quotient) | 2.5 | 보통 | 성공 |
| 0 * 10 | 0 | 낮음 | 성공 |
| -10 / 2 | -5 | 중요 | 성공 |

### 추가 테스트 사례

1. **예외 처리 확인**
   - `0 / 0` → `ArithmeticException` 예외 발생 확인

2. **다양한 조합**
   - 양수, 음수, 0을 포함한 다양한 테스트 케이스를 추가하여 연산의 정확도와 범위를 검증

3. **몫 계산 테스트 (quotient)**
   - 정수 나눗셈 대신 소수점을 포함한 결과를 테스트

## To-Do List : TDD 접근 방식

본 프로젝트는 **RED-GREEN-REFACTOR** 사이클을 따릅니다:

1. **RED**: 실패하는 테스트를 먼저 작성 ✅ _진행완료_
2. **GREEN**: 테스트를 통과하는 최소한의 코드 작성 🔄 _진행중_
3. **REFACTOR**: 코드를 개선하고 리팩토링 ⏳ _대기중_

### 개발 단계

```
[RED] → 테스트 작성 (실패) → [GREEN] → 코드 구현 (성공) → [REFACTOR] → 코드 개선
```

### GREEN 단계 작업 목록

#### 높은 우선순위 (중요도: 중요)

1. ✅ **`add(a, b)` 메서드 구현**
   - 양수 덧셈: `1 + 10 = 11`
   - 0 포함 덧셈: `0 + 1 = 1`
   - 음수 덧셈: `-1 + (-10) = -11`

2. ✅ **`subtract(a, b)` 메서드 구현**
   - 양수 뺄셈: `5 - 2 = 3`

3. ✅ **`divide(a, b)` 메서드 구현**
   - 정수 나눗셈 (버림 처리): `5 / 2 = 2`
   - 음수 나눗셈: `-10 / 2 = -5`

4. ✅ **예외 처리 구현**
   - `0 / 0` 시 `ArithmeticError` 예외 발생 처리

#### 중간 우선순위 (중요도: 보통)

5. ✅ **`multiply(a, b)` 메서드 구현**
   - 음수 곱셈: `-5 * -3 = 15`
   - 0 곱셈: `0 * 10 = 0`

6. ✅ **`quotient(a, b)` 메서드 구현**
   - 실수 나눗셈 (소수점 포함): `5 ÷ 2 = 2.5`

#### 구현 체크리스트

- [ ] `Arithmetic` 클래스에 `add(a, b)` 메서드 추가
- [ ] `Arithmetic` 클래스에 `subtract(a, b)` 메서드 추가
- [ ] `Arithmetic` 클래스에 `multiply(a, b)` 메서드 추가
- [ ] `Arithmetic` 클래스에 `divide(a, b)` 메서드 추가 (정수 나눗셈)
- [ ] `Arithmetic` 클래스에 `quotient(a, b)` 메서드 추가 (실수 나눗셈)
- [ ] `divide(a, b)` 메서드에 `0 / 0` 예외 처리 추가
- [ ] 모든 테스트 케이스 통과 확인 (10개)
- [ ] GREEN 단계 커밋 완료

## 프로젝트 구조

```
Arithmetic/
├── README.md
├── src/
│   └── (소스 코드)
├── test/
│   └── (테스트 코드)
└── (기타 설정 파일)
```

## 기능 요구사항

### 산술 연산 기능

- **덧셈 (Addition)**: 두 수의 합 계산
- **뺄셈 (Subtraction)**: 두 수의 차 계산
- **곱셈 (Multiplication)**: 두 수의 곱 계산
- **나눗셈 (Division)**: 두 수의 몫 계산
  - 정수 나눗셈: 정수 결과 반환
  - 실수 나눗셈 (quotient): 소수점 결과 반환
- **예외 처리**: 0으로 나누기 시 `ArithmeticException` 발생

## 실행 방법

(프로젝트 설정 후 업데이트 예정)

## 참고사항

이 테스트 케이스는 기능의 정확성과 예외 처리를 포함하여 클래스의 모든 기능을 검증합니다.


```


README.md에 GREEN 단계 작업 목록을 추가했습니다.

추가된 내용:
1. **TDD 단계 상태 표시**: RED 완료, GREEN 진행중, REFACTOR 대기중으로 업데이트
2. **GREEN 단계 작업 목록**: 구현 우선순위별로 정리
   - 높은 우선순위: `add`, `subtract`, `divide`, 예외 처리
   - 중간 우선순위: `multiply`, `quotient`
3. **구현 체크리스트**: 각 메서드 구현 및 테스트 통과 확인 항목 포함

README.md의 "To-Do List : TDD 접근 방식" 섹션에서 GREEN 단계 작업 목록을 확인할 수 있습니다.

---

**User**

@README.md 내용 중 
@README.md (63-78) 
을 최소 단위로 구현 하려고 하는데,
먼저 시나리오를 작성 해서 보내주고 승인 받은 후 구현해줘.

---

**Cursor**


최소 단위 구현 시나리오를 작성합니다. 현재 코드 상태를 확인 중입니다.



최소 단위 구현 시나리오 작성 중입니다.


```markdown
# GREEN 단계 구현 시나리오

## 목표
README.md의 높은 우선순위 항목(63-78번 라인)을 최소 단위로 구현하여 테스트를 통과시키기

## 현재 상태
- ✅ RED 단계 완료: 모든 테스트 케이스 작성 완료 (10개)
- ✅ 테스트 실행 결과: 모든 테스트 실패 (예상된 동작)
- 🔄 GREEN 단계 진행: 최소한의 코드로 테스트 통과

## 구현 대상 (높은 우선순위)

### 1. `add(a, b)` 메서드 구현
- **관련 테스트**: 3개
  - `test_add_1_plus_10_should_return_11`
  - `test_add_0_plus_1_should_return_1`
  - `test_add_negative1_plus_negative10_should_return_negative11`

### 2. `subtract(a, b)` 메서드 구현
- **관련 테스트**: 1개
  - `test_subtract_5_minus_2_should_return_3`

### 3. `divide(a, b)` 메서드 구현
- **관련 테스트**: 2개
  - `test_divide_5_by_2_should_return_2`
  - `test_divide_negative10_by_2_should_return_negative5`

### 4. 예외 처리 구현
- **관련 테스트**: 1개
  - `test_divide_0_by_0_should_throw_arithmetic_exception`

---

## 구현 시나리오

### Phase 1: `add(a, b)` 메서드 구현

**목표**: 덧셈 기능 구현으로 3개 테스트 통과

**단계**:
1. `Arithmetic` 클래스에 `add(a, b)` 메서드 추가
   ```python
   def add(self, a, b):
       return a + b
   ```
2. 테스트 실행: `pytest test/test_arithmetic.py::TestArithmeticOperations::test_add_1_plus_10_should_return_11 -v`
3. 모든 add 관련 테스트 실행: `pytest test/test_arithmetic.py -k "test_add" -v`
4. 결과 확인: 3개 테스트 모두 통과 확인
5. 체크리스트 업데이트: `add(a, b)` 메서드 항목 체크

**예상 결과**: 
- ✅ `test_add_1_plus_10_should_return_11` 통과
- ✅ `test_add_0_plus_1_should_return_1` 통과
- ✅ `test_add_negative1_plus_negative10_should_return_negative11` 통과

---

### Phase 2: `subtract(a, b)` 메서드 구현

**목표**: 뺄셈 기능 구현으로 1개 테스트 통과

**단계**:
1. `Arithmetic` 클래스에 `subtract(a, b)` 메서드 추가
   ```python
   def subtract(self, a, b):
       return a - b
   ```
2. 테스트 실행: `pytest test/test_arithmetic.py::TestArithmeticOperations::test_subtract_5_minus_2_should_return_3 -v`
3. 결과 확인: 테스트 통과 확인
4. 체크리스트 업데이트: `subtract(a, b)` 메서드 항목 체크

**예상 결과**: 
- ✅ `test_subtract_5_minus_2_should_return_3` 통과

---

### Phase 3: `divide(a, b)` 메서드 구현 (예외 처리 제외)

**목표**: 정수 나눗셈 기능 구현으로 2개 테스트 통과

**단계**:
1. `Arithmetic` 클래스에 `divide(a, b)` 메서드 추가
   ```python
   def divide(self, a, b):
       return a // b  # 정수 나눗셈 (버림 처리)
   ```
2. 테스트 실행: `pytest test/test_arithmetic.py -k "test_divide" -v`
3. 결과 확인: 
   - ✅ `test_divide_5_by_2_should_return_2` 통과 예상
   - ✅ `test_divide_negative10_by_2_should_return_negative5` 통과 예상
   - ❌ `test_divide_0_by_0_should_throw_arithmetic_exception` 실패 예상 (예외 처리 미구현)
4. 체크리스트 업데이트: `divide(a, b)` 메서드 항목 체크

**예상 결과**: 
- ✅ `test_divide_5_by_2_should_return_2` 통과
- ✅ `test_divide_negative10_by_2_should_return_negative5` 통과
- ❌ `test_divide_0_by_0_should_throw_arithmetic_exception` 실패 (다음 단계에서 처리)

---

### Phase 4: 예외 처리 구현

**목표**: `0 / 0` 예외 처리로 1개 테스트 통과

**단계**:
1. `divide(a, b)` 메서드에 예외 처리 추가
   ```python
   def divide(self, a, b):
       if b == 0:
           raise ArithmeticError("Division by zero")
       return a // b
   ```
2. 테스트 실행: `pytest test/test_arithmetic.py::TestArithmeticOperations::test_divide_0_by_0_should_throw_arithmetic_exception -v`
3. 모든 divide 관련 테스트 재실행: `pytest test/test_arithmetic.py -k "test_divide" -v`
4. 결과 확인: 모든 divide 테스트 통과 확인
5. 체크리스트 업데이트: 예외 처리 항목 체크

**예상 결과**: 
- ✅ `test_divide_5_by_2_should_return_2` 통과
- ✅ `test_divide_negative10_by_2_should_return_negative5` 통과
- ✅ `test_divide_0_by_0_should_throw_arithmetic_exception` 통과

---

## 최종 검증

### 전체 테스트 실행
```bash
pytest test/test_arithmetic.py -v
```

**예상 결과**:
- ✅ Phase 1-4에서 구현한 테스트: 7개 통과
- ❌ 중간 우선순위 항목 테스트: 3개 실패 (아직 미구현)
  - `test_multiply_negative5_by_negative3_should_return_15`
  - `test_multiply_0_by_10_should_return_0`
  - `test_quotient_5_divide_2_should_return_2_5`

### 구현 완료 체크리스트
- [x] `Arithmetic` 클래스에 `add(a, b)` 메서드 추가
- [x] `Arithmetic` 클래스에 `subtract(a, b)` 메서드 추가
- [x] `Arithmetic` 클래스에 `divide(a, b)` 메서드 추가 (정수 나눗셈)
- [x] `divide(a, b)` 메서드에 `0 / 0` 예외 처리 추가
- [x] 높은 우선순위 테스트 케이스 통과 확인 (7개)
- [ ] GREEN 단계 커밋 완료 (구현 후 진행)

---

## 구현 원칙

1. **최소한의 코드**: 테스트를 통과시키는 최소한의 코드만 작성
2. **단계별 검증**: 각 Phase마다 테스트 실행 및 확인
3. **TDD 원칙 준수**: GREEN 단계에서는 리팩토링 없이 최소 구현만
4. **명확한 커밋**: 각 Phase별로 커밋하거나, 전체 완료 후 커밋 (선택)

---

## 예상 소요 시간
- Phase 1: ~5분
- Phase 2: ~3분
- Phase 3: ~5분
- Phase 4: ~5분
- 최종 검증: ~3분
- **총 예상 시간**: ~21분

---

## 승인 대기

이 시나리오에 대한 승인을 기다립니다. 승인 후 구현을 진행하겠습니다.

**작성일**: 2025-12-16  
**작성자**: AI Assistant

```


최소 단위 구현 시나리오를 작성했습니다. `Report/GREEN_Implementation_Scenario.md` 파일에 저장했습니다.

## 시나리오 요약

높은 우선순위 항목을 4단계로 나누어 구현합니다:

### Phase 1: `add(a, b)` 메서드 구현
- 덧셈 기능 구현 (3개 테스트 통과)

### Phase 2: `subtract(a, b)` 메서드 구현
- 뺄셈 기능 구현 (1개 테스트 통과)

### Phase 3: `divide(a, b)` 메서드 구현
- 정수 나눗셈 기능 구현 (2개 테스트 통과, 예외 처리 제외)

### Phase 4: 예외 처리 구현
- `0 / 0` 시 `ArithmeticError` 발생 처리 (1개 테스트 통과)

각 단계마다:
- 최소한의 코드로 구현
- 테스트 실행 및 검증
- 체크리스트 업데이트

**예상 결과**: 총 7개 테스트 통과 (높은 우선순위 항목 완료)

시나리오를 검토해 주세요. 승인해 주시면 구현을 진행하겠습니다. 수정이 필요하면 알려주세요.

---

**User**

네

---

**Cursor**


시나리오에 따라 구현을 진행합니다.



Phase 1: `add(a, b)` 메서드 구현 중.


```python
"""
TC-CMM-001: Common Module / Core Mathematical Module
산술 연산 모듈
"""


class Arithmetic:
    """산술 연산을 수행하는 클래스"""
    
    def add(self, a, b):
        """두 수의 합을 계산합니다.
        
        Args:
            a: 첫 번째 숫자
            b: 두 번째 숫자
            
        Returns:
            두 수의 합
        """
        return a + b


```


Phase 1 완료: `add(a, b)` 메서드 구현 완료, 3개 테스트 통과. Phase 2 진행: `subtract(a, b)` 메서드 구현.


```python
"""
TC-CMM-001: Common Module / Core Mathematical Module
산술 연산 모듈
"""


class Arithmetic:
    """산술 연산을 수행하는 클래스"""
    
    def add(self, a, b):
        """두 수의 합을 계산합니다.
        
        Args:
            a: 첫 번째 숫자
            b: 두 번째 숫자
            
        Returns:
            두 수의 합
        """
        return a + b
    
    def subtract(self, a, b):
        """두 수의 차를 계산합니다.
        
        Args:
            a: 첫 번째 숫자 (피감수)
            b: 두 번째 숫자 (감수)
            
        Returns:
            두 수의 차
        """
        return a - b


```


Phase 2 완료: `subtract(a, b)` 메서드 구현 완료, 1개 테스트 통과. Phase 3 진행: `divide(a, b)` 메서드 구현 (예외 처리 제외).


```python
"""
TC-CMM-001: Common Module / Core Mathematical Module
산술 연산 모듈
"""


class Arithmetic:
    """산술 연산을 수행하는 클래스"""
    
    def add(self, a, b):
        """두 수의 합을 계산합니다.
        
        Args:
            a: 첫 번째 숫자
            b: 두 번째 숫자
            
        Returns:
            두 수의 합
        """
        return a + b
    
    def subtract(self, a, b):
        """두 수의 차를 계산합니다.
        
        Args:
            a: 첫 번째 숫자 (피감수)
            b: 두 번째 숫자 (감수)
            
        Returns:
            두 수의 차
        """
        return a - b
    
    def divide(self, a, b):
        """두 수의 정수 나눗셈을 계산합니다 (버림 처리).
        
        Args:
            a: 첫 번째 숫자 (피제수)
            b: 두 번째 숫자 (제수)
            
        Returns:
            정수 나눗셈 결과 (버림)
        """
        return a // b


```


Phase 3 완료: `divide(a, b)` 메서드 구현 완료, 3개 테스트 통과(예외 처리 테스트 포함). Phase 4 진행: 예외 처리 명시적 구현.


```python
"""
TC-CMM-001: Common Module / Core Mathematical Module
산술 연산 모듈
"""


class Arithmetic:
    """산술 연산을 수행하는 클래스"""
    
    def add(self, a, b):
        """두 수의 합을 계산합니다.
        
        Args:
            a: 첫 번째 숫자
            b: 두 번째 숫자
            
        Returns:
            두 수의 합
        """
        return a + b
    
    def subtract(self, a, b):
        """두 수의 차를 계산합니다.
        
        Args:
            a: 첫 번째 숫자 (피감수)
            b: 두 번째 숫자 (감수)
            
        Returns:
            두 수의 차
        """
        return a - b
    
    def divide(self, a, b):
        """두 수의 정수 나눗셈을 계산합니다 (버림 처리).
        
        Args:
            a: 첫 번째 숫자 (피제수)
            b: 두 번째 숫자 (제수)
            
        Returns:
            정수 나눗셈 결과 (버림)
            
        Raises:
            ArithmeticError: 제수가 0일 때 발생
        """
        if b == 0:
            raise ArithmeticError("Division by zero")
        return a // b


```


Phase 4 완료: 예외 처리 구현 완료. 최종 검증 진행.



최종 검증 완료. 높은 우선순위 항목 7개 테스트 통과. 구현된 코드 확인 및 README.md 체크리스트 업데이트 중.



README.md의 체크리스트 업데이트 중.


```markdown
# Arithmetic Operations Module

## 프로젝트 개요

사칙연산 정확도 테스트를 위한 공통 모듈(Core Mathematical Module) 프로젝트입니다.
본 프로젝트는 TDD(Test-Driven Development) 방식인 RED-GREEN-REFACTOR 사이클을 따라 개발됩니다.

## 테스트 케이스 정보

- **테스트 케이스 ID**: TC-CMM-001 (Common Module / Core Mathematical Module)
- **기능 테스트 ID**: TC-AO-001 (Arithmetic Operations)
- **작성자**: 홍길동
- **승인자**: 박문수
- **문서 상태**: 최초 작성
- **버전**: v1.0
- **테스트 일자**: 2020-09-01
- **테스트 범위**: 공통 모듈

## 테스트 케이스

### 기본 사칙연산 테스트

| 테스트 케이스 | 예상값 | 중요도 | 상태 |
|--------------|--------|--------|------|
| 1 + 10 | 11 | 중요 | 성공 |
| 0 + 1 | 1 | 중요 | 성공 |
| 0 / 0 | 예외 발생 | 중요 | 성공 |
| -1 + (-10) | -11 | 보통 | 성공 |
| 5 - 2 | 3 | 중요 | 성공 |
| -5 * -3 | 15 | 보통 | 성공 |
| 5 / 2 | 2 | 중요 | 성공 |
| 5 ÷ 2 (quotient) | 2.5 | 보통 | 성공 |
| 0 * 10 | 0 | 낮음 | 성공 |
| -10 / 2 | -5 | 중요 | 성공 |

### 추가 테스트 사례

1. **예외 처리 확인**
   - `0 / 0` → `ArithmeticException` 예외 발생 확인

2. **다양한 조합**
   - 양수, 음수, 0을 포함한 다양한 테스트 케이스를 추가하여 연산의 정확도와 범위를 검증

3. **몫 계산 테스트 (quotient)**
   - 정수 나눗셈 대신 소수점을 포함한 결과를 테스트

## To-Do List : TDD 접근 방식

본 프로젝트는 **RED-GREEN-REFACTOR** 사이클을 따릅니다:

1. **RED**: 실패하는 테스트를 먼저 작성 ✅ _진행완료_
2. **GREEN**: 테스트를 통과하는 최소한의 코드 작성 🔄 _진행중_
3. **REFACTOR**: 코드를 개선하고 리팩토링 ⏳ _대기중_

### 개발 단계

```
[RED] → 테스트 작성 (실패) → [GREEN] → 코드 구현 (성공) → [REFACTOR] → 코드 개선
```

### GREEN 단계 작업 목록

#### 높은 우선순위 (중요도: 중요)

1. ✅ **`add(a, b)` 메서드 구현**
   - 양수 덧셈: `1 + 10 = 11`
   - 0 포함 덧셈: `0 + 1 = 1`
   - 음수 덧셈: `-1 + (-10) = -11`

2. ✅ **`subtract(a, b)` 메서드 구현**
   - 양수 뺄셈: `5 - 2 = 3`

3. ✅ **`divide(a, b)` 메서드 구현**
   - 정수 나눗셈 (버림 처리): `5 / 2 = 2`
   - 음수 나눗셈: `-10 / 2 = -5`

4. ✅ **예외 처리 구현**
   - `0 / 0` 시 `ArithmeticError` 예외 발생 처리

#### 중간 우선순위 (중요도: 보통)

5. ✅ **`multiply(a, b)` 메서드 구현**
   - 음수 곱셈: `-5 * -3 = 15`
   - 0 곱셈: `0 * 10 = 0`

6. ✅ **`quotient(a, b)` 메서드 구현**
   - 실수 나눗셈 (소수점 포함): `5 ÷ 2 = 2.5`

#### 구현 체크리스트

- [x] `Arithmetic` 클래스에 `add(a, b)` 메서드 추가 ✅
- [x] `Arithmetic` 클래스에 `subtract(a, b)` 메서드 추가 ✅
- [ ] `Arithmetic` 클래스에 `multiply(a, b)` 메서드 추가 (중간 우선순위)
- [x] `Arithmetic` 클래스에 `divide(a, b)` 메서드 추가 (정수 나눗셈) ✅
- [ ] `Arithmetic` 클래스에 `quotient(a, b)` 메서드 추가 (실수 나눗셈) (중간 우선순위)
- [x] `divide(a, b)` 메서드에 `0 / 0` 예외 처리 추가 ✅
- [x] 높은 우선순위 테스트 케이스 통과 확인 (7개) ✅
- [ ] 중간 우선순위 테스트 케이스 통과 확인 (3개) (다음 단계)
- [ ] GREEN 단계 커밋 완료

## 프로젝트 구조

```
Arithmetic/
├── README.md
├── src/
│   └── (소스 코드)
├── test/
│   └── (테스트 코드)
└── (기타 설정 파일)
```

## 기능 요구사항

### 산술 연산 기능

- **덧셈 (Addition)**: 두 수의 합 계산
- **뺄셈 (Subtraction)**: 두 수의 차 계산
- **곱셈 (Multiplication)**: 두 수의 곱 계산
- **나눗셈 (Division)**: 두 수의 몫 계산
  - 정수 나눗셈: 정수 결과 반환
  - 실수 나눗셈 (quotient): 소수점 결과 반환
- **예외 처리**: 0으로 나누기 시 `ArithmeticException` 발생

## 실행 방법

(프로젝트 설정 후 업데이트 예정)

## 참고사항

이 테스트 케이스는 기능의 정확성과 예외 처리를 포함하여 클래스의 모든 기능을 검증합니다.


```


## 구현 완료 요약

### 구현된 기능 (높은 우선순위)

1. **`add(a, b)` 메서드** — 3개 테스트 통과
   - 양수 덧셈: `1 + 10 = 11`
   - 0 포함 덧셈: `0 + 1 = 1`
   - 음수 덧셈: `-1 + (-10) = -11`

2. **`subtract(a, b)` 메서드** — 1개 테스트 통과
   - 양수 뺄셈: `5 - 2 = 3`

3. **`divide(a, b)` 메서드** — 2개 테스트 통과
   - 정수 나눗셈 (버림): `5 / 2 = 2`
   - 음수 나눗셈: `-10 / 2 = -5`

4. **예외 처리** — 1개 테스트 통과
   - `0 / 0` 시 `ArithmeticError` 발생

### 테스트 결과

- 통과: 7개 (높은 우선순위 항목 모두 통과)
- 실패: 3개 (중간 우선순위 항목 - 아직 미구현)
  - `multiply` 메서드 관련 2개
  - `quotient` 메서드 관련 1개

### 구현된 코드

`src/arithmetic.py`에 다음 메서드가 추가되었습니다:
- `add(a, b)` - 덧셈
- `subtract(a, b)` - 뺄셈
- `divide(a, b)` - 정수 나눗셈 (예외 처리 포함)

모든 메서드에 docstring이 포함되어 있으며, linter 오류는 없습니다.

README.md의 체크리스트도 업데이트되었습니다. 다음 단계로 중간 우선순위 항목(`multiply`, `quotient`)을 구현하면 됩니다.

---

**User**

첨부한 이미지 처럼 arithmetic.py 실행 했을 때 아무 것도 안 나오는데 실행결과 만들 수 있을까?

---

**Cursor**


`arithmetic.py`에 실행 가능한 코드가 없어 출력이 없습니다. 실행 시 결과가 보이도록 `if __name__ == "__main__":` 블록을 추가하겠습니다.



실행 시 결과가 보이도록 예제 코드를 추가 중입니다.


```python
"""
TC-CMM-001: Common Module / Core Mathematical Module
산술 연산 모듈
"""


class Arithmetic:
    """산술 연산을 수행하는 클래스"""
    
    def add(self, a, b):
        """두 수의 합을 계산합니다.
        
        Args:
            a: 첫 번째 숫자
            b: 두 번째 숫자
            
        Returns:
            두 수의 합
        """
        return a + b
    
    def subtract(self, a, b):
        """두 수의 차를 계산합니다.
        
        Args:
            a: 첫 번째 숫자 (피감수)
            b: 두 번째 숫자 (감수)
            
        Returns:
            두 수의 차
        """
        return a - b
    
    def divide(self, a, b):
        """두 수의 정수 나눗셈을 계산합니다 (버림 처리).
        
        Args:
            a: 첫 번째 숫자 (피제수)
            b: 두 번째 숫자 (제수)
            
        Returns:
            정수 나눗셈 결과 (버림)
            
        Raises:
            ArithmeticError: 제수가 0일 때 발생
        """
        if b == 0:
            raise ArithmeticError("Division by zero")
        return a // b


if __name__ == "__main__":
    """모듈이 직접 실행될 때 예제 코드를 실행합니다."""
    print("=" * 50)
    print("Arithmetic Operations Module - 예제 실행")
    print("=" * 50)
    print()
    
    arithmetic = Arithmetic()
    
    # 덧셈 예제
    print("1. 덧셈 (Addition)")
    print(f"   1 + 10 = {arithmetic.add(1, 10)}")
    print(f"   0 + 1 = {arithmetic.add(0, 1)}")
    print(f"   -1 + (-10) = {arithmetic.add(-1, -10)}")
    print()
    
    # 뺄셈 예제
    print("2. 뺄셈 (Subtraction)")
    print(f"   5 - 2 = {arithmetic.subtract(5, 2)}")
    print()
    
    # 나눗셈 예제
    print("3. 나눗셈 (Division - 정수 나눗셈)")
    print(f"   5 / 2 = {arithmetic.divide(5, 2)}")
    print(f"   -10 / 2 = {arithmetic.divide(-10, 2)}")
    print()
    
    # 예외 처리 예제
    print("4. 예외 처리 (Exception Handling)")
    try:
        result = arithmetic.divide(0, 0)
        print(f"   0 / 0 = {result}")
    except ArithmeticError as e:
        print(f"   0 / 0 → {type(e).__name__}: {e}")
    print()
    
    print("=" * 50)
    print("예제 실행 완료")
    print("=" * 50)


```


완료했습니다. 이제 `python src\arithmetic.py`를 실행하면 구현된 메서드들의 예제 결과가 출력됩니다.

## 추가된 내용

`if __name__ == "__main__":` 블록을 추가해 다음을 표시합니다:

1. **덧셈 예제** - 3가지 케이스 (양수, 0 포함, 음수)
2. **뺄셈 예제** - 기본 뺄셈
3. **나눗셈 예제** - 정수 나눗셈 2가지 케이스
4. **예외 처리 예제** - `0 / 0` 시 `ArithmeticError` 발생 확인

모듈을 직접 실행하면 예제가 자동으로 실행되고, 다른 모듈에서 import할 때는 실행되지 않습니다. 테스트를 실행해 정상 동작을 확인했습니다.

---

**User**

@README.md 내용 중 
@README.md (80-87) 
을 최소 단위로 구현 하려고 하는데,
먼저 시나리오를 작성 해서 보내주고 승인 받은 후 구현해줘.

---

**Cursor**


중간 우선순위 항목 구현 시나리오 작성 중입니다.



중간 우선순위 항목 구현 시나리오 작성 중입니다.


```markdown
# GREEN 단계 구현 시나리오 (Part 2: 중간 우선순위)

## 목표
README.md의 중간 우선순위 항목(80-87번 라인)을 최소 단위로 구현하여 테스트를 통과시키기

## 현재 상태
- ✅ 높은 우선순위 항목 구현 완료 (7개 테스트 통과)
- 🔄 중간 우선순위 항목 구현 진행 (3개 테스트 실패)
- ⏳ 낮은 우선순위 항목 대기

## 구현 대상 (중간 우선순위)

### 1. `multiply(a, b)` 메서드 구현
- **관련 테스트**: 2개
  - `test_multiply_negative5_by_negative3_should_return_15`
  - `test_multiply_0_by_10_should_return_0`

### 2. `quotient(a, b)` 메서드 구현
- **관련 테스트**: 1개
  - `test_quotient_5_divide_2_should_return_2_5`

---

## 구현 시나리오

### Phase 1: `multiply(a, b)` 메서드 구현

**목표**: 곱셈 기능 구현으로 2개 테스트 통과

**단계**:
1. `Arithmetic` 클래스에 `multiply(a, b)` 메서드 추가
   ```python
   def multiply(self, a, b):
       return a * b
   ```
2. 테스트 실행: `pytest test/test_arithmetic.py -k "test_multiply" -v`
3. 결과 확인: 2개 테스트 모두 통과 확인
4. 체크리스트 업데이트: `multiply(a, b)` 메서드 항목 체크

**예상 결과**: 
- ✅ `test_multiply_negative5_by_negative3_should_return_15` 통과
- ✅ `test_multiply_0_by_10_should_return_0` 통과

---

### Phase 2: `quotient(a, b)` 메서드 구현

**목표**: 실수 나눗셈 기능 구현으로 1개 테스트 통과

**단계**:
1. `Arithmetic` 클래스에 `quotient(a, b)` 메서드 추가
   ```python
   def quotient(self, a, b):
       return a / b  # 실수 나눗셈 (소수점 포함)
   ```
2. 테스트 실행: `pytest test/test_arithmetic.py::TestArithmeticOperations::test_quotient_5_divide_2_should_return_2_5 -v`
3. 결과 확인: 테스트 통과 확인
4. 체크리스트 업데이트: `quotient(a, b)` 메서드 항목 체크

**예상 결과**: 
- ✅ `test_quotient_5_divide_2_should_return_2_5` 통과

---

## 최종 검증

### 전체 테스트 실행
```bash
pytest test/test_arithmetic.py -v
```

**예상 결과**:
- ✅ 모든 테스트: 10개 통과
- ✅ 높은 우선순위 항목: 7개 통과
- ✅ 중간 우선순위 항목: 3개 통과

### 구현 완료 체크리스트
- [x] `Arithmetic` 클래스에 `add(a, b)` 메서드 추가 ✅
- [x] `Arithmetic` 클래스에 `subtract(a, b)` 메서드 추가 ✅
- [ ] `Arithmetic` 클래스에 `multiply(a, b)` 메서드 추가
- [x] `Arithmetic` 클래스에 `divide(a, b)` 메서드 추가 ✅
- [ ] `Arithmetic` 클래스에 `quotient(a, b)` 메서드 추가
- [x] `divide(a, b)` 메서드에 `0 / 0` 예외 처리 추가 ✅
- [ ] 모든 테스트 케이스 통과 확인 (10개)
- [ ] GREEN 단계 커밋 완료 (구현 후 진행)

---

## 추가 작업: 예제 코드 업데이트

구현 완료 후 `if __name__ == "__main__":` 블록에 다음 예제 추가:
- 곱셈 예제 (multiply)
- 실수 나눗셈 예제 (quotient)

---

## 구현 원칙

1. **최소한의 코드**: 테스트를 통과시키는 최소한의 코드만 작성
2. **단계별 검증**: 각 Phase마다 테스트 실행 및 확인
3. **TDD 원칙 준수**: GREEN 단계에서는 리팩토링 없이 최소 구현만
4. **일관성 유지**: 기존 구현된 메서드들과 동일한 스타일 유지

---

## 예상 소요 시간
- Phase 1: ~5분
- Phase 2: ~5분
- 예제 코드 업데이트: ~3분
- 최종 검증: ~3분
- **총 예상 시간**: ~16분

---

## 승인 대기

이 시나리오에 대한 승인을 기다립니다. 승인 후 구현을 진행하겠습니다.

**작성일**: 2025-12-16  
**작성자**: AI Assistant

```


중간 우선순위 항목 구현 시나리오를 작성했습니다. `Report/GREEN_Implementation_Scenario_Part2.md`에 저장했습니다.

## 시나리오 요약

중간 우선순위 항목을 2단계로 나누어 구현합니다:

### Phase 1: `multiply(a, b)` 메서드 구현
- 곱셈 기능 구현 (2개 테스트 통과)
  - 음수 곱셈: `-5 * -3 = 15`
  - 0 곱셈: `0 * 10 = 0`

### Phase 2: `quotient(a, b)` 메서드 구현
- 실수 나눗셈 기능 구현 (1개 테스트 통과)
  - 소수점 포함 나눗셈: `5 ÷ 2 = 2.5`

### 추가 작업
- 구현 완료 후 예제 코드(`if __name__ == "__main__":`)에 곱셈과 실수 나눗셈 예제 추가

각 단계마다:
- 최소한의 코드로 구현
- 테스트 실행 및 검증
- 체크리스트 업데이트

**예상 결과**: 총 10개 테스트 모두 통과 (GREEN 단계 완료)

시나리오를 검토해 주세요. 승인해 주시면 구현을 진행하겠습니다. 수정이 필요하면 알려주세요.

---

**User**

네

---

**Cursor**


시나리오에 따라 구현을 진행합니다.



Phase 1: `multiply(a, b)` 메서드 구현 중.


```python
"""
TC-CMM-001: Common Module / Core Mathematical Module
산술 연산 모듈
"""


class Arithmetic:
    """산술 연산을 수행하는 클래스"""
    
    def add(self, a, b):
        """두 수의 합을 계산합니다.
        
        Args:
            a: 첫 번째 숫자
            b: 두 번째 숫자
            
        Returns:
            두 수의 합
        """
        return a + b
    
    def subtract(self, a, b):
        """두 수의 차를 계산합니다.
        
        Args:
            a: 첫 번째 숫자 (피감수)
            b: 두 번째 숫자 (감수)
            
        Returns:
            두 수의 차
        """
        return a - b
    
    def multiply(self, a, b):
        """두 수의 곱을 계산합니다.
        
        Args:
            a: 첫 번째 숫자
            b: 두 번째 숫자
            
        Returns:
            두 수의 곱
        """
        return a * b
    
    def divide(self, a, b):
        """두 수의 정수 나눗셈을 계산합니다 (버림 처리).
        
        Args:
            a: 첫 번째 숫자 (피제수)
            b: 두 번째 숫자 (제수)
            
        Returns:
            정수 나눗셈 결과 (버림)
            
        Raises:
            ArithmeticError: 제수가 0일 때 발생
        """
        if b == 0:
            raise ArithmeticError("Division by zero")
        return a // b


if __name__ == "__main__":
    """모듈이 직접 실행될 때 예제 코드를 실행합니다."""
    print("=" * 50)
    print("Arithmetic Operations Module - 예제 실행")
    print("=" * 50)
    print()
    
    arithmetic = Arithmetic()
    
    # 덧셈 예제
    print("1. 덧셈 (Addition)")
    print(f"   1 + 10 = {arithmetic.add(1, 10)}")
    print(f"   0 + 1 = {arithmetic.add(0, 1)}")
    print(f"   -1 + (-10) = {arithmetic.add(-1, -10)}")
    print()
    
    # 뺄셈 예제
    print("2. 뺄셈 (Subtraction)")
    print(f"   5 - 2 = {arithmetic.subtract(5, 2)}")
    print()
    
    # 나눗셈 예제
    print("3. 나눗셈 (Division - 정수 나눗셈)")
    print(f"   5 / 2 = {arithmetic.divide(5, 2)}")
    print(f"   -10 / 2 = {arithmetic.divide(-10, 2)}")
    print()
    
    # 예외 처리 예제
    print("4. 예외 처리 (Exception Handling)")
    try:
        result = arithmetic.divide(0, 0)
        print(f"   0 / 0 = {result}")
    except ArithmeticError as e:
        print(f"   0 / 0 → {type(e).__name__}: {e}")
    print()
    
    print("=" * 50)
    print("예제 실행 완료")
    print("=" * 50)


```


Phase 1 완료: `multiply(a, b)` 메서드 구현 완료, 2개 테스트 통과. Phase 2 진행: `quotient(a, b)` 메서드 구현.


```python
"""
TC-CMM-001: Common Module / Core Mathematical Module
산술 연산 모듈
"""


class Arithmetic:
    """산술 연산을 수행하는 클래스"""
    
    def add(self, a, b):
        """두 수의 합을 계산합니다.
        
        Args:
            a: 첫 번째 숫자
            b: 두 번째 숫자
            
        Returns:
            두 수의 합
        """
        return a + b
    
    def subtract(self, a, b):
        """두 수의 차를 계산합니다.
        
        Args:
            a: 첫 번째 숫자 (피감수)
            b: 두 번째 숫자 (감수)
            
        Returns:
            두 수의 차
        """
        return a - b
    
    def multiply(self, a, b):
        """두 수의 곱을 계산합니다.
        
        Args:
            a: 첫 번째 숫자
            b: 두 번째 숫자
            
        Returns:
            두 수의 곱
        """
        return a * b
    
    def divide(self, a, b):
        """두 수의 정수 나눗셈을 계산합니다 (버림 처리).
        
        Args:
            a: 첫 번째 숫자 (피제수)
            b: 두 번째 숫자 (제수)
            
        Returns:
            정수 나눗셈 결과 (버림)
            
        Raises:
            ArithmeticError: 제수가 0일 때 발생
        """
        if b == 0:
            raise ArithmeticError("Division by zero")
        return a // b
    
    def quotient(self, a, b):
        """두 수의 실수 나눗셈을 계산합니다 (소수점 포함).
        
        Args:
            a: 첫 번째 숫자 (피제수)
            b: 두 번째 숫자 (제수)
            
        Returns:
            실수 나눗셈 결과 (소수점 포함)
        """
        return a / b


if __name__ == "__main__":
    """모듈이 직접 실행될 때 예제 코드를 실행합니다."""
    print("=" * 50)
    print("Arithmetic Operations Module - 예제 실행")
    print("=" * 50)
    print()
    
    arithmetic = Arithmetic()
    
    # 덧셈 예제
    print("1. 덧셈 (Addition)")
    print(f"   1 + 10 = {arithmetic.add(1, 10)}")
    print(f"   0 + 1 = {arithmetic.add(0, 1)}")
    print(f"   -1 + (-10) = {arithmetic.add(-1, -10)}")
    print()
    
    # 뺄셈 예제
    print("2. 뺄셈 (Subtraction)")
    print(f"   5 - 2 = {arithmetic.subtract(5, 2)}")
    print()
    
    # 나눗셈 예제
    print("3. 나눗셈 (Division - 정수 나눗셈)")
    print(f"   5 / 2 = {arithmetic.divide(5, 2)}")
    print(f"   -10 / 2 = {arithmetic.divide(-10, 2)}")
    print()
    
    # 예외 처리 예제
    print("4. 예외 처리 (Exception Handling)")
    try:
        result = arithmetic.divide(0, 0)
        print(f"   0 / 0 = {result}")
    except ArithmeticError as e:
        print(f"   0 / 0 → {type(e).__name__}: {e}")
    print()
    
    print("=" * 50)
    print("예제 실행 완료")
    print("=" * 50)


```


Phase 2 완료: `quotient(a, b)` 메서드 구현 완료, 1개 테스트 통과. 예제 코드 업데이트 진행.


```python
"""
TC-CMM-001: Common Module / Core Mathematical Module
산술 연산 모듈
"""


class Arithmetic:
    """산술 연산을 수행하는 클래스"""
    
    def add(self, a, b):
        """두 수의 합을 계산합니다.
        
        Args:
            a: 첫 번째 숫자
            b: 두 번째 숫자
            
        Returns:
            두 수의 합
        """
        return a + b
    
    def subtract(self, a, b):
        """두 수의 차를 계산합니다.
        
        Args:
            a: 첫 번째 숫자 (피감수)
            b: 두 번째 숫자 (감수)
            
        Returns:
            두 수의 차
        """
        return a - b
    
    def multiply(self, a, b):
        """두 수의 곱을 계산합니다.
        
        Args:
            a: 첫 번째 숫자
            b: 두 번째 숫자
            
        Returns:
            두 수의 곱
        """
        return a * b
    
    def divide(self, a, b):
        """두 수의 정수 나눗셈을 계산합니다 (버림 처리).
        
        Args:
            a: 첫 번째 숫자 (피제수)
            b: 두 번째 숫자 (제수)
            
        Returns:
            정수 나눗셈 결과 (버림)
            
        Raises:
            ArithmeticError: 제수가 0일 때 발생
        """
        if b == 0:
            raise ArithmeticError("Division by zero")
        return a // b
    
    def quotient(self, a, b):
        """두 수의 실수 나눗셈을 계산합니다 (소수점 포함).
        
        Args:
            a: 첫 번째 숫자 (피제수)
            b: 두 번째 숫자 (제수)
            
        Returns:
            실수 나눗셈 결과 (소수점 포함)
        """
        return a / b


if __name__ == "__main__":
    """모듈이 직접 실행될 때 예제 코드를 실행합니다."""
    print("=" * 50)
    print("Arithmetic Operations Module - 예제 실행")
    print("=" * 50)
    print()
    
    arithmetic = Arithmetic()
    
    # 덧셈 예제
    print("1. 덧셈 (Addition)")
    print(f"   1 + 10 = {arithmetic.add(1, 10)}")
    print(f"   0 + 1 = {arithmetic.add(0, 1)}")
    print(f"   -1 + (-10) = {arithmetic.add(-1, -10)}")
    print()
    
    # 뺄셈 예제
    print("2. 뺄셈 (Subtraction)")
    print(f"   5 - 2 = {arithmetic.subtract(5, 2)}")
    print()
    
    # 곱셈 예제
    print("3. 곱셈 (Multiplication)")
    print(f"   -5 * -3 = {arithmetic.multiply(-5, -3)}")
    print(f"   0 * 10 = {arithmetic.multiply(0, 10)}")
    print()
    
    # 나눗셈 예제
    print("4. 나눗셈 (Division - 정수 나눗셈)")
    print(f"   5 / 2 = {arithmetic.divide(5, 2)}")
    print(f"   -10 / 2 = {arithmetic.divide(-10, 2)}")
    print()
    
    # 실수 나눗셈 예제
    print("5. 실수 나눗셈 (Quotient - 소수점 포함)")
    print(f"   5 ÷ 2 = {arithmetic.quotient(5, 2)}")
    print()
    
    # 예외 처리 예제
    print("6. 예외 처리 (Exception Handling)")
    try:
        result = arithmetic.divide(0, 0)
        print(f"   0 / 0 = {result}")
    except ArithmeticError as e:
        print(f"   0 / 0 → {type(e).__name__}: {e}")
    print()
    
    print("=" * 50)
    print("예제 실행 완료")
    print("=" * 50)


```


예제 코드 업데이트 완료. 최종 검증 진행.



모든 테스트 통과. README.md 체크리스트 업데이트 중.


```markdown
# Arithmetic Operations Module

## 프로젝트 개요

사칙연산 정확도 테스트를 위한 공통 모듈(Core Mathematical Module) 프로젝트입니다.
본 프로젝트는 TDD(Test-Driven Development) 방식인 RED-GREEN-REFACTOR 사이클을 따라 개발됩니다.

## 테스트 케이스 정보

- **테스트 케이스 ID**: TC-CMM-001 (Common Module / Core Mathematical Module)
- **기능 테스트 ID**: TC-AO-001 (Arithmetic Operations)
- **작성자**: 홍길동
- **승인자**: 박문수
- **문서 상태**: 최초 작성
- **버전**: v1.0
- **테스트 일자**: 2020-09-01
- **테스트 범위**: 공통 모듈

## 테스트 케이스

### 기본 사칙연산 테스트

| 테스트 케이스 | 예상값 | 중요도 | 상태 |
|--------------|--------|--------|------|
| 1 + 10 | 11 | 중요 | 성공 |
| 0 + 1 | 1 | 중요 | 성공 |
| 0 / 0 | 예외 발생 | 중요 | 성공 |
| -1 + (-10) | -11 | 보통 | 성공 |
| 5 - 2 | 3 | 중요 | 성공 |
| -5 * -3 | 15 | 보통 | 성공 |
| 5 / 2 | 2 | 중요 | 성공 |
| 5 ÷ 2 (quotient) | 2.5 | 보통 | 성공 |
| 0 * 10 | 0 | 낮음 | 성공 |
| -10 / 2 | -5 | 중요 | 성공 |

### 추가 테스트 사례

1. **예외 처리 확인**
   - `0 / 0` → `ArithmeticException` 예외 발생 확인

2. **다양한 조합**
   - 양수, 음수, 0을 포함한 다양한 테스트 케이스를 추가하여 연산의 정확도와 범위를 검증

3. **몫 계산 테스트 (quotient)**
   - 정수 나눗셈 대신 소수점을 포함한 결과를 테스트

## To-Do List : TDD 접근 방식

본 프로젝트는 **RED-GREEN-REFACTOR** 사이클을 따릅니다:

1. **RED**: 실패하는 테스트를 먼저 작성 ✅ _진행완료_
2. **GREEN**: 테스트를 통과하는 최소한의 코드 작성 🔄 _진행중_
3. **REFACTOR**: 코드를 개선하고 리팩토링 ⏳ _대기중_

### 개발 단계

```
[RED] → 테스트 작성 (실패) → [GREEN] → 코드 구현 (성공) → [REFACTOR] → 코드 개선
```

### GREEN 단계 작업 목록

#### 높은 우선순위 (중요도: 중요)

1. ✅ **`add(a, b)` 메서드 구현**
   - 양수 덧셈: `1 + 10 = 11`
   - 0 포함 덧셈: `0 + 1 = 1`
   - 음수 덧셈: `-1 + (-10) = -11`

2. ✅ **`subtract(a, b)` 메서드 구현**
   - 양수 뺄셈: `5 - 2 = 3`

3. ✅ **`divide(a, b)` 메서드 구현**
   - 정수 나눗셈 (버림 처리): `5 / 2 = 2`
   - 음수 나눗셈: `-10 / 2 = -5`

4. ✅ **예외 처리 구현**
   - `0 / 0` 시 `ArithmeticError` 예외 발생 처리

#### 중간 우선순위 (중요도: 보통)

5. ✅ **`multiply(a, b)` 메서드 구현**
   - 음수 곱셈: `-5 * -3 = 15`
   - 0 곱셈: `0 * 10 = 0`

6. ✅ **`quotient(a, b)` 메서드 구현**
   - 실수 나눗셈 (소수점 포함): `5 ÷ 2 = 2.5`

#### 구현 체크리스트

- [x] `Arithmetic` 클래스에 `add(a, b)` 메서드 추가 ✅
- [x] `Arithmetic` 클래스에 `subtract(a, b)` 메서드 추가 ✅
- [x] `Arithmetic` 클래스에 `multiply(a, b)` 메서드 추가 ✅
- [x] `Arithmetic` 클래스에 `divide(a, b)` 메서드 추가 (정수 나눗셈) ✅
- [x] `Arithmetic` 클래스에 `quotient(a, b)` 메서드 추가 (실수 나눗셈) ✅
- [x] `divide(a, b)` 메서드에 `0 / 0` 예외 처리 추가 ✅
- [x] 높은 우선순위 테스트 케이스 통과 확인 (7개) ✅
- [x] 중간 우선순위 테스트 케이스 통과 확인 (3개) ✅
- [x] 모든 테스트 케이스 통과 확인 (10개) ✅
- [ ] GREEN 단계 커밋 완료

## 프로젝트 구조

```
Arithmetic/
├── README.md
├── src/
│   └── (소스 코드)
├── test/
│   └── (테스트 코드)
└── (기타 설정 파일)
```

## 기능 요구사항

### 산술 연산 기능

- **덧셈 (Addition)**: 두 수의 합 계산
- **뺄셈 (Subtraction)**: 두 수의 차 계산
- **곱셈 (Multiplication)**: 두 수의 곱 계산
- **나눗셈 (Division)**: 두 수의 몫 계산
  - 정수 나눗셈: 정수 결과 반환
  - 실수 나눗셈 (quotient): 소수점 결과 반환
- **예외 처리**: 0으로 나누기 시 `ArithmeticException` 발생

## 실행 방법

(프로젝트 설정 후 업데이트 예정)

## 참고사항

이 테스트 케이스는 기능의 정확성과 예외 처리를 포함하여 클래스의 모든 기능을 검증합니다.


```


## 구현 완료 요약

### 구현된 기능 (중간 우선순위)

1. **`multiply(a, b)` 메서드** - 2개 테스트 통과
   - 음수 곱셈: `-5 * -3 = 15`
   - 0 곱셈: `0 * 10 = 0`

2. **`quotient(a, b)` 메서드** - 1개 테스트 통과
   - 실수 나눗셈 (소수점 포함): `5 ÷ 2 = 2.5`

### 최종 테스트 결과

- 통과: 10개 (모든 테스트 통과)
  - 높은 우선순위: 7개
  - 중간 우선순위: 3개
- 실패: 0개

### 추가 작업

- 예제 코드 업데이트: `multiply`와 `quotient` 예제를 `if __name__ == "__main__":` 블록에 추가

### 구현된 코드

`src/arithmetic.py`에 다음 메서드가 추가되었습니다:
- `multiply(a, b)` - 곱셈
- `quotient(a, b)` - 실수 나눗셈

모든 메서드에 docstring이 포함되어 있으며, linter 오류는 없습니다.

### GREEN 단계 완료

모든 기능 구현이 완료되었고, 10개 테스트가 모두 통과했습니다. GREEN 단계가 완료되었습니다. 다음 단계는 REFACTOR 단계입니다.

README.md의 체크리스트도 업데이트되었습니다.

---

**User**

첨부한 이미지 처럼 값을 입력 받아서 처리 할 수 있는 콘솔 프로그램을 만들어줘.

---

**Cursor**


이미지 예시에 맞춰 콘솔 프로그램을 구현합니다. 프로젝트 구조를 확인한 뒤 파일을 생성합니다.



이미지 예시에 맞춰 콘솔 프로그램을 생성합니다.


```python
"""
간단한 사칙연산 콘솔 프로그램
Arithmetic 클래스를 사용하여 사칙연산을 수행합니다.
"""

from src.arithmetic import Arithmetic


def get_integer_input(prompt):
    """정수 입력을 받는 함수"""
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("올바른 정수를 입력해주세요.")


def get_operator_input():
    """연산자 입력을 받는 함수"""
    valid_operators = ['+', '-', '*', '/', '÷']
    while True:
        operator = input("연산자>>").strip()
        if operator in valid_operators:
            return operator
        print(f"올바른 연산자를 입력해주세요. ({', '.join(valid_operators)})")


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


def format_result(a, operator, b, result):
    """결과를 포맷팅하는 함수"""
    # 연산자 표시 통일 (÷를 /로 변환)
    display_operator = operator if operator != '÷' else '/'
    return f"{a}{display_operator}{b}={result}입니다."


def main():
    """메인 함수"""
    print("=" * 50)
    print("간단한 사칙연산 콘솔 프로그램")
    print("=" * 50)
    print()
    
    arithmetic = Arithmetic()
    
    # 입력 화면
    print("[입력화면]")
    first_number = get_integer_input("첫번째 정수값>>")
    operator = get_operator_input()
    second_number = get_integer_input("두번째 정수값>>")
    print()
    
    # 결과 뷰 화면
    print("=" * 34)
    # 연산자 표시 통일
    display_operator = operator if operator != '÷' else '/'
    print(f"{first_number} {display_operator} {second_number}을 계산합니다.")
    print("=" * 34)
    
    try:
        result = calculate(arithmetic, first_number, operator, second_number)
        print(format_result(first_number, operator, second_number, result))
    except ArithmeticError as e:
        print(f"오류: {e}")
    except Exception as e:
        print(f"오류가 발생했습니다: {e}")


if __name__ == "__main__":
    main()

```


프로그램이 정상적으로 실행됩니다. 이미지 형식에 맞게 출력 형식을 조정 중입니다.



이미지 형식에 맞게 간소화 중입니다.


```python
"""
간단한 사칙연산 콘솔 프로그램
Arithmetic 클래스를 사용하여 사칙연산을 수행합니다.
"""

from src.arithmetic import Arithmetic


def get_integer_input(prompt):
    """정수 입력을 받는 함수"""
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("올바른 정수를 입력해주세요.")


def get_operator_input():
    """연산자 입력을 받는 함수"""
    valid_operators = ['+', '-', '*', '/', '÷']
    while True:
        operator = input("연산자>>").strip()
        if operator in valid_operators:
            return operator
        print(f"올바른 연산자를 입력해주세요. ({', '.join(valid_operators)})")


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


def format_result(a, operator, b, result):
    """결과를 포맷팅하는 함수"""
    # 연산자 표시 통일 (÷를 /로 변환)
    display_operator = operator if operator != '÷' else '/'
    return f"{a}{display_operator}{b}={result}입니다."


def main():
    """메인 함수"""
    arithmetic = Arithmetic()
    
    # 입력 화면
    first_number = get_integer_input("첫번째 정수값>>")
    operator = get_operator_input()
    second_number = get_integer_input("두번째 정수값>>")
    
    # 결과 뷰 화면
    print("=" * 34)
    # 연산자 표시 통일
    display_operator = operator if operator != '÷' else '/'
    print(f"{first_number} {display_operator} {second_number}을 계산합니다.")
    print("=" * 34)
    
    try:
        result = calculate(arithmetic, first_number, operator, second_number)
        print(format_result(first_number, operator, second_number, result))
    except ArithmeticError as e:
        print(f"오류: {e}")
    except Exception as e:
        print(f"오류가 발생했습니다: {e}")


if __name__ == "__main__":
    main()


```


이미지 형식에 맞게 콘솔 프로그램을 생성했습니다.

## 생성된 파일

**`main.py`** - 간단한 사칙연산 콘솔 프로그램

## 주요 기능

1. 입력 화면
   - 첫번째 정수값 입력
   - 연산자 입력 (+, -, *, /, ÷)
   - 두번째 정수값 입력

2. 결과 뷰 화면
   - 계산 과정 표시
   - 최종 결과 표시

3. 예외 처리
   - 잘못된 입력 처리
   - 0으로 나누기 오류 처리

## 사용 방법

```bash
python main.py
```

실행 후 다음과 같이 입력하면 됩니다:
```
첫번째 정수값>>10
연산자>>+
두번째 정수값>>30
```

결과:
```
==================================
10 + 30을 계산합니다.
==================================
10+30=40입니다.
```

## 지원하는 연산

- `+` : 덧셈 (add)
- `-` : 뺄셈 (subtract)
- `*` : 곱셈 (multiply)
- `/` 또는 `÷` : 정수 나눗셈 (divide)

프로그램이 준비되었습니다. 실행해 테스트해 보세요.

```shellscript
python main.py
```

```plaintext
첫번째 정수값>>10
연산자>>+
두번째 정수값>>30
```

```plaintext
==================================
10 + 30을 계산합니다.
==================================
10+30=40입니다.
```

