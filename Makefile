default:
	mkdir -p out
	zip -j out/tranq src/*.py
	echo '#!/usr/bin/env python' | cat - out/tranq.zip > out/tranq
	chmod 755 out/tranq

test:
	python -m unittest discover
