# Part2-구현) 시각

문제 유형: 완전 탐색
(완전 탐색: 가능한 경우의 수를 모두 검사해보는 탐색 방법)<br/>

### 알게된 점

Before: if ('3' in str(h)) or ('3' in str(m)) or ('3' in str(s))<br/>
After: if '3' in str(h) + str(m) + str(s)

다음과 같이 표현이 가능하다는 점을 알고 있자!
