%define		rname		dbus-qt3
Summary:	Qt-based library for using D-BUS
Summary(pl.UTF-8):	Biblioteka do używania D-BUS oparta o Qt
Name:		dbus-qt
Version:	0.70
Release:	5
# AFL v2.1 or GPL v2+, but Qt license enforces GPL
License:	GPL v2+
Group:		Libraries
Source0:	%{rname}-%{version}.tar.bz2
# Source0-md5:	9a8d4a4d560b49fb5ad034abfd3e3db5
Patch0:		%{name}-nolibs.patch
URL:		https://www.freedesktop.org/Software/DBusBindings
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

%description -l pl.UTF-8
Dodatkowa biblioteka D-BUS do integracji standardowej biblioteki D-BUS
z abstrakcją wątków i główną pętlą Qt. Jest to stara implementacja z
API Qt3 dla DBUS 0.70.

%package devel
Summary:	Header files for Qt-based library for using D-BUS
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki do używania D-BUS opartej o Qt
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	dbus-devel >= 0.91
Requires:	qt-devel >= 6:3.1.0

%description devel
Header files for Qt-based library for using D-BUS.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki do używania D-BUS opartej o Qt.

%package static
Summary:	Static Qt-based library for using D-BUS
Summary(pl.UTF-8):	Statyczna biblioteka do używania D-BUS oparta o Qt
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static Qt-based library for using D-BUS.

%description static -l pl.UTF-8
Statyczna biblioteka do używania D-BUS oparta o Qt.

%prep
%setup -qn %{rname}-%{version}
%patch -P0 -p1

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
%{_libdir}/libdbus-qt-1.so.*.*.*
%ghost %{_libdir}/libdbus-qt-1.so.1

%files devel
%defattr(644,root,root,755)
%{_libdir}/libdbus-qt-1.so
%{_libdir}/libdbus-qt-1.la
%{_includedir}/dbus-1.0/dbus/connection.h
%{_includedir}/dbus-1.0/dbus/dbus-qt.h
%{_includedir}/dbus-1.0/dbus/message.h
%{_includedir}/dbus-1.0/dbus/server.h

%files static
%defattr(644,root,root,755)
%{_libdir}/libdbus-qt-1.a
