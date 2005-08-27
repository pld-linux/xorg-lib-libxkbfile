# $Rev: 3327 $, $Date: 2005-08-27 17:42:48 $
#
Summary:	xkbfile library
Summary(pl):	Biblioteka xkbfile
Name:		xorg-lib-libxkbfile
Version:	0.99.0
Release:	0.02
License:	MIT
Group:		X11/Libraries
Source0:	http://xorg.freedesktop.org/X11R7.0-RC0/lib/libxkbfile-%{version}.tar.bz2
# Source0-md5:	e696a2accee17d4a6ac73b746ca41e08
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 0.19
BuildRequires:	xorg-util-util-macros
BuildRoot:	%{tmpdir}/libxkbfile-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

%description
xkbfile library.

%description -l pl
Biblioteka xkbfile.


%package devel
Summary:	Header files libxkbfile development
Summary(pl):	Pliki nag³ówkowe do biblioteki libxkbfile
Group:		X11/Development/Libraries
Requires:	xorg-lib-libxkbfile = %{version}-%{release}
Requires:	xorg-lib-libX11-devel

%description devel
xkbfile library.

This package contains the header files needed to develop programs that
use these libxkbfile.

%description devel -l pl
Biblioteka xkbfile.

Pakiet zawiera pliki nag³ówkowe niezbêdne do kompilowania programów
u¿ywaj±cych biblioteki libxkbfile.


%package static
Summary:	Static libxkbfile libraries
Summary(pl):	Biblioteki statyczne libxkbfile
Group:		Development/Libraries
Requires:	xorg-lib-libxkbfile-devel = %{version}-%{release}

%description static
xkbfile library.

This package contains the static libxkbfile library.

%description static -l pl
Biblioteka xkbfile.

Pakiet zawiera statyczne biblioteki libxkbfile.


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
%attr(755,root,wheel) %{_libdir}/libxkbfile.so.*


%files devel
%defattr(644,root,root,755)
%{_includedir}/X11/extensions/*.h
%{_libdir}/libxkbfile.la
%attr(755,root,wheel) %{_libdir}/libxkbfile.so
%{_pkgconfigdir}/xkbfile.pc


%files static
%defattr(644,root,root,755)
%{_libdir}/libxkbfile.a
