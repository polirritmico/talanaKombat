SHELL = /bin/bash

TARGET_BIN_NAME = talanaKombat
TARGET_FOLDER = deploy
FILES = __main__.py README.MD src/*.py docs/LICENSE.md
CFG_FILE = config.py

# ======================================================

default: zip make_bin deploy clean

zip:
	@echo -e "Building talanaKombat..."
	@zip $(TARGET_BIN_NAME)-TEMP.zip -r $(FILES) > /dev/null 2>&1

make_bin:
	@echo "#!/usr/bin/env python" | \
		   cat - $(TARGET_BIN_NAME)-TEMP.zip > $(TARGET_BIN_NAME)
	@chmod +x $(TARGET_BIN_NAME)
	@echo "Done"

deploy:
	@mv $(TARGET_BIN_NAME) $(TARGET_FOLDER)/
	@echo -e "Generated binary moved to '$(TARGET_FOLDER)'"

clean:
	@rm $(TARGET_BIN_NAME)-TEMP.zip
	@echo -e "Done"

