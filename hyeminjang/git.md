# summary
1. remote1 - upstream - pull request
2. remote2 - origin - push
3. local - branch - add, commit

![git_image](users/user/downloads/git.jpg) 왜 안나오지?

# 
1. branch 생성 : git checkout -b [branch_name] upstream master
    * 뒤에 upstream master를 붙이면 최신 상태에서 branch 추가
2. upstream 업데이트 : git pull --rebase upstream master
    * if conflict : git rebase --continue
3. commit
4. git push origin [branch_name]
5. pull request
6. merge 확인
7. [다시] git pull --rebase upstream master 
8. merge 된 이후에는 branch 생성 가능 (안해도 무방)


# 
1. TIL 폴더 생성
2. 해당 폴더에 git clone [origin주소] .
3. branch 생성
4. branch로 checkout
5. TIL/ 안에 하위 폴더(e.g.hyeminjang) 만들기
6. commit
7. git push origin hyeminjang

# 
## reference
1. git remote add upstream [upstream 주소]
2. git reamote add origitn [origitn 주소]
3. vi [파일명] : 파일 내용 확인하기


