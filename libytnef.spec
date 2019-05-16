Summary:	C library for decoding application/ms-tnef e-mail attachments
Summary(pl.UTF-8):	Biblioteka C do dekodowania załączników e-maili typu application/ms-tnef
Name:		libytnef
Version:	1.9.3
Release:	1
License:	GPL v2+
Group:		Libraries
#Source0Download: https://github.com/Yeraze/ytnef/releases
Source0:	https://github.com/Yeraze/ytnef/archive/v%{version}/ytnef-%{version}.tar.gz
# Source0-md5:	60b7c26daa19a1246d077560b6862150
URL:		https://github.com/Yeraze/ytnef
BuildRequires:	autoconf >= 2.63
BuildRequires:	automake >= 1:1.9
BuildRequires:	libtool >= 2:2.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
C library for decoding TNEF streams (application/ms-tnef or
winmail.dat e-mail attachments) generated by Microsoft Outlook.

%description -l pl.UTF-8
Biblioteka C do dekodowania strumieni TNEF (załączników e-maili typu
application/ms-tnef lub o nazwie winmail.dat), generowanych przez
program Microsoft Outlook.

%package devel
Summary:	Header files for libytnef library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libytnef
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for libytnef library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libytnef.

%package static
Summary:	Static libytnef library
Summary(pl.UTF-8):	Statyczna biblioteka libytnef
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libytnef library.

%description static -l pl.UTF-8
Statyczna biblioteka libytnef.

%package -n ytnef
Summary:	Yerase's TNEF Stream Reader
Summary(pl.UTF-8):	Czytnik strumieni TNET autorstwa Yerase
# it's a continuation of separate subproject (ytnef.spec) ended at version 2.7
Epoch:		1
Group:		Applications/File
Requires:	%{name} = %{version}-%{release}

%description -n ytnef
Yerase's TNEF Stream Reader. Can take a TNEF Stream (winmail.dat)
sent from Microsoft Outlook (or similar products) and extract the
attachments, including construction of Contact Cards & Calendar
entries.

%description -n ytnef -l pl.UTF-8
Czytnik strumieni TNET autorstwa Yerase - potrafi przyjąć strumień
TNEF (winmail.dat) wysłany w programu Microsoft Outlook (lub
podobnego) i wydobyć załączniki, w tym tworzenie kart kontaktowych
oraz wpisów kalendarza.

# NOTE: don't place any subpackages after -n ytnef because of EPOCH setting

%prep
%setup -q -n ytnef-%{version}

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libytnef.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc ChangeLog
%attr(755,root,root) %{_libdir}/libytnef.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libytnef.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libytnef.so
%{_includedir}/mapi.h
%{_includedir}/mapidefs.h
%{_includedir}/mapitags.h
%{_includedir}/tnef-errors.h
%{_includedir}/tnef-types.h
%{_includedir}/ytnef.h
%{_pkgconfigdir}/libytnef.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libytnef.a

%files -n ytnef
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ytnef
%attr(755,root,root) %{_bindir}/ytnefprint
%attr(755,root,root) %{_bindir}/ytnefprocess
