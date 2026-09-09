# Этап 1
FROM golang:1.21-alpine AS builder

WORKDIR /app

COPY . .

RUN go mod init myapp

RUN go test -v ./...

RUN CGO_ENABLED=0 GOOS=linux go build -o myapp .

# Этап 2
FROM scratch
COPY --from=builder /app/myapp /myapp
ENTRYPOINT ["/myapp"]