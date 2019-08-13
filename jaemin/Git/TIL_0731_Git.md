### git repository 만드는 방법
- git init
- view> palette> git initialize

<br>

### gistory
- 파이썬 기반 git 분석 도구
- .git 폴더 안에서 일어나는 일들(add, commit 등)을 사람이 볼 수 있는 형식으로 보여줌
- .\index : 여기에 파일 목록 나오는데 내용이 같은 파일들은 같은 id(56a6051…)를 가지고 있음
    - hash : 단방향암호화된 id. 파일 컨텐츠가 똑같으면 hash generator 알고리즘에 의해 어떤 컴퓨터에서든 똑같은 hash를 갖는다. (알고리즘 종류에 따라 다름) 
- .\head : commit 할 시점의 index가 여기에 적힘. tree commit id / parent id 적혀있음.
- cd .git > gistory > http://0.0.0.0:8805/

<br>

### 네이버 실시간검색어 페이지 소스코드 가져오기

1-1. 소스코드를 ‘naver.html’ 파일 안에 저장 후 커밋
```
curl -H "User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.89 Safari/537.36" https://datalab.naver.com/keyword/realtimeList.naver?where=main > naver.html && git add naver.html && git commit -m “naver update"
```
* && : 앞에 것이 실행되면 뒤에 것을 실행해라는 뜻 (&& 대신에 줄바꿈으로 해도 됨)

1-2. 5초마다 자동 갱신
```
while true
do
curl -H "User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.89 Safari/537.36" https://datalab.naver.com/keyword/realtimeList.naver?where=main > naver.html 
git add naver.html 
git commit -m “naver update”
sleep 5
done

# 멈출 때: ctrl+c
```

2. "sync.sh" 파일 안에 1번 내용을 저장한 후 명령어 "bash sync.sh" 입력

<br>

### git merge

- git merge exp : exp를 지금 head가 있는 곳(master)로 병합
- git branch -d exp : 병합 전에 이걸 쓰면 안전장치로 다시 한번 물어보며 대문자 D로 하라고 함. 병합 후에는 바로 먹힘.
- 충돌 났을 때 
    * accept current change : 현재 헤드가 가리키는 것(master)의 결과를 가져옴
    * accept incoming change : 들어온 것(exp)의 결과를 가져옴
    * accept both changes : 둘 다 
    * compare changes : 두 개를 병렬로 비교

- work.txt.orig : 파괴적인 작업 전에 자동으로 만들어진 안전장치 파일 (original)
- git merge —help : merge 사용법 보여줌

<br>

### vi(visual) editor 명령어  
- vi work2.txt : 파일 만들기
- I : 입력모드
- ctrl+c : 입력모드에서 명령어모드로 전환
- dd : 한 줄 삭제
- :w : 저장
- :q : 나가기
- :wq : 저장하고 나가기

<br>

### git을 이용해 백업하는 방법
- .git 폴더가 들어있는 폴더 전체를 드롭박스에 올리기
- github

<br>

### github 사용 방법

1. 깃허브에 remote repository를 만든다.
    - 주의사항: ssh로 설정!! 

2. 인증을 한다.
    - 한 컴퓨터에서 한 번만 하면 됨. 고유의 ssh-keygen (key generation) 생성
    - /Users/jaemin/.ssh 에서 ls -al >> cat id_rsa.pub (public 키는 공개 가능. 뒤에 .pub 안 붙은 id_rsa는 private이므로 절대 공개 ㄴㄴ)

3. local repository와 remote repository 연결
    - echo "# dataitgirls-remote" >> README.md : 내용이 담긴 readme.md 파일 생성
    - git remote add origin ssh주소: 지역저장소에게 원격저장소 주소 알려주기 (remote 관련 명령을 할거임. origin이라는 별명을 가진 주소를 add)
    - git push --set -upstream origin master : 원격저장소(upstream)의 브랜치를 로컬저장소의 master와 페어링하면서 푸시까지 하겠다.
    - git push -u origin master

4. local repository(home/me)에 commit

5. remote repository 로 push

6. local repository(office/other) 로 pull

<br>

### 2개 이상의 컴퓨터로 하나의 remote repository를 사용할 때 

- 디렉토리 복제부터 해야함 : git clone ssh주소

- 늦게 푸쉬하면 망한다! 다른 사람이 작업 해 놓은 것을 pull을 안하고 바로 내꺼 push 하면 거절당함. 

![github](remote.png)

**git pull 과 git fetch**
- 둘 다 끌어당기는 것이지만 차이가 있다.
- fetch: 기본적인 명령으로 원격 저장소의 파일을 다운만 받음. 
    * 지역저장소에는 어떠한 변화도 가하지 않음. 
    * 원격저장소와 저장소 내용 사이의 차이점을 알 수 있음. (git diff HEAD origin/master) 
    * origin/master와 (local/)master가 다른 곳을 가리키게 됨.
- pull = fetch + merge 

<br>

### 수련 방법: 짝 프로그래밍으로 github 연습
1. 프로젝트 폴더 만들기 (6일 동안 한명씩 돌아가면서)
2. vs code에 프로젝트 폴더를 등록
3. 프로젝트 폴더를 저장소로 만든다. git init
4. 새로운 파일을 만든다. (work.txt)
5. 스테이지로 등록한다. git add filename
6. 버전을 만든다. git commit -am “commit message”
7. 실험적인 프로젝트를 위해서 브랜치를 만든다. git branch exp
8. exp에서 작업을 진행한다. git checkout exp
9. 버전을 생성한다.
10. master에서 작업을 진행한다. git checkout master
11. 버전을 생성한다.
12. exp의 작업을 master로 병합한다. git checkout master && git merge exp
13. 충돌 상황을 재현해본다.
14. github에 원격 저장소를 만든다.
15. 지금까지 작업한 지역 저장소를 github의 원격 저장소에 등록한다. git remote add origin …
16. 지역 저장소를 업로드한다. git push
17. 각자의 컴퓨터에 지역 저장소를 복제한다. git clone…
18. 각자 작업해서 버전을 만들고 push를 동시에 해본다.
19. 생기는 상황을 같이 분석하고 해결한다.