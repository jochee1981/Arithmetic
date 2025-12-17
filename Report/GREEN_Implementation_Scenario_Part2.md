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

