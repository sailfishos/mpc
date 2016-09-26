Name:       mpc
Summary:    A multiprecision library
Version:    0.9
Release:    1
Group:      Development/Libraries
License:    LGPL3
URL:        http://www.multiprecision.org/
Source0:    http://www.multiprecision.org/mpc/download/%{name}-%{version}.tar.gz
Patch0:     disable_doc.patch
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
BuildRequires:  gmp-devel >= 4.3.2
BuildRequires:  mpfr-devel >= 2.4.2

%description
Mpc is a C library for the arithmetic of complex numbers with arbitrarily 
high precision and correct rounding of the result. It is built upon and 
follows the same principles as Mpfr. The library is written by Andreas 
Enge, Philippe Theveny and Paul Zimmermann and is distributed under the
Gnu Lesser General Public License, either version 3 of the licence, or 
(at your option) any later version.


%package devel
Summary:    Development tools for the MPC Library
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}
Requires:   %{name} = %{version}-%{release}, gmp-devel, mpfr-devel

%description devel
The header files, documentation and static libraries for developing
applications using the MPC Library.



%prep
%setup -q -n %{name}-%{version}/mpc
%patch0 -p1

%build
autoreconf --install --force

%reconfigure --disable-static

make

%install
rm -rf %{buildroot}

%make_install

%post
/sbin/ldconfig

%postun
/sbin/ldconfig

%files
%defattr(-,root,root,-)
%{_libdir}/libmpc.so.*

%files devel
%defattr(-,root,root,-)
%{_libdir}/libmpc.so
%{_includedir}/mpc.h

