Name:           perl-Sys-Syscall
Version:        0.23
Release:        3%{?dist}
Summary:        Access system calls that Perl doesn't normally provide access to
License:        GPL or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Sys-Syscall/
Source0:        http://www.cpan.org/modules/by-module/Sys/Sys-Syscall-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch

Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

BuildRequires:  perl(Test::More)
BuildRequires:  perl(ExtUtils::MakeMaker)

%description
Use epoll, sendfile, from Perl. Mostly Linux-only support now, but more
syscalls/OSes planned for future.

%prep
%setup -q -n Sys-Syscall-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

rm -v $RPM_BUILD_ROOT%{_mandir}/man3/Sys::README.3pm
rm -v $RPM_BUILD_ROOT%{perl_vendorlib}/Sys/README.pod

%check
make test

%clean
rm -rf $RPM_BUILD_ROOT

%check
make test

%files
%defattr(-,root,root,-)
%doc CHANGES README
%{perl_vendorlib}/Sys
%{_mandir}/man3/Sys::Syscall.*

%changelog
* Fri Jun 22 2012 Luis Bazan <lbazan@fedoraproject.org> 0.23-3
- New Upstream Version

* Thu May 08 2007 Ruben Kerkhof <ruben@rubenkerkhof.com> 0.22-2
- Test::More added to BR (#239369)
* Mon May 07 2007 Ruben Kerkhof <ruben@rubenkerkhof.com> 0.22-1
- Specfile autogenerated by cpanspec 1.69.1.
