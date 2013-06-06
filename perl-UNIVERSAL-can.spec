%define upstream_name    UNIVERSAL-can
%define upstream_version 1.20120726
Name:		perl-%{upstream_name}
<<<<<<< HEAD
Version:	%perl_convert_version %{upstream_version}
Release:	3
=======
Version:	%perl_convert_version 1.20120726
Release:	1
>>>>>>> auto_update

Summary:	Hack around calling UNIVERSAL::can() as a function
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/UNIVERSAL/UNIVERSAL-can-1.20120726.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Test::Warn)
BuildRequires:	perl(Test::Exception)

BuildArch:	noarch

%description
The UNIVERSAL class provides a few default methods so that all objects can use
them. Object orientation allows programmers to override these methods in
subclasses to provide more specific and appropriate behavior.

Some authors call methods in the UNIVERSAL class on potential invocants as
functions, bypassing any possible overriding. This is wrong and you should not
do it. Unfortunately, not everyone heeds this warning and their bad code can
break your good code.

Fortunately, this upstream_name replaces UNIVERSAL::can() with a method that
checks to
see if the first argument is a valid invocant (whether an object -- a blessed
referent -- or the name of a class). If so, and if the invocant's class has its
own can() method, it calls that as a method. Otherwise, everything works as you
might expect.

If someone attempts to call UNIVERSAL::can() as a function, this module
will emit a lexical warning (see perllexwarn) to that effect. You can disable
it with no warnings; or no warnings 'UNIVERSAL::isa';, but don't do that; fix
the code instead.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL installdirs=vendor
%make

%check
%make test

%install
%makeinstall_std

%files 
%doc README
%{perl_vendorlib}/UNIVERSAL
%{_mandir}/*/*


%changelog
* Fri Jun 24 2011 Guillaume Rousse <guillomovitch@mandriva.org> 1.201.106.170-1mdv2011.0
+ Revision: 687005
- update to new version 1.20110617

* Fri Jun 17 2011 Guillaume Rousse <guillomovitch@mandriva.org> 1.201.106.140-1
+ Revision: 685752
- new version

* Fri Jan 15 2010 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 1.160.0-1mdv2011.0
+ Revision: 491635
- update to 1.16

* Thu Jan 14 2010 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 1.150.0-2mdv2010.1
+ Revision: 491286
- fix upstream bug #49580 - deep recursion on string overloading

* Tue Jul 07 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 1.150.0-1mdv2010.0
+ Revision: 393108
- update to 1.15
- fix license field

* Sun Jun 21 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.140.0-1mdv2010.0
+ Revision: 387864
- new version

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 1.12-6mdv2009.0
+ Revision: 242108
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Sat Sep 15 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.12-4mdv2008.0
+ Revision: 87065
- rebuild


* Tue Aug 29 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1.12-3mdv2007.0
- Rebuild

* Fri Apr 28 2006 Nicolas Lécureuil <neoclust@mandriva.org> 1.12-2mdk
- Fix SPEC according to Perl Policy
    - BuildRequires
    - Source URL

* Sat Apr 01 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1.12-1mdk
- New release 1.12

* Wed Mar 01 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1.11-1mdk
- New release 1.11

* Mon Jan 16 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1.03-1mdk
- New release 1.03

* Tue Dec 20 2005 Nicolas Lécureuil <neoclust@mandriva.org> 1.01-2mdk
- Add BuildRequires

* Thu Dec 15 2005 Guillaume Rousse <guillomovitch@mandriva.org> 1.01-1mdk
- New release 1.01

* Mon Oct 03 2005 Nicolas Lécureuil <neoclust@mandriva.org> 1.00-2mdk
- Fix BuildRequires

* Tue Sep 20 2005 Guillaume Rousse <guillomovitch@mandriva.org> 1.00-1mdk
- first mdk release


