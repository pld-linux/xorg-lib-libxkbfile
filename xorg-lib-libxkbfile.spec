Summary:	xkbfile library
Summary(pl.UTF-8):   Biblioteka xkbfile
Name:		xorg-lib-libxkbfile
Version:	1.0.4
Release:	3
License:	MIT
Group:		X11/Libraries
Source0:	http://xorg.freedesktop.org/releases/individual/lib/libxkbfile-%{version}.tar.bz2
# Source0-md5:	12b4ceb5d42b520228b5fb40a96ae6c5
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-util-util-macros
Obsoletes:	xkbfile
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
xkbfile library.

%description -l pl.UTF-8
Biblioteka xkbfile.

%package devel
Summary:	Header files for libxkbfile library
Summary(pl.UTF-8):   Pliki nagłówkowe biblioteki libxkbfile
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	xorg-lib-libX11-devel
Obsoletes:	xkbfile-devel

%description devel
xkbfile library.

This package contains the header files needed to develop programs that
use libxkbfile.

%description devel -l pl.UTF-8
Biblioteka xkbfile.

Pakiet zawiera pliki nagłówkowe niezbędne do kompilowania programów
używających biblioteki libxkbfile.

%package static
Summary:	Static libxkbfile library
Summary(pl.UTF-8):   Biblioteka statyczna libxkbfile
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
xkbfile library.

This package contains the static libxkbfile library.

%description static -l pl.UTF-8
Biblioteka xkbfile.

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
	DESTDIR=$RPM_BUILD_ROOT \
	pkgconfigdir=%{_pkgconfigdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog
%attr(755,root,root) %{_libdir}/libxkbfile.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libxkbfile.so
%{_libdir}/libxkbfile.la
%{_includedir}/X11/extensions/*.h
%{_pkgconfigdir}/xkbfile.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libxkbfile.a
