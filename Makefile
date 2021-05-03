.PHONY: dev-up
dev-up:
	docker-compose up

.PHONY: dev-up-d
dev-up-d:
	docker-compose up -d

.PHONY: dev-down
dev-down:
	docker-compose down

.PHNY: dev-prompt
dev-prompt:
	docker exec -it website_web_1 bash