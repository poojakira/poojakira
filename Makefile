PYTHON ?= python

.PHONY: all demo smoke test dashboard provenance verify lint format

all: smoke

demo:
	@echo "Profile repository: README plus conservative evidence dashboard."

smoke: test dashboard provenance

test:
	$(PYTHON) -m pytest tests -q -ra -W error

dashboard:
	$(PYTHON) tools/build_security_dashboard.py

provenance: dashboard
	$(PYTHON) tools/write_profile_provenance.py

verify: smoke

lint:
	$(PYTHON) -m ruff check tools tests

format:
	$(PYTHON) -m ruff format tools tests
