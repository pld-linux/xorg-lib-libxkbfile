Summary:	xkbfile library
Summary(pl):	Biblioteka xkbfile
Name:		xorg-lib-libxkbfile
Version:	1.0.1
Release:	0.1
License:	MIT
Group:		X11/Libraries
Source0:	http://xorg.freedesktop.org/releases/X11R7.0/src/lib/libxkbfile-%{version}.tar.bz2
# Source0-md5:	6a2e1686fe07b0302f339048e01fb3f7
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
Summary:	Header files for libxkbfile library
Summary(pl):	Pliki nag��wkowe biblioteki libxkbfile
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	xorg-lib-libX11-devel

%description devel
xkbfile library.

This package contains the header files needed to develop programs that
use libxkbfile.

%description devel -l pl
Biblioteka xkbfile.

Pakiet zawiera pliki nag��wkowe niezb�dne do kompilowania program�w
u�ywaj�cych biblioteki libxkbfile.

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

Pakiet zawiera statyczn� bibliotek� libxkbfile.

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
