# Git & Gitbub by egoing

### 사용법 1
#### git을 사용할 수 있는 환경
* GUI(Graphical User Interface) ; 그래픽을 통해 작업할 수 있는 환경
* CLI(Command Line Interface) ; 명령어를 입력하여 작업함으로써 작업 수행
* CLI는 거의 모든 컴퓨터에서 가능, GUI는 개인 컴퓨터는 가능하고 서버시스템에서는 사용 안 함

### 사용법 2
#### VS code에서 CLI사용하기 
* Visual Studio code에는 CLI가 내장되어 있음
* Ctrl + j ; 프롬프트 창 실행
* view / command palette / select default shell / git bash<br> -> git bash ; terminal을 처음 켰을 때 bash로 뜨도록 설정
* Emulator (git bash) ; window에서 unix와 같은 명령어를 사용할 수 있도록 하는 것
* pwd ; 현재 위치 ; 내가 어디있는지 인지하는 것이 중요
* terminal mode는 등록한 폴더로 위치를 자동설정 시켜줌
* git bash는 위치를 수동으로 설정해줘야 함
* clear ; terminal 내역 지우기
* mkdir hello-dir ; hello-dir폴더 생성(MakeDirectory)
* cd hello-dir ; hello-dir로 위치 변경(ChangeDirectory)
* 절대경로 ; cd /c/Users/user/Desktop/project1 ; 전체 경로를 쓰는 것
* 상대경로 ; 부모 디렉으로 이동 cd ..; 해당 위치 내의 폴더로 이동 cd hello-dir ; 현재 디렉 . ; cd hello-dir은 ./가 생력되어 있는 것 ; ../..는 부모디렉의 부모디렉
* rm hello-dir ; hello-dir 삭제? ; 오류 ; 디렉토리 삭제X
* rm -r hello-dir ; hello-dir 디렉토리 삭제 ; 디렉토리 삭제하려면 -r옵션을 넣어줘야함
* rm -rf hello-dir ; 경고창 없이 삭제
* rm -rf / ; root dir 삭제 ; 망함
* . 현재디렉 ; ./ 현재디렉 ; / 루트디렉

### 사용법 3
#### VS code git 기본 사용법
* 동작방법 -옵션 ; 코멘드라인의 핵심문법
* git init ; 해당 폴더를 project folder로 버전관리
* ls ; 파일리스트
* ls -l ; 리스트, 자세히보기; 파일보유자 생성날짜 파일명<br> -> d.. ; directory, -.. ; directory 아님
* ls -a ; 모든 파일 보기
* ls -la ; 두 개의 옵션을 합쳐서 사용할 수 있음
* git status ; 깃의 현재 상태<br> -> 연습할 때 status 이용해서 상태 변화 확인해보기
* git add index.html ; stage area로 올리기
* git add index.html index2html ; 이처럼 두 개의 파일을 한 번에 stage에 add할 수 있음
* git add./ ; 현재 디렉토리의 모든 파일을 stage area로 옮김
* commit ; working copy의 스냅샷을 만드는 것
* git commit -m "work 1" ; 새로운 버전 commit ; m옵션은 버전설명옵션
* git commit ; m옵션을 주지 않으면 메세지를 입력할 새로운 창이 떠서 버전에 대한 설명을 길게 쓸 수 있음
* git commit -a "work 1" ;  a옵션은 commit전 add로 해주는 옵션 <br> -> tracked되고 있는 파일만 가능한 옵션
* <b>.gitignore ; .gitignore 파일에 password.txt를 적고 .gitignore를 commit하면 password.txt는 track되지 않음</b>
* password.txt.template ; 내용을 고쳐쓰더라도 형식만 track되게 하고 싶을 때는 passwork.txt.template 이용
* git log ; history를 볼 수 있음 <br> -> Q를 누르면 빠져나감
* git log --oneline ; 한 줄로 표시할 수 있음
* <b>git log --all ; 확인 필요</b>
* git reflog ; 결과 / 원인<br> -> 오른쪽이 원인이 돼서 head가 가르키는 id가 왼쪽에 나옴 <br> -> 모든 작업의 결과로 head가 가르키는 id를 볼 수 있으므로 모든 버전의 id를 확인할 수 있다. 
* state ; 현재 상태를 확인, log ; history를 확인
* 컨트롤 C ; cancel

### 사용법 4
#### VS code git - checkout사용법
* git checkout id ; head를 해당 버전으로 옮김
* git checkout master ; head를 다시 master로 옮김
* head가 가르키는 버전이 부모버전이 됨
* head라는 txt파일이 .git안에 물리적으로 들어있음
* head ; master를 가르킴 ; 나의 working copy가 어디서 유래되었는지 알려주는 것

### 사용법 5
#### VS code git - reset사용법
* master ; 방금 commit한 버전을 가르킴
* reset ; master를 바꿈
* git reset --hard id ; master를 옮기고 이 후 버전을 삭제
* git reset --hard id ; master를 옮기고 이 후의 버전으로 복원

### 사용법 6
#### branch 사용법
* 개념은 오래 전부터 있었지만 비싸고 위험하기 때문에 사용X
* 현업에서 대성공 -> 협업에서 널리 사용됨
* git branch exp ; branch exp를 만듦
* git branch ; branch를 볼 수 있음
* git checkout exp ; head를 exp로 옮김
* <b>head가 향한 곳에서 작업이 시작됨</b>
* head, exp vs head->exp ; detached vs branch
* 이전 버전으로 돌리면 바일도 삭제되는데 password와 같은 관리되지 않은 파일들은 삭제되지 않음
* git branch -d exp2 ; 브랜치 삭제<br> -> 현재 head가 향해있는 브랜치는 삭제되지 않음

### 사용법 7
#### merge 사용법
* master로 branch(exp)를 병합
1. git checkout master
2. git merge exp
3. fit merge를 하면 commit까지 자동으로 완료
4. 반대 방향이여도 병합결과는 같음
* 다른 파일을 수정하면 파일을 추가 
* 같은 파일 다른 방향을 수정하면 파일이 합쳐짐
* 같은 파일 같은 부분을 수정하면 그 부분은 수동으로 합쳐야 함 <br> -> complict 발생
* resolve using 'mine' ; 병합된 방향으로 충돌해결
* reselve using 'thier' ; 병합한 방향으로 충돌해결
* 2way merge는 master, exp만 비교
* 3way merge는 master, exp, base를 비교하여 더 효율절
* git의 merge는 3way merge를 사용
