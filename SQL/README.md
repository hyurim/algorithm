[SQL solution](https://leetcode.com/problem-list/database/)

---

[1.sql-파싱과-최적화](#📘-1-sql-파싱과-최적화)
[2.인덱스-기본](#📘-2-인덱스-기본)

## 📘 1. SQL 파싱과 최적화

DBMS 내부에서 프로시저를 작성하고 컴파일해서 실행 가능한 상태로 만드는 전 과정을 **SQL 최적화**라고 해.

---

#### 최적화 과정은 어떻게 되는데?

> 자 우리 세분화를 해보자.

### 🔹 1. SQL 파싱

사용자로부터 SQL을 전달받으면 가장 먼저 **SQL 파서**가 **파싱**을 진행하게 돼.

> Q. 그러면 SQL 파싱이 뭐야?
> A. SQL 문을 이루는 개별 구성요소를 분석해서 파싱 트리를 생성해.
> 그 다음에 문법적으로 오류가 없는지 확인`(Syntax)`하고, 의미상 오류가 없는지 확인`(Semantic)`하는거야.
> 즉, **파싱 트리 생성 → Syntax 체크 → Semantic 체크** 순서로 진행되는거지.

---

### 🔹 1.2 SQL 최적화

파싱이 끝나면, **SQL 옵티마이저(Optimizer)**가 **SQL 최적화**를 진행해.

> Q. SQL 옵티마이저가 뭐야?
> A. 아 그거는 미리 수집한 시스템 및 오브젝트 통계정보를 바탕으로 다행한 실행경로를 생성해서 비교한 후 가장 효율적인 하나를 선택하는거지.
> 즉, **DB 성능을 결정하는 가장 핵심적인 엔진 역할**이야.

---

### 🔹 1.3 로우 소스 생성

SQL 옵티마이저가 선택한 실행경로를 실제 실행 가능한 코드 또는 프로시저 형태로 변환하는 단계야.
**로우 소스 생성기(Row Source Generator)**가 그 역할을 맡아.

---

## 📘 2. 인덱스 기본

---

### 2.1 인덱스 구조 및 탐색

인덱스 탐색은 **수직적 탐색**과 **수평적 탐색**, 두 단계로 나뉘어.

> SQL 튜닝은 **랜덤 Input/Output(이하 I/O)**와의 전쟁이야.
> DB 성능이 느린 이유는 **디스크 I/O** 때문이야. 왜냐하면 읽어야 할 데이터량이 많은데 그 과정에 디스크 I/O가 많이 발생할 때 느려져.
> 인덱스를 많이 사용하는 **OLTP 시스템**이라면 디스크 I/O 중에서도 랜덤 I/O가 특히 중요해.

#### Q. OLTP가 뭐야?

> A. Online Transcation Processing의 줄임말로 온라인 거래 처리 시스템을 의미해.
> 사용자의 실시간 데이터 처리를 중심으로 설계된 DB 시스템 또는 응용 프로그램을 말해
> 특징으로는 짧고 빈번한 트랜잭션과 즉각적인 응답 속도 요구, 정규화된 DB 구조 사용, 데이터의 정확성과 무결성이 매우 중요해. 또한, 동시성 처리가 매우 중요해.

> 추가로 DBMS가 제공하는 많은 기능이 느린 랜덤 I/O를 극복하기 위해서 개발된 거 알아?
> IOT, 클러스터, 파티션에서부터, Prefetch, Batch I/O처럼 숨은 기능과 소트머지 조인, 해시 조인 메소드 같은 것도 결국 랜덤 I/O를 극복하기 위해서 개발된 기능인 만큼 랜덤 I/O가 매우 중요해.

#### 📍 인덱스 탐색 2단계

| 단계            | 설명                           |
| --------------- | ------------------------------ |
| **수직적 탐색** | 인덱스 스캔 **시작 지점 찾기** |
| **수평적 탐색** | 조건에 맞는 **데이터 찾기**    |

---

### 🔹 2.2 인덱스 기본 사용법

- 인덱스 기본 사용법은 인덱스를 Range Scan 하는 방법을 의미해.

인덱스 컬럼을 가공하지 않아야 인덱스를 정상적으로 사용할 수 있어.

#### Q. 왜 인덱스를 가공하면 사용이 안돼?

> A. 먼저, 정상적으로 사용한다는 것은 리프 블록에서 스캔 시작점을 찾아 거기서부터 스캔하다가 중간에 멈추는 것을 의미해.
> **인덱스 컬럼을 함수/연산 등으로 가공하면** 인덱스의 정렬 구조를 사용할 수 없게 돼.
> 사용은 할 수 있지만, **스캔 시작점을 찾을 수 없어** 결국 리프 블록 전체를 스캔하게 되는거지.
> 즉, **Index Full Scan** 방식으로 작동하게 되는거고, 결국 성능이 떨어지기 때문에 튜닝의 효과는 사라져.

- '인덱스 칼럼을 가공하면 인덱스를 정상적으로 사용할 수 없다.' 라는 말은 공부하면서 들어봤지? 이유는 앞서 설명한 것과 같아.
  왜 그러는지 이유를 잘 모르고 '아 저렇구나' 라고만 알고 있는 경우가 많은데
  > 그 이유는 `인덱스 스캔 시작점을 찾을 수 없기 때문`이야. 함수, 연산, 가공이 들어가면 인덱스 구조의 정렬성이 상실되서 결국에는 Index Full Scan이 적용돼.

인덱스를 Range Scan 하기 위한 가장 첫 번째 조건은 인덱스 선두 컬럼이 조건절에 있어야 돼. 물론 가공하지 않은 상태여야 돼.

#### Q. 근데 Range Scan 하면 성능이 무조건 좋아져?

> A. 아니. 항상 성능이 좋아지는 건 아니야.

#### Q. 그러면 조건절이 아니라 ORDER BY나 SELECT-LIST에서 컬럼을 가공하면 사용할 수 있어?

> A. 음.. 일단 결론만 말하면 대부분 인덱스를 사용할 수 없어.
> 예시를 들어줄게

```
SELECT *
FROM table
WHERE SUBSTR(name, 1, 1) = '임'
ORDER BY birth_date || address;
```

이런 식으로 사용한다고 하면
`WHERE SUBSTR(name, 1, 1) = '임'`의 경우는 가공된 조건이기 때문에 인덱스를 사용하지 못해
`ORDER BY birth_date || address`의 경우는 문자열 연산이 들어가기 때문에 정렬도 인덱스를 사용하지 못해

### 2.3 인덱스 확장 기능 사용법

자 이제까지 Index Range Scan 중심으로 기본 사용법을 알아봤는데 이거 말고도 여러가지 있어.
예시를 들면 Index Full Scan, Index Unique Scan, Index Skip Scan, Index Fast Full Scan 등이 있어.

이제부터 정리해보자

---

#### Index Range Scan

B\*Tree 인덱스의 가장 일반적이고 정상적인 형태의 액세스 방식이야.

#### Q. B\*Tree는 뭐야?

> A. Balance Tree의 한 종류로 DB에서 데이터를 빠르게 찾기 위해 사용하는 인덱스 구조인데 대부분의 RDBMS에서 기본 인덱스 구조로 사용해.
> 모든 리프 노드가 동일한 깊이를 가지기 때문에 탐색 속도가 일정해
> 키 값들이 오름차순으로 정렬되어 있고, 범위 조건에 효율이 좋아.
> 한 노드에 여러 키와 포인터를 담아 디스크 접근을 줄여서 I/O가 최소화 되는거지.

---

#### Index Full Scan

이건 수직적 탐색 없이 인덱스 리프 블록을 처음부터 끝까지 수평적으로 탐색하는 방식이야.
데이터 검색을 위한 최적의 인덱스가 없을 때 차선으로 선택되는거야.

#### Q. 그럼 효용성은 어때?

> A. 인덱스 선두 컬럼이 조건절에 없으면 옵티마이저는 먼저 Table Full Scan을 고려해, 근데 대용량 테이블이면 부담이 크기 때문에 옵티마이저는 인덱스 활용을 다시 고려하지 않을 수 없어.

#### Q. 그러면 언제 쓰는거야?

> A. 인덱스는 테이블보다 저장 면적이 작아서, 전체를 스캔하더라도 오히려 유리한 경우가 있어.
> 데이터 저장 공간은 컬럼 길이 × 레코드 수로 결정되는데,
> 인덱스는 일부 컬럼만 포함하므로 전체 테이블보다 훨씬 작아.
> 그래서 아래와 같은 경우엔 Range Scan이 안 되더라도 인덱스를 쓰는 게 유리해:
> 인덱스에서 먼저 필터링이 가능하고
> 실제 테이블 접근을 최소화할 수 있는 경우
> 다만, 이런 성능을 끌어내려면 조건절에 사용하는 컬럼이 인덱스의 선두 컬럼이 되도록 설계하는 것이 중요해.

#### 소트 연산 생략

인덱스를 Full Scan하면 Range Scan과 마찬가지로 결과 집합이 인덱스 컬럼 순으로 정렬되는데 Sort Order By 연산을 생략할 목적으로 사용할 수도 있어.
이때는 차선책이 아니라 옵티마이저가 전략적으로 선택한 경우에 해당해.

#### Q. 어떨 때 쓰는거야?

> A. 소트 연산을 생략함으로써 전체 집합 중 일부를 빠르게 출력할 목적으로 옵티마이저가 Index Full Scan 방식을 선택한거야.

```
SELECT *
FROM users
ORDER BY name
FETCH FIRST 10 ROWS ONLY;
```

> 이런 경우에는 부분범위 처리가 가능한 상황에서 극적인 성능 개션 효과를 가져다줘

#### 하지만 주의할 점이 있어.

데이터를 전부 읽을 경우에는 Table Full Scan 보다 훨씬 더 많은 I/O를 일으키기 때문에 속도는 훨씬 느려져. 이 부분은 확실히 조심해야돼.

---

#### Index Unique Scan

이건 Index Full Scan와 달리 수직적 탐색만으로 데이터를 찾는 스캔 방식이야
Unique 인덱스를 `=`조건으로 탐색하는 경우에 작동해

```
SELECT *
FROM users
WHERE user_id = 123;
```

에서 만약에 user_id가 UNIQUE 인덱스 인 경우에 Index Unique Scan을 사용해서 한 번에 해당 레코드를 찾아가는거지

---

#### Index Skip Scan

이건 오라클 9i 버전에서부터 사용되는건데 `인덱스 선두 컬럼의 Distinct Value 개수가 적고 후행 컬럼의 Distinct Value 개수가 많을 때 유용해

루트 또는 브랜치 블록에서 읽은 컬럼 값 정보를 이용해 조건절에 부합하는 레코드를 포함할 `가능성이 있는` 리프 블록만 골라서 액세스 하는 스캔 방식이야.

> Index Range Scan이 불가능하거나 효율적이지 못한 상황에서 종종 빛을 발해.
> 그리고 부분범위 처리가 가능하면 `Index Full Scan`이 도움이 되기도 해.
> 하지만 이게 최선책이 될 수는 없어 `Index Range Scan`이 목표가 되도록 설계해야 해.
> 수행 횟 수가 적은 SQL은 인덱스를 추가하는 것이 비효율적인 경우가 있는데 이때 위에서 말한 방식을 차선책으로 활용하는게 좋아

---

#### Index Fast Full Scan

말 그대로 Index Full Scan 보다 빨라.
이유는 논리적인 인덱스 트리 구조를 무시하고 인덱스 세그먼트 전체를 Multiblock I/O 방식으로 스캔하기 때문이야

#### Q. Multiblock I/O 방식은 뭐야?

> A. 한 번의 I/O 작업으로 여러 개의 데이터 블록(block) 을 한꺼번에 읽는 방식이야

이건 디스크로부터 대량의 인덱스 블록을 읽어야 할 때 큰 효과를 발휘해, 속도는 빠르지만, 인덱스 리프 노드가 갖는 연결 리스트 구조를 무시한 채 데이터를 읽기 때문에 결과집합이 인덱스 키 순서대로 정렬되지 않아.
그리고 쿼리에 사용한 컬럼이 모두 인덱스에 포함돼 있을 때만 사용할 수 있어.
인덱스가 파티션 되어있지 않아도 병렬쿼리가 가능한 것도 중요해.
병렬 쿼리 때는 Direct Path I/O 방식을 사용하기 때문에 I/O 속도가 더 빨라져.

#### Q. Direct Path I/O는 뭐야?

> A. Buffer Cache를 거치지 않고, 디스크에서 사용자 프로세스가 직접 데이터를 읽거나 쓰는 방식이야.
> 그리고 CPU, 캐시 오버헤드가 줄어들어.
> 근데 캐시를 안거치기 때문에 재사용이 불가능해. 따라서 자주 사용하는 데이터에는 비효율적이고, 일회성 대량 처리 시에 유리해

#### 그러면 Buffer Cache는 뭐야?

> A. DB 서버 메모리 영역 중 하나로, 디스크에서 읽어온 데이터를 임시로 저장해두는 공간이야
> 자주 사용하는 데이터를 여기서 읽고 쓰게 되면 디스크 접근(I/O) 없이 빠르게 처리할 수 있어.
> 디스크는 느리기 때문에 한 번 읽은 걸 메모리에 남겨서 다음에 또 읽을 때 디스크 접근을 피하는 것이 목적이야
> 성능 향상을 위한 캐시 메모리야.

---

#### Index Range Scan Descending

Index Range Scan과 기본적으로 동일한 스캔 방식이야.
근데 다른건 `뒤에서 앞쪽으로 스캔하기 때문에 내림차순으로 정렬된 결과 집합을 얻는다`는 점만 달라

### 3. 테이블 엑세스 최소화

#### Q. 인덱스를 스캔하는 이유가 뭐야?

> A. 검색 조건을 만족하는 소량의 데이터를 인덱스에서 빨리 찾고 거기서 테이블 레코드를 찾아가기 위한 주소값, 즉 ROWID를 얻으려는 데 있어.

#### Q. ROWID가 뭔데?

> A. ROWID는 테이블에서 행의 위치를 지정하는 논리적인 주소값이야.
> DB 전체에서 중복되지 않는 유일한 값으로, 테이블에 새로운 행이 삽입되면 테이블 내부에서 자동으로 생성돼.
