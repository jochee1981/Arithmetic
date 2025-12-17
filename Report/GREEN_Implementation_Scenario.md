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

