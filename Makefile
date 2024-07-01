scrape:
	docker compose run --rm app python main.py

tail-logs:
	tail -f src/temp/cesal-scraper.log


check-code-quality:
	docker compose run --rm app ruff format . --check
	docker compose run --rm app ruff check .

apply-code-quality:
	docker compose run --rm app ruff format .
	docker compose run --rm app ruff check . --fix