# 190722 Today I Learned

1. 마크다운 문서 작성 및 문법
2. MySQL 기초 문법
3. 각종링크

<!-- 주석확인후 공개하기-->
# 마크다운 문서 작성 및 문법

[참고문서](https://heropy.blog/2017/09/30/markdown/)
[참고문서2](https://gist.github.com/ihoneymon/652be052a0727ad59601)

# 제목
## 소제목
### 소소제목
#### 어디까지
##### 작아지나
###### 봅시다
####### ??6개까지만 되는 군요


* 목록
* 목록 2
    * 탭을누르고
        * 별표를 쓰면
            * 하위 목록이 생기는 매직(3개까지 다름)
            1. ul 이던 ol던 상관없습니다.

1. 목록은
2. 그냥
3. 쓰세요

*이탤릭체는 별표 한번*

**볼드는 별표 두번**

~~취소선은 ~두개 양옆에~~
테이블 | 만들기
-- | --
위의 -은 필수입니다 | 갯수는 2개이상 큰 상관이 없습니다
A| B

[링크](https://www.naver.com)
이때 https:// 은 필수입니다

![고양이액체설](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSi-15RixAD5iVHWPCw3s9z7a0CAY7R_oNotkdEcU4UkZVPXWAKFw)

이름은 안써도 []는 꼭 써야 합니다.이미지주소가 다소 더러운 건 함정입니다.

> 인용
> 인용 2
인용은 한번만 써도 되나봅니다. 엔터를 쳐서 구분하지 않는 이상 다 인용입니다.

***
별표 세개는 페이지 나누기 줄!




```sql
SELECT data
WHERE
```
 
 ![](./1.jpeg)
 ./=현재폴더 

주석은 goolged

<!-- 각주 -->

<sup>[1](#myfootnote1)</sup>

ddd[^1]

[^1]: This is the first footnote.
[^bignote]

dd<sup>1</sup>

<a name="myfootnote1">1</a>: Footnote content goes here


# MySQL 기초 문법


```sql
SELECT count(data)
FROM set
WHERE MOD(10,2) <>0
WHERE 10%2 <>0
SELECT DISTINCT
SELECT count(city)-count(distinct city)

```

```sql
select distinct s.city
from station as s
where s.city REGEXP 'a$|e$|i$|o$|u$'

```

```sql
select distinct s.city 
from station as s
where (city like 'a%'
    or city like 'e%'
    or city like 'i%'
    or city like 'o%'
    or city like 'u%')
and (city like '%a'
    or city like '%e'
    or city like '%i'
    or city like '%o'
    or city like '%u')
```

```sql
SELECT DISTINCT city 
FROM station
WHERE city not like 'a%'
and city not like 'i%'
and city not like 'e%'
and city not like 'u%'
and city not like 'o%'
```
# 각종링크
[선미님노션링크](https://www.notion.so/e1267aa9562844f6a5aae758b71f7b45)

[sql 테스트하는 곳](https://www.tutorialrepublic.com)

[정규표현식 스팀잇블로그](https://steemit.com/mysql/@seobangnim/mysql-regexp)

[해커랭크에서 문제풀기](https://www.hackerrank.com)

[w3school](https://www.w3schools.com)

[생활코딩 깃허브](https://opentutorials.org/course/3840)

[코랩사이트](https://colab.research.google.com)

[리플파이썬](https://repl.it/languages/python3)

[슬랙](https://dataitgirls.slack.com)

[3기 오늘은 어때?스프레드시트](https://docs.google.com/spreadsheets/d/1PU1Y_LcR0nGeoZXV7h_S97sq1Yaewo8Vzaezhe0-uq8/edit#gid=0)

[데잇걸즈 일정 스프레드시트](https://docs.google.com/spreadsheets/d/1JrB39AFlrOxcS0lxmnjb0nTDdl4j15jpzPbF8q6ZCgo/edit#gid=274467197)

[데잇걸즈 수업공지](https://docs.google.com/document/d/1gjjiOiMcLagoYy-SBN552mdy3lnxKLMzfr1gTi1upc0/edit#)