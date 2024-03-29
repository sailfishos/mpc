Name:       mpc
Summary:    A multiprecision library
Version:    1.3.1
Release:    1
License:    LGPLv3+
URL:        http://www.multiprecision.org/
Source0:    %{name}-%{version}.tar.gz
Patch0:     disable_doc.patch
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
BuildRequires:  gmp-devel >= 5.0.0
BuildRequires:  mpfr-devel >= 4.1.0

%description
Mpc is a C library for the arithmetic of complex numbers with arbitrarily
high precision and correct rounding of the result. It is built upon and
follows the same principles as Mpfr. The library is written by Andreas
Enge, Philippe Theveny and Paul Zimmermann and is distributed under the
Gnu Lesser General Public License, either version 3 of the licence, or
(at your option) any later version.


%package devel
Summary:    Development tools for the MPC Library
Requires:   %{name} = %{version}-%{release}
Requires:   %{name} = %{version}-%{release}, gmp-devel, mpfr-devel

%description devel
The header files, documentation and static libraries for developing
applications using the MPC Library.


%prep
%autosetup -p1 -n %{name}-%{version}/%{name}

%build
autoreconf --install --force

%reconfigure --disable-static

%make_build

%install
%make_install

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%{_libdir}/libmpc.so.*

%files devel
%defattr(-,root,root,-)
%{_libdir}/libmpc.so
%{_includedir}/mpc.h

