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
