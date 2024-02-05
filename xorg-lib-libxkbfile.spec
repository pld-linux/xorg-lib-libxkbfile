Summary:	xkbfile library - XKB file handling routines
Summary(pl.UTF-8):	Biblioteka xkbfile - funkcje do obsługi plików XKB
Name:		xorg-lib-libxkbfile
Version:	1.1.3
Release:	1
License:	MIT
Group:		X11/Libraries
Source0:	https://xorg.freedesktop.org/releases/individual/lib/libxkbfile-%{version}.tar.xz
# Source0-md5:	229708c15c9937b6e5131d0413474139
URL:		https://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake
BuildRequires:	libtool >= 2:2
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	tar >= 1:1.22
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-proto-kbproto-devel
BuildRequires:	xorg-util-util-macros >= 1.8
BuildRequires:	xz
Obsoletes:	xkbfile < 1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libxkbfile library is used by the X servers and utilities to parse the
XKB configuration data files.

%description -l pl.UTF-8
Biblioteka libxkbfile jest wykorzystywana przez serwery i narzędzia X
do analizy plików danych konfiguracyjnych XKB.

%package devel
Summary:	Header files for libxkbfile library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libxkbfile
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	xorg-lib-libX11-devel
Requires:	xorg-proto-kbproto-devel
Obsoletes:	xkbfile-devel < 1

%description devel
This package contains the header files needed to develop programs that
use libxkbfile.

%description devel -l pl.UTF-8
Pakiet zawiera pliki nagłówkowe niezbędne do kompilowania programów
używających biblioteki libxkbfile.

%package static
Summary:	Static libxkbfile library
Summary(pl.UTF-8):	Biblioteka statyczna libxkbfile
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
This package contains the static libxkbfile library.

%description static -l pl.UTF-8
Pakiet zawiera statyczną bibliotekę libxkbfile.

%prep
%setup -q -n libxkbfile-%{version}

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/libxkbfile.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog README.md
%attr(755,root,root) %{_libdir}/libxkbfile.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libxkbfile.so.1

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libxkbfile.so
%{_includedir}/X11/extensions/XKB*.h
%{_includedir}/X11/extensions/XKM*.h
%{_pkgconfigdir}/xkbfile.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libxkbfile.a
