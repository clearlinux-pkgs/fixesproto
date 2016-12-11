#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : fixesproto
Version  : 5.0
Release  : 7
URL      : http://xorg.freedesktop.org/releases/individual/proto/fixesproto-5.0.tar.bz2
Source0  : http://xorg.freedesktop.org/releases/individual/proto/fixesproto-5.0.tar.bz2
Summary  : X Fixes extension headers
Group    : Development/Tools
License  : MIT
Requires: fixesproto-doc
BuildRequires : pkgconfig(xorg-macros)

%description
X Fixes Extension
The extension makes changes to many areas of the protocol to resolve
issues raised by application interaction with core protocol mechanisms
that cannot be adequately worked around on the client side of the wire.

%package dev
Summary: dev components for the fixesproto package.
Group: Development
Provides: fixesproto-devel

%description dev
dev components for the fixesproto package.


%package doc
Summary: doc components for the fixesproto package.
Group: Documentation

%description doc
doc components for the fixesproto package.


%prep
%setup -q -n fixesproto-5.0

%build
export LANG=C
%configure --disable-static
make V=1  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/X11/extensions/xfixesproto.h
/usr/include/X11/extensions/xfixeswire.h
/usr/lib64/pkgconfig/fixesproto.pc

%files doc
%defattr(-,root,root,-)
%doc /usr/share/doc/fixesproto/*
