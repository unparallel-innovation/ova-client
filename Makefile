SHELL := /bin/bash

setup:
	@(\
	    python3 -m venv .venv && \
	    source .venv/bin/activate &&  \
	    python3 -m pip install -U pip && \
	    python3 -m pip install -U pygments && \
			python3 -m pip install -U flask && \
			python3 -m pip install -U requests && \
	    pip3 install -r requirements/common.txt \
	)
