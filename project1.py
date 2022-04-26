print("hello world")



###
1. 초기화
# git init # 경로 폴더내 git 파일 생성

2. 추가할 파일 더하기
# git add . #모든파일
# git add project1.py #대상파일

3. 상태 확인
# git status 추가되거나 변경된 내용 확인

4. 히스토리 만들기
# git commit -m "freshment commit"

5. Github repository랑 내 로컬 프로젝트랑 연결
# git remote add origin https://github.com/Muramuradin/company-project.git
# 이 명령어는 github에서 복사해서 붙여와야함

6. 잘 연결되었는지 확인(선택사항)
# git remote -v
# 내가 연결한 주소가 뜨면 성공

7. Github 올리기
# git push origin master


### Github로 팀프로젝트 하는법 ###

1. Github에서 소스코드 다운로드
# git clone 주소 폴더이름
# 주소는 github에서 들고와야함
# 폳더 이름은 선택사항, 이름을 안줄경우 포르젝트 이름으로 폴더가 자동으로 생기고 그안에 코드가 다운로드

2. Github에서 내 브렌치(branch) 만들기
# git checkout -b 브렌치이름

3. 내 브렌치에 소스코드 입력하기
# git add .
# git commit -m "first commit"
# git push origin 브렌치이름

4. 마스터 브렌치에 소스 가져오기(Pull)
# git pull origin master
