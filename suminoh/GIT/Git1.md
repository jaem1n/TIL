# Git & Github by egoing
## intro
지옥에서 온 Git<br>
창시자 ; 리노스토바이츠(리눅스)
리눅수 ; 30년이 된 프로젝트로 12000명이 오픈소르로 진행 
; 2000만줄의 코딩<br>
공부 ; 나의 문제 * 상상력 > 공부의 어려움? 구원 : 지옥<br>
사용성과 기능은 반비례 / 깃은 기능이 좋으나 사용성은 어려움
깃의 내부 매커니즘은 매우 심플함<br>
경제성있는 원리들

## Git없이 버전관리
인간이 수동화 할 수 있는 것만 자동화 할 수 있음
* 새폴더 (working) - work.txt 생성 - 새로운 버전 생성
* 버전을 만드는 것의 단점? 용량, 설명 빈약, 지저분한 파일 이름... <br>-> 버전관리 프로그램의 출현

## Git 
4가지 operation ; create / read / update / delete
### 사용법 1
#### sourcetree 이용 ; 버전 만들기, 기본 특징
* dropbox ; 버전이 쌓임 / 편하지만 쓸모없음 / 디텍토리 하나에 다 저장됨
* 버전관리 ; 각각의 버전을 정교하게 컨트롤해야 하는 프로젝트에 유용
* .git폴더(숨김폴더)에 히스토리 저장
* sourcetree 디렉토리 설정 - 텍스트파일 생성(수정) - unstaged file을 staged file로 add - 상세내용 입력 - commit
* 히스토리 확인 가능
* 단위 작업 / 하나의 기능(수정사항)이 끝났을 때 버전을 만드는 것이 효율적
* 깃은 파일의 수정사항을 추적한다. 
* 한 번이라도 커밋된 것은 관리 대상 / 한 번도 커밋되지 않은 것은 버전 관리 되지 않음
* ? 표시는 버전 관리되기 전의 파일임
* 사소한 변경사항도 한 눈에 알 수 있음
* 같은 작업을 수행한 파일 -> 같이 스테이지에 올려서 커밋 (하나의 버전에 여러 개의 파일을 포함시킴)
#### 용어
* repository = .git폴더<br> -> repository를 project folder라고 지칭할 수도 있으나 확실하게는 repository가 맞음
* working directory = .git directory를 제외한 나머지
* stage area = commit 시 해당 버전이 될 영역
* add = stage area에 추가하는 것<br> -> 커밋하면 stage area에 있는 것만 봄
![git](.\git.jpg)

### 사용법 2
#### 시간여행
* check out ; 이전 버전으로 들어가는 것 (버전을 선택하는 것)
* 브랜치 master에서 들어가고 싶은 버전 클릭
* 모든 파일이 commit된 상태에서만 가능
* 파일의 실제 내용이 이전 버전으로 변경됨
* master는 가장 최신버전을 가르키고 있음
* head는 check out한 버전을 가르키고 있음
* master를 더블클릭하면 head가 master를 가르킴<br> -> 검은색 동그라미로 표시됨
* <b>check out은 head를 옮김</b>
* check out하기 전 commit하면 head는 master를 가르킴

### 사용법 3
#### 폐기
* commit되지 않은 버전 - 폐기 가능
* 파일을 지웠을 때 - 폐기 가능

### 사용법 4
#### 부모버전, master와 head란?
* 각각의 버전은 그 부모버전(P)을 기록함
* commit의 40글자 텍스트 = commit의 식별자 = commit id <br> ex)d3f8fcf1bf244b3d180544839b8fce977de3d2c6
* master ; 마지막 버전이 무엇인지를 가르킴
* head ; working copy가 어느 버전에서 유래했는지를 가르킴
* <b>check out은 head를 옮김</b>
* 시간여행이 끝나면 master로 check out 해야 함
* head가 master가 아닌 다른 버전을 가르킬때 head가 master로 부터 detached됐다고 함
* head가 가르키는 버전이 부모버전이 된다. 
* git을 열면 head를 먼저 확인 -> master를 확인 -> 부모버전 확인

### 사용법 5
#### reset으로 버전 되돌리기
* 이전 버전으로 아예 되돌리고 싶을 때는 head를 check out한 후 master도 해당 버전으로 옮겨줘야 함
* reset ; 깃에게 해당 버전으로 reset하도록 하면 master를 옮김
* check out하면 head를 옮기고, reset하면 master를 옮김
* 해당 버전으로 reset하면 그 뒤의 버전은 삭제됨
* 이 커밋까지 현재 브랜치를 초기화(reset) -> Hard
* 그 상태에서 새로운 작업 / 새로운 버전을 다시 만들면 됨
* check out ; 시간여행 / reset ; 삭제
* reset은 delete보다 복합적인 개념이지만 삭제랑 비슷
* reset ; head가 가르키는 브랜치(master)를 바꾸는 것

### 사용법 6
#### reset으로 사라진 버전 다시 되살리기
* reset하기 전에 commit id를 보관
* terminal - git reset --hard commit id
* 실제로 버전을 영구삭제하기 위해서는 물리적인 저장소에 새로운 데이터를 덮어 씌워야함
