Summary:	xkbfile library
Summary(pl):	Biblioteka xkbfile
Name:		xorg-lib-libxkbfile
Version:	0.99.1
Release:	0.1
License:	MIT
Group:		X11/Libraries
Source0:	http://xorg.freedesktop.org/releases/X11R7.0-RC1/lib/libxkbfile-%{version}.tar.bz2
# Source0-md5:	eb063c487334b68bde8c908479c99e8b
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-util-util-macros
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
xkbfile library.

%description -l pl
Biblioteka xkbfile.

%package devel
Summary:	Header files libxkbfile development
Summary(pl):	Pliki nagłówkowe do biblioteki libxkbfile
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	xorg-lib-libX11-devel

%description devel
xkbfile library.

This package contains the header files needed to develop programs that
use these libxkbfile.

%description devel -l pl
Biblioteka xkbfile.

Pakiet zawiera pliki nagłówkowe niezbędne do kompilowania programów
używających biblioteki libxkbfile.

%package static
Summary:	Static libxkbfile library
Summary(pl):	Biblioteka statyczna libxkbfile
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
xkbfile library.

This package contains the static libxkbfile library.

%description static -l pl
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
%doc ChangeLog
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
