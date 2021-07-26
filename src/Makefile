.DEFAULT_GOAL := help

REQUIREMENTS_DIR = requirements
objects = $(REQUIREMENTS_DIR)/base.txt $(REQUIREMENTS_DIR)/dev.txt $(REQUIREMENTS_DIR)/test.txt

requirements/%.txt: $(REQUIREMENTS_DIR)/%.in $(REQUIREMENTS_DIR)/base.in
	pip-compile $<

.PHONY: requirements
requirements: $(objects) ## Compile requirements with pip-compile

.PHONY: upgrade-requirements
upgrade-requirements: ## Upgrade and compile requirements with pip-compile --upgrade
	for file in $(REQUIREMENTS_DIR)/*.in; do \
		pip-compile --upgrade $$file; \
	done

.PHONY: sync-requirements
sync-requirements:
	pip-sync $(objects)

clean:
	rm $(objects)
