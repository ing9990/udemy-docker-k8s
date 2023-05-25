FROM openjdk:11
WORKDIR /app
COPY . /app
RUN ./gradlew clean build
EXPOSE 8082
CMD ["./gradlew", "bootRun"]