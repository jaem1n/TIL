# Git by Ashal
* 버전 관리 도구
* 형상 관리 - 버전이 증가하는 것 이상의 관리를 해줌
* 타임머신 - 평행 우주 - 여러 작업 - 통합(Merge)
* Branch를 만드는 이유 - Merge를 하기 위해
## Git을 사용하는 이유?
* 여태까지 어떻게 바뀌었는지 히스토리를 쌓기 위해
* 모두가 접근 할 수 있게 해서 협업할 수 있도록
## Pull Request
* pull ; Fetch + Merge
* 내 브랜치를 받아서 합쳐줘
* git pull --rebase origin master ; 불필요한 merge를 막기 위해 --rebase 명령을 줌
## rebase
* 내 브랜치가 생성된 곳 = base
* base의 위치는 옮기는 것 = rebase
* head를 바꿔주는 곳이므로 head가 되기 원하는 곳에서 rebase를 하면 됨

## 매일 해야되는 루틴
1. branch생성 + checkout  
 -> git checkout -b 브랜치 이름 upstream/master
2. fetch
3. rebase (1,2 합쳐서 git pull --rebase upstream master)(status가 clean한 상태에서 해야 함)
4. 수정
5. add
6. commit
7. push origin 내 브랜치 이름
