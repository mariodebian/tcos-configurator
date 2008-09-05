VERSION=$(shell head -1 debian/changelog 2>/dev/null | awk  '{gsub(/\(/,"",$$2); gsub(/\)/, "" , $$2); print $$2}' )

have_changelog := $(wildcard debian/changelog)
ifeq ($(strip $(have_changelog)),)
VERSION=$(shell head -1 ../debian/changelog 2>/dev/null | awk  '{gsub(/\(/,"",$$2); gsub(/\)/, "" , $$2); print $$2}' )
endif

all:
	#none

clean:
	find -name "*~" | xargs rm -f
	rm -f tcos-configurator.glade.bak tcos-configurator.gladep

test:
	@echo "TCOS_CONFIGURATOR VERSION="$(VERSION)


patch_version:
	# PATCHING VERSION
	sed -i 's/__VERSION__/$(VERSION)/g' tcos-configurator

patch_dapper: patch_version
	# PATCHING TcosMonitor in Ubuntu DAPPER
	sed -i '/^Build/s/5.0.37.2/5.0.7ubuntu13/g' debian/control

	sed -i '/\/usr\/bin\/env/s/python/python2.4/g' tcos-configurator

patch_edgy: patch_version
	sed -i '/\/usr\/bin\/env/s/python/python2.4/g' tcos-configurator

patch_feisty: patch_version

patch_gutsy: patch_version

patch_max: patch_version

patch_etch: patch_version
	sed -i '/\/usr\/bin\/env/s/python/python2.4/g' tcos-configurator

patch_unstable: patch_version

patch_testing: patch_version

patch_hardy: patch_version

patch_max: patch_version
	sed -i -e 's/Configurar servidor TCOS/Configurar servidor MAX/g' po/es.po
	sed -i -e 's/Configurador del servidor TCOS/Configurador del servidor MAX/g' po/es.po

patch_intrepid: patch_version


.PHONY:
