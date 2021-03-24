STAGING_NAME = build-staging
DATE := $(shell date +"%Y-%m%d-%H%M%S")

all: prebuild build postbuild

prebuild:
	rm -rf $(STAGING_NAME)
	mkdir $(STAGING_NAME)

build:
	mkdir "$(STAGING_NAME)/app"
	find app/* -type d -exec mkdir "$(STAGING_NAME)/{}" \;
	find app/*.py app/*/*.py -type f -exec cp '{}' "$(STAGING_NAME)/{}" \;
	mkdir "$(STAGING_NAME)/data"
	find data/*.* -exec cp '{}' "$(STAGING_NAME)/{}" \;
	cp app.py "$(STAGING_NAME)"
	zip -r -D "build-$(DATE).zip" $(STAGING_NAME)

clean: postbuild
	rm -f build-*.zip

postbuild:
	rm -rf $(STAGING_NAME)