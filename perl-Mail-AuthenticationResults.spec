%define upstream_name    Mail-AuthenticationResults
%define upstream_version 2.20210112

%{?perl_default_filter}

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    1

Summary:    Class for modelling AuthenticationResults Header parts detected as quoted strings
License:    GPLv1+ or Artistic
Group:      Development/Perl
Url:        http://metacpan.org/release/%{upstream_name}
Source0:    https://cpan.metacpan.org/modules/by-module/Mail/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl-devel
BuildRequires: perl(Carp)
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(JSON)
BuildRequires: perl(Scalar::Util)
BuildRequires: perl(Test::Exception)
BuildRequires: perl(Test::More)
BuildRequires: perl(base)
BuildRequires: perl(lib)
BuildRequires: perl(strict)
BuildRequires: perl(warnings)
BuildArch:  noarch

%description
Object Oriented Authentication-Results email headers.

This parser copes with most styles of Authentication-Results header seen in
the wild, but is not yet fully RFC7601 compliant

Differences from RFC7601

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor

%make_build

%check
%make_build test

%install
%make_install

%files
%doc Changes LICENSE META.yml MYMETA.yml README
%{_mandir}/man3/*
%perl_vendorlib/*
