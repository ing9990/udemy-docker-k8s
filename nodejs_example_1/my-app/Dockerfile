# Hello world

# 파일 명: Dockerfile

# NODE 14버전에서 작업을 한다.
FROM node:14

# 컨테이너는 자체의 파일 시스템을 구성하고 있다.
# /app 이라는 디렉토리에서 작업한다.
WORKDIR /app

# /package.json 파일을 복사한다.
# 현재 디렉토리 to 컨테이너 내의 /app 디렉토리로 복사한다.
COPY package.json .

# npm install 명령어를 통해 필요한 의존성을 설치한다.
RUN npm install

# 나머지 파일들을 /app 디렉토리로 복사한다.
COPY . .

# 3000번 포트를 외부세계로 열어준다.
EXPOSE 3000

# node app.mjs 라는 명령어를 실행한다.
# node 명령어는 FROM에서 기초 이미지를 nodejs로 가져왔기 때문에 사용할 수 있다.
CMD ["npm", "start"]
