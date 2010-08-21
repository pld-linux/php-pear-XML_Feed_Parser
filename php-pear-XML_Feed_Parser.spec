%include	/usr/lib/rpm/macros.php
%define		_status		stable
%define		_pearname	XML_Feed_Parser
Summary:	%{_pearname} - unified API for handling RSS and ATOM feeds
Summary(pl.UTF-8):	%{_pearname} - zunifikowane API do obsługi źródeł RSS i ATOM
Name:		php-pear-%{_pearname}
Version:	1.0.3
Release:	3
License:	PHP License
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	35049f24534b72947b5f331252eb8d59
URL:		http://pear.php.net/package/XML_Feed_Parser/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-common >= 4:5.0
Requires:	php-pear
Requires:	php-xml
Suggests:	php-tidy
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# files not distributed (bug reported)
%define _noautoreq 'pear(XML/Feed/Parser/RSS11.php)' 'pear(XML/Feed/Parser/RSS11Element.php)'

%description
XML_Feed_Parser is a parser for (the various) RSS and ATOM format XML
feeds. It attempts to provide a somewhat unified API while still
allowing access to the full details of each feed type.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
XML_Feed_Parser jest parserem dla (różnych) formatów XML źródeł RSS i
ATOM. Klasa ta stara się dostarczyć zunifikowanego API przy
jednoczesnej możliwości dostępu do pełnych informacji dotyczących
każdego źródła.

Ta klasa ma w PEAR status: %{_status}.

%package tests
Summary:	Tests for PEAR::%{_pearname}
Summary(pl.UTF-8):	Testy dla PEAR::%{_pearname}
Group:		Development/Languages/PHP
Requires:	%{name} = %{version}-%{release}
AutoProv:	no
AutoReq:	no

%description tests
Tests for PEAR::%{_pearname}.

%description tests -l pl.UTF-8
Testy dla PEAR::%{_pearname}.

%prep
%pear_package_setup

mv ./%{php_pear_dir}/tests/%{_pearname}/{tests/*,}
rmdir ./%{php_pear_dir}/tests/%{_pearname}/tests

mv .%{php_pear_dir}/data/XML_Feed_Parser/samples examples

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{php_pear_dir},%{_examplesdir}/%{name}-%{version}}
%pear_package_install

cp -a examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/XML/Feed
%{php_pear_dir}/data/XML_Feed_Parser

%{_examplesdir}/%{name}-%{version}

%files tests
%defattr(644,root,root,755)
%{php_pear_dir}/tests/XML_Feed_Parser
