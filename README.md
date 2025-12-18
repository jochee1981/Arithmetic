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

---

## 🔧 REFACTOR 단계 작업 목록

### PyQt6 GUI 계산기로 리팩토링 계획

본 프로젝트는 콘솔 프로그램에서 **PyQt6 GUI 애플리케이션**으로 리팩토링하며, **SOLID 원칙**과 **디자인 패턴**을 적용합니다.

#### STEP 1: 도메인 모델 분리 (Domain Layer) ✅

- [x] **Operation 추상 클래스 생성**
  - Strategy Pattern 적용
  - 연산자별 클래스 분리 (Addition, Subtraction, Multiplication, Division)
  - OCP(Open-Closed Principle) 준수

- [x] **연산 결과 Value Object 생성**
  - CalculationResult 클래스 구현
  - 불변 객체로 결과 캡슐화 (dataclass frozen=True)

**디렉토리 구조:**
```
src/
├── domain/
│   ├── operation.py              # Operation 추상 클래스 ✅
│   ├── calculation_result.py     # CalculationResult Value Object ✅
│   └── operations/
│       ├── addition.py           # 덧셈 연산 ✅
│       ├── subtraction.py        # 뺄셈 연산 ✅
│       ├── multiplication.py     # 곱셈 연산 ✅
│       └── division.py           # 나눗셈 연산 ✅
```

**테스트 결과:** ✅ 14개 테스트 모두 통과

#### STEP 2: 비즈니스 로직 계층 (Service Layer) ⏳

- [ ] **Calculator Service 클래스 생성**
  - 연산 로직과 UI 로직 분리
  - SRP(Single Responsibility Principle) 준수
  - 연산 전략 등록 및 관리

- [ ] **연산 로직 통합**
  - Operation Strategy 패턴으로 if-elif 체인 제거
  - 새로운 연산 추가 시 기존 코드 수정 불필요

**디렉토리 구조:**
```
src/
├── service/
│   └── calculator_service.py     # 계산기 비즈니스 로직
```

#### STEP 3: GUI 프레젠테이션 계층 (Presentation Layer) ⏳

- [ ] **PyQt6 의존성 추가**
  - requirements.txt에 PyQt6>=6.6.0 추가

- [ ] **Calculator Window 구현 (View)**
  - PyQt6로 계산기 UI 구현
  - 버튼 레이아웃 (0-9, +, -, *, /, =, C, .)
  - 디스플레이 영역 (수식 표시, 결과 표시)

- [ ] **Calculator Presenter 구현**
  - MVP(Model-View-Presenter) 패턴 적용
  - View와 Service 간 중재자 역할
  - 사용자 입력 이벤트 처리

**디렉토리 구조:**
```
src/
├── ui/
│   ├── calculator_window.py     # GUI View (PyQt6)
│   └── calculator_presenter.py  # Presenter (MVP)
```

#### STEP 4: 의존성 주입 및 테스트 ⏳

- [ ] **의존성 역전 적용 (DIP)**
  - 추상화에 의존하도록 설계
  - main_gui.py에서 의존성 조립

- [ ] **단위 테스트 작성**
  - Service 계층 테스트
  - Domain 계층 테스트
  - Presenter 로직 테스트

- [ ] **GUI 진입점 생성**
  - main_gui.py 파일 생성
  - 의존성 주입 컨테이너 역할

**최종 프로젝트 구조:**
```
Arithmetic/
├── main.py                       # 콘솔 버전 (레거시)
├── main_gui.py                   # GUI 진입점 (NEW)
├── requirements.txt              # PyQt6 의존성 추가
├── src/
│   ├── arithmetic.py             # 기존 산술 연산 클래스
│   ├── domain/                   # 도메인 계층 (NEW)
│   ├── service/                  # 서비스 계층 (NEW)
│   └── ui/                       # 프레젠테이션 계층 (NEW)
├── test/
│   ├── test_arithmetic.py        # 기존 테스트
│   └── test_calculator_service.py # 새로운 테스트 (NEW)
└── Report/
    └── Refactoring_Report.md     # 리팩토링 보고서 (NEW)
```

### SOLID 원칙 적용 체크리스트

- [ ] **SRP (Single Responsibility Principle)**
  - 각 클래스가 단일 책임만 가짐
  
- [ ] **OCP (Open-Closed Principle)**
  - 확장에는 열려있고, 수정에는 닫혀있음
  - 새로운 연산 추가 시 기존 코드 수정 불필요
  
- [ ] **LSP (Liskov Substitution Principle)**
  - 모든 Operation 구현체가 Operation을 대체 가능
  
- [ ] **ISP (Interface Segregation Principle)**
  - 최소한의 인터페이스만 제공
  
- [ ] **DIP (Dependency Inversion Principle)**
  - 상위 모듈이 하위 모듈이 아닌 추상화에 의존

### 디자인 패턴 적용 체크리스트

- [ ] **Strategy Pattern**
  - 연산 알고리즘을 캡슐화하고 교체 가능하게 구현
  
- [ ] **MVP Pattern**
  - Model(Service), View(Window), Presenter로 계층 분리
  
- [ ] **Dependency Injection**
  - 의존성을 외부에서 주입하여 결합도 감소

### Code Smell 제거 목록

- [ ] **Long Method 제거**
  - main() 함수의 여러 책임을 계층별로 분리
  
- [ ] **Switch Statement 제거**
  - if-elif 체인을 Strategy Pattern으로 대체
  
- [ ] **Feature Envy 제거**
  - 각 클래스가 자신의 데이터를 처리하도록 수정
  
- [ ] **Primitive Obsession 제거**
  - 연산자 문자열을 Operation 클래스로 캡슐화
  
- [ ] **Duplicated Code 제거**
  - 중복된 연산자 변환 로직 통합

---

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

### 의존성 설치

```bash
pip install -r requirements.txt
```

### 1. 콘솔 계산기 실행 (현재 버전)

```bash
python main.py
```

### 2. GUI 계산기 실행 (리팩토링 후)

```bash
python main_gui.py
```

*※ GUI 버전은 REFACTOR 단계 완료 후 실행 가능*

### 3. 테스트 실행

```bash
pytest
```

### 4. 커버리지 확인

```bash
pytest --cov=src --cov-report=html
```

## 참고사항

이 테스트 케이스는 기능의 정확성과 예외 처리를 포함하여 클래스의 모든 기능을 검증합니다.

