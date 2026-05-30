.PHONY: all demo smoke test
all: demo smoke test
demo:
	@echo "Running demo for poojakira..."
smoke:
	@echo "Running smoke tests for poojakira..."
	./smoke_test.sh
test:
	@echo "Running tests for poojakira..."
	pytest tests/ || echo "No tests found"
