default:
	mkdir -p out
	zip out/tranq src/*.py __main__.py
	echo '#!/usr/bin/env python' | cat - out/tranq.zip > out/tranq
	chmod 755 out/tranq

test:
	python -m unittest discover

autoformat:
	yapf -r -p -i src tests
