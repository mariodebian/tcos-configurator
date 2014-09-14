LANGUAGES=es pt_BR gl fr
PACKAGE=tcos-configurator

all:


clean:
	@rm -f *.mo *.gmo *autosave
	@for lang in $(LANGUAGES); do \
		echo " **CLEAN** $$lang"; \
		rm -rf $$lang;\
	done

files: pot

pot:
	echo ../tcos-configurator.py > FILES.py.txt
	echo ../tcos-configurator.ui > FILES.ui.txt
	xgettext -o tcos-configurator.py.pot --files-from=FILES.py.txt --language=Python
	xgettext -o tcos-configurator.ui.pot --files-from=FILES.ui.txt --language=Glade
	msgcat -o tcos-configurator.pot tcos-configurator.py.pot tcos-configurator.ui.pot
	rm -f FILES.py.txt FILES.ui.txt tcos-configurator.py.pot tcos-configurator.ui.pot

po:
	@for lang in $(LANGUAGES); do \
		echo " **PO** $$lang"; \
		if [ ! -f $$lang.po ]; then \
			msginit --input $(PACKAGE).pot -o $$lang-old.po;\
		else \
			mv $$lang.po $$lang-old.po; \
		fi ; \
		msgmerge -o $$lang.po $$lang-old.po $(PACKAGE).pot; \
		rm -f $$lang-old.po; \
	done

gmo:
	@echo "Compiling languages: $(LANGUAGES)"
	@for lang in $(LANGUAGES); do \
		echo " **MO** $$lang" ; \
		mkdir -p $$lang/LC_MESSAGES/; \
		msgfmt -v -o $$lang/LC_MESSAGES/$(PACKAGE).mo $$lang.po; \
		touch $$lang.gmo; \
	done
	

install: gmo
	@for lang in $(LANGUAGES); do \
		echo " **INSTALL MO** $$lang" ; \
		mkdir -p $(DESTDIR)/$(PREFIX)/share/locale/$$lang/LC_MESSAGES/; \
		echo "    Installing $$lang.mo into $(DESTDIR)/$(PREFIX)/share/locale/$$lang/LC_MESSAGES/$(PACKAGE).mo"; \
		msgfmt -v -o $(DESTDIR)/$(PREFIX)/share/locale/$$lang/LC_MESSAGES/$(PACKAGE).mo $$lang.po; \
	done
