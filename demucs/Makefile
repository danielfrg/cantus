SHELL := bash
.ONESHELL:
.SHELLFLAGS := -eu -o pipefail -c
.DELETE_ON_ERROR:
MAKEFLAGS += --warn-undefined-variables
MAKEFLAGS += --no-builtin-rules


first: help


# ------------------------------------------------------------------------------
# Build

env:  ## Create Python environment
	mamba env create


download:  ## Download model
	cd $(CURDIR)/models; curl -O https://dl.fbaipublicfiles.com/demucs/v2.0/demucs_extra.th.gz
	cd $(CURDIR)/models; gunzip demucs_extra.th.gz


# ------------------------------------------------------------------------------
# Other


cleanall:  ## Clean everything
	echo "clean"


help:  ## Show this help menu
	@grep -E '^[0-9a-zA-Z_-]+:.*?##.*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?##"; OFS="\t\t"}; {printf "\033[36m%-30s\033[0m %s\n", $$1, ($$2==""?"":$$2)}'
