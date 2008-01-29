Summary:	C library for decoding application/ms-tnef e-mail attachments
Summary(pl.UTF-8):	Biblioteka C do dekodowania załączników e-maili typu application/ms-tnef
Name:		libytnef
Version:	1.5
Release:	1
License:	GPL v2
Group:		Libraries
Source0:	http://dl.sourceforge.net/ytnef/%{name}-%{version}.tar.gz
# Source0-md5:	6c44b955f33cf714c75a7bbe895cc352
URL:		http://ytnef.sourceforge.net/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
C library for decoding application/ms-tnef e-mail attachments.

%description -l pl.UTF-8
Biblioteka C do dekodowania załączników e-maili typu
application/ms-tnef.

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

%prep
%setup -q

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
%{_libdir}/libytnef.la
%{_includedir}/*.h

%files static
%defattr(644,root,root,755)
%{_libdir}/libytnef.a
