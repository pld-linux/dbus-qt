#
%define		rname		dbus-qt3
#
Summary:	Qt-based library for using D-BUS
Summary(pl):	Biblioteka do u¿ywania D-BUS oparta o Qt
Name:		dbus-qt
Version:	0.70
Release:	0.1
# AFL v2.1 or GPL v2+, but Qt license enforces GPL
License:	GPL v2+
Group:		Libraries
Source0:	%{rname}-%{version}.tar.bz2
# Source0-md5:	9a8d4a4d560b49fb5ad034abfd3e3db5
Patch0:		%{name}-nolibs.patch
URL:		http://www.freedesktop.org/Software/dbus
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake
BuildRequires:	dbus-devel >= 0.91
BuildRequires:	libtool >= 2:1.5
BuildRequires:	qt-devel >= 6:3.1.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
D-BUS add-on library to integrate the standard D-BUS library with the
Qt thread abstraction and main loop. This is backport of old Qt3 API
from DBUS 0.70.

%description -l pl
Dodatkowa biblioteka D-BUS do integracji standardowej biblioteki D-BUS
z abstrakcj± w±tków i g³ówn± pêtl± Qt. Jest to stara implementacja z
API Qt3 dla DBUS 0.70.

%package devel
Summary:	Header files for Qt-based library for using D-BUS
Summary(pl):	Pliki nag³ówkowe biblioteki do u¿ywania D-BUS opartej o Qt
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	dbus-devel >= 0.91

%description devel
Header files for Qt-based library for using D-BUS.

%description devel -l pl
Pliki nag³ówkowe biblioteki do u¿ywania D-BUS opartej o Qt.

%package static
Summary:	Static Qt-based library for using D-BUS
Summary(pl):	Statyczna biblioteka do u¿ywania D-BUS oparta o Qt
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static Qt-based library for using D-BUS.

%description static -l pl
Statyczna biblioteka do u¿ywania D-BUS oparta o Qt.

%prep
%setup -qn %{rname}-%{version}
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--enable-qt3
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/libdbus*.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libdbus*.so
%{_libdir}/libdbus*.la
%{_includedir}/dbus-1.0/dbus/*

%files static
%defattr(644,root,root,755)
%{_libdir}/libdbus*.a
