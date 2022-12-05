# 2022_12_05_Java_foreach

### for each 구조

- iterate는 루프를 돌릴 객체
- iterate의 요소 중 한개씩 var에 대입하여 for문 수행
- 값을 변경할 수 없음 → 객체의 값을 읽을 때 사용

```
for (type var: iterate) {
    body-of-loop
}
```

### 예시

```
String[] numbers = {"one", "two", "three"};

for(String number: numbers) {
    System.out.println(number);
}
```