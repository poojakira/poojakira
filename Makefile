.PHONY: all demo smoke test dashboard provenance

all: smoke

demo:
	@echo "Profile repository: README plus conservative evidence dashboard."

smoke: test dashboard provenance

test:
	python -m pytest tests -q -ra -W error

dashboard:
	python tools/build_security_dashboard.py

provenance: dashboard
	python tools/write_profile_provenance.py