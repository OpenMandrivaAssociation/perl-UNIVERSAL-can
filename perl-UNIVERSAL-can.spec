%define module  UNIVERSAL-can
%define name    perl-%{module}
%define version 1.12
%define release %mkrel 3

Name:           %{name}
Version:        %{version}
Release:        %{release}
Summary:        Hack around calling UNIVERSAL::can() as a function
License:        GPL or Artistic
Group:          Development/Perl
Url:            http://search.cpan.org/dist/%{module}
Source:         http://www.cpan.org/modules/by-module/UNIVERSAL/%{module}-%{version}.tar.bz2
%if %{mdkversion} < 1010
BuildRequires:  perl-devel
%endif
BuildRequires:  perl(Test::Warn)
BuildRequires:  perl(Test::Exception)
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}

%description
The UNIVERSAL class provides a few default methods so that all objects can use
them. Object orientation allows programmers to override these methods in
subclasses to provide more specific and appropriate behavior.

Some authors call methods in the UNIVERSAL class on potential invocants as
functions, bypassing any possible overriding. This is wrong and you should not
do it. Unfortunately, not everyone heeds this warning and their bad code can
break your good code.

Fortunately, this module replaces UNIVERSAL::can() with a method that checks to
see if the first argument is a valid invocant (whether an object -- a blessed
referent -- or the name of a class). If so, and if the invocant's class has its
own can() method, it calls that as a method. Otherwise, everything works as you
might expect.

If someone attempts to call UNIVERSAL::can() as a function, this module will
emit a lexical warning (see perllexwarn) to that effect. You can disable it
with no warnings; or no warnings 'UNIVERSAL::isa';, but don't do that; fix the
code instead.

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%{__make} test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%doc README
%{perl_vendorlib}/UNIVERSAL
%{_mandir}/*/*

