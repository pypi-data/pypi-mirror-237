#!/bin/bash

VERSION="1.0"
GIT="https://github.com/gary-1959/cashflex"
DOWNLOAD="$GIT/archive/refs/tags/$VERSION.tar.gz"
PACKAGE="Cashflex $VERSION"
BASE="cashflex-$VERSION"

FILE="$BASE.tar.gz"
INSTALL="$HOME"
if [ "$1" != '' ]; then
	if test -d $1; then
		INSTALL=$1
	else
		echo "Folder $1 does not exist!"
		exit 1
	fi
fi

read -n1 -s -r -p $"Installing $PACKAGE to $INSTALL/$BASE. OK to continue (y/N)? " KEY
echo

if [ "$KEY" != 'Y' ] && [ "$KEY" != 'y' ]; then
	exit 0
fi
if test -f /tmp/$FILE; then
	rm /tmp/$FILE
fi
echo "Downloading $FILE to /tmp"
wget "$DOWNLOAD" -O /tmp/$FILE

if ! test -f "/tmp/$FILE"; then
	echo "File download failed!"
	exit 1
fi
if test -d "$INSTALL/$BASE"; then
        mv "$INSTALL/$BASE" "$INSTALL/$BASE.$(date +'%Y-%m-%d_%H-%M-%S')"
fi

# extract files to installation point
tar -xf "/tmp/$FILE" --directory "$INSTALL"

# remove downloaded file
rm "/tmp/$FILE"

# create desktop file
DESKTOP="$HOME/Desktop/cashflex-$VERSION.desktop"
cat >"$DESKTOP" <<EOL
[Desktop Entry]
Name=Cashflex
Comment=Cashflex Money Manager
Path=$INSTALL/$BASE
Exec=python3 cashflex'
Terminal=false
Type=Application
Icon=$INSTALL/$BASE/icons/64x64/uk.co.contrelec.cashflex.svg
Categories=GNOME;Financial;
StartupNotify=false
StartupWMClass=cashflex
Name[en_US]=Cashflex Money Manager
Categories=GNOME;GTK;Utility;Core;)
EOL

# copy to local applications

cp -f "$DESKTOP" "$HOME/.local/share/applications"

# allow launching
gio set "$HOME/Desktop/cashflex-$VERSION.desktop" metadata::trusted true
chmod a+x "$HOME/Desktop/cashflex-$VERSION.desktop"

echo "Installation complete!"
echo "Visit $GIT for instructions on how to use this application."

exit 0
