# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.22
# 
# >> macros
# << macros

Name:       mpc
Summary:    A multiprecision library
Version:    0.8.2
Release:    1
Group:      Development/Libraries
License:    LGPL2.1
URL:        http://www.multiprecision.org/
Source0:    http://www.multiprecision.org/mpc/download/%{name}-%{version}.tar.gz
Source1:    mpc-rpmlintrc
Source100:  mpc.yaml
Requires(post): /sbin/install-info
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/install-info
Requires(postun): /sbin/ldconfig
BuildRequires:  gmp-devel
BuildRequires:  mpfr-devel


%description
Mpc is a C library for the arithmetic of complex numbers with arbitrarily 
high precision and correct rounding of the result. It is built upon and 
follows the same principles as Mpfr. The library is written by Andreas 
Enge, Philippe Theveny and Paul Zimmermann and is distributed under r the
Gnu Lesser General Public License, either version 2.1 of the licence, or 
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
%setup -q -n %{name}-%{version}

# >> setup
# << setup

%build
# >> build pre
autoreconf --install --force
# << build pre

%configure --disable-static

# >> build post
make
# << build post
%install
rm -rf %{buildroot}
# >> install pre
# << install pre

# >> install post
%make_install
# << install post



%post
/sbin/ldconfig
%install_info --info-dir=%_infodir /usr/share/info/mpc.info.gz

%postun
/sbin/ldconfig
if [ $1 = 0 ] ;then
%install_info_delete --info-dir=%{_infodir} /usr/share/info/mpc.info.gz
fi





%files
%defattr(-,root,root,-)
# >> files
/usr/lib/libmpc.so
/usr/lib/libmpc.so.2
/usr/lib/libmpc.so.2.0.0
/usr/share/info/mpc.info.gz
# << files


%files devel
%defattr(-,root,root,-)
# >> files devel
/usr/include/mpc.h
# << files devel
