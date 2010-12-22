%global libname Sys-Syscall

Name:           perl-%{libname}
Version:        0.23
Release:        2%{?dist}
Summary:        Access system calls that Perl doesn't normally provide access to
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/%{libname}/
Source0:        http://www.cpan.org/modules/by-module/Sys/%{libname}-%{version}.tar.gz
BuildArch:      noarch

Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

BuildRequires:  perl(Test::More)
BuildRequires:  perl(ExtUtils::MakeMaker)

%description
Use epoll, sendfile, from Perl. Mostly Linux-only support now, but more
syscalls/OSes planned for future.

%prep
%setup -q -n %{libname}-%{version}
pod2text < README.pod > README

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install PERL_INSTALL_ROOT=%{buildroot}

find %{buildroot} -type f -name .packlist -exec rm -f {} \;
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} %{buildroot}/*

rm -v %{buildroot}%{_mandir}/man3/Sys::README.3pm
rm -v %{buildroot}%{perl_vendorlib}/Sys/README.pod

%check
make test

%files
%defattr(-,root,root,-)
%doc CHANGES README
%{perl_vendorlib}/Sys
%{_mandir}/man3/Sys::Syscall.*

%changelog
* Wed Dec 22 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.23-2
- 661697 rebuild for fixing problems with vendorach/lib

* Thu Jun 24 2010 Ruben Kerkhof <ruben@rubenkerkhof.com> 0.23-1
- Upstream released new version

* Thu May 06 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.22-7
- Mass rebuild with perl-5.12.0

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 0.22-6
- rebuild against perl 5.10.1

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.22-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.22-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Feb 08 2008 Tom "spot" Callaway <tcallawa@redhat.com> 0.22-3
- rebuild for new perl

* Thu May 08 2007 Ruben Kerkhof <ruben@rubenkerkhof.com> 0.22-2
- Test::More added to BR (#239369)
* Mon May 07 2007 Ruben Kerkhof <ruben@rubenkerkhof.com> 0.22-1
- Specfile autogenerated by cpanspec 1.69.1.
