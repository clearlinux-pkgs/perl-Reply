#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cpan
#
Name     : perl-Reply
Version  : 0.42
Release  : 21
URL      : https://cpan.metacpan.org/authors/id/D/DO/DOY/Reply-0.42.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/D/DO/DOY/Reply-0.42.tar.gz
Summary  : 'read, eval, print, loop, yay!'
Group    : Development/Tools
License  : MIT
Requires: perl-Reply-bin = %{version}-%{release}
Requires: perl-Reply-license = %{version}-%{release}
Requires: perl-Reply-man = %{version}-%{release}
Requires: perl-Reply-perl = %{version}-%{release}
Requires: perl(App::Nopaste)
Requires: perl(B::Keywords)
Requires: perl(Carp::Always)
Requires: perl(Class::Refresh)
Requires: perl(Config::INI::Reader::Ordered)
Requires: perl(Data::Dump)
Requires: perl(Data::Printer)
Requires: perl(File::HomeDir)
Requires: perl(PadWalker)
Requires: perl(Proc::InvokeEditor)
Requires: perl(Term::ReadKey)
BuildRequires : buildreq-cpan
BuildRequires : perl(Config::INI::Reader)
BuildRequires : perl(Config::INI::Reader::Ordered)
BuildRequires : perl(Data::OptList)
BuildRequires : perl(Devel::LexAlias)
BuildRequires : perl(Eval::Closure)
BuildRequires : perl(File::HomeDir)
BuildRequires : perl(File::Which)
BuildRequires : perl(Mixin::Linewise::Readers)
BuildRequires : perl(Module::Implementation)
BuildRequires : perl(Module::Runtime)
BuildRequires : perl(Package::Stash)
BuildRequires : perl(PadWalker)
BuildRequires : perl(Params::Util)
BuildRequires : perl(PerlIO::utf8_strict)
BuildRequires : perl(Sub::Exporter)
BuildRequires : perl(Sub::Install)
BuildRequires : perl(Try::Tiny)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
This archive contains the distribution Reply,
version 0.42:
read, eval, print, loop, yay!

%package bin
Summary: bin components for the perl-Reply package.
Group: Binaries
Requires: perl-Reply-license = %{version}-%{release}

%description bin
bin components for the perl-Reply package.


%package dev
Summary: dev components for the perl-Reply package.
Group: Development
Requires: perl-Reply-bin = %{version}-%{release}
Provides: perl-Reply-devel = %{version}-%{release}
Requires: perl-Reply = %{version}-%{release}

%description dev
dev components for the perl-Reply package.


%package license
Summary: license components for the perl-Reply package.
Group: Default

%description license
license components for the perl-Reply package.


%package man
Summary: man components for the perl-Reply package.
Group: Default

%description man
man components for the perl-Reply package.


%package perl
Summary: perl components for the perl-Reply package.
Group: Default
Requires: perl-Reply = %{version}-%{release}

%description perl
perl components for the perl-Reply package.


%prep
%setup -q -n Reply-0.42
cd %{_builddir}/Reply-0.42

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} -I. Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Reply
cp %{_builddir}/Reply-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/perl-Reply/4b8973752a2f9e93d3abb6f77d17bb9385fb9064 || :
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/reply

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Reply.3
/usr/share/man/man3/Reply::App.3
/usr/share/man/man3/Reply::Config.3
/usr/share/man/man3/Reply::Plugin.3
/usr/share/man/man3/Reply::Plugin::AutoRefresh.3
/usr/share/man/man3/Reply::Plugin::Autocomplete::Commands.3
/usr/share/man/man3/Reply::Plugin::Autocomplete::Functions.3
/usr/share/man/man3/Reply::Plugin::Autocomplete::Globals.3
/usr/share/man/man3/Reply::Plugin::Autocomplete::Keywords.3
/usr/share/man/man3/Reply::Plugin::Autocomplete::Lexicals.3
/usr/share/man/man3/Reply::Plugin::Autocomplete::Methods.3
/usr/share/man/man3/Reply::Plugin::Autocomplete::Packages.3
/usr/share/man/man3/Reply::Plugin::CollapseStack.3
/usr/share/man/man3/Reply::Plugin::Colors.3
/usr/share/man/man3/Reply::Plugin::DataDump.3
/usr/share/man/man3/Reply::Plugin::DataDumper.3
/usr/share/man/man3/Reply::Plugin::DataPrinter.3
/usr/share/man/man3/Reply::Plugin::Editor.3
/usr/share/man/man3/Reply::Plugin::FancyPrompt.3
/usr/share/man/man3/Reply::Plugin::Hints.3
/usr/share/man/man3/Reply::Plugin::Interrupt.3
/usr/share/man/man3/Reply::Plugin::LexicalPersistence.3
/usr/share/man/man3/Reply::Plugin::LoadClass.3
/usr/share/man/man3/Reply::Plugin::Nopaste.3
/usr/share/man/man3/Reply::Plugin::Packages.3
/usr/share/man/man3/Reply::Plugin::Pager.3
/usr/share/man/man3/Reply::Plugin::ReadLine.3
/usr/share/man/man3/Reply::Plugin::ResultCache.3
/usr/share/man/man3/Reply::Plugin::Timer.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Reply/4b8973752a2f9e93d3abb6f77d17bb9385fb9064

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/reply.1

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
