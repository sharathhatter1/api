.PHONY:  install test test-smoke test-e2e test-parallel clean report

install:
	pip install -r requirements.txt

test:
	python run_tests.py --env qa

test-smoke:
	python run_tests.py --env qa --markers smoke

test-e2e:
	python run_tests.py --env qa --markers e2e

test-parallel:
	python run_tests.py --env qa --parallel

test-staging:
	python run_tests.py --env staging

clean:
	rm -rf allure-results allure-report reports __pycache__ .pytest_cache
	find . -name "*.pyc" -delete

report:
	allure serve allure-results

help:
	@echo "Available commands:"
	@echo "  install      - Install dependencies"
	@echo "  test         - Run all tests"
	@echo "  test-smoke   - Run smoke tests only"
	@echo "  test-e2e     - Run E2E tests only"
	@echo "  test-parallel- Run tests in parallel"
	@echo "  clean        - Clean generated files"
	@echo "  report       - Serve Allure report"
 