
PYTHON=pypy3
DST_DIR=dist

build: $(DST_DIR)
	$(PYTHON) -m build

$(DST_DIR):
	mkdir -f $@

package:
	$(PYTHON) -m build

install_local:
	 $(PYTHON) -m pip install .

upload_test:
	twine upload -r testpypi dist/*

clean:
	rm -rf $(DST_DIR)/*
