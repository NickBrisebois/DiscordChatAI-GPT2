PROG_NAME=chatai

build:
	docker build -t $(PROG_NAME) .

build-nogpu:
	docker build -t $(PROG_NAME)-nogpu . --file ./Dockerfile-nogpu
