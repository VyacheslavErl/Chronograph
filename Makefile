.PHONY: install

install:
	@echo "Installing Chronograph..."
	install -d "$(DESTDIR)/usr/share/chronograph"
	install -Dm755 main.py "$(DESTDIR)/usr/share/chronograph/main.py"
	install -Dm644 CalendarWidget.py "$(DESTDIR)/usr/share/chronograph/CalendarWidget.py"
	install -Dm644 style.qss "$(DESTDIR)/usr/share/chronograph/style.qss"
