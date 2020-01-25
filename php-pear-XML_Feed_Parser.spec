%define		_status		stable
%define		_pearname	XML_Feed_Parser
Summary:	%{_pearname} - unified API for handling RSS and ATOM feeds
Summary(pl.UTF-8):	%{_pearname} - zunifikowane API do obsługi źródeł RSS i ATOM
Name:		php-pear-%{_pearname}
Version:	1.0.5
Release:	3
License:	PHP License
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	8a8a0113a4ecd4d9dd6a6f4ecaa5f0d5
URL:		http://pear.php.net/package/XML_Feed_Parser/
BuildRequires:	php-pear-PEAR >= 1:1.4.0-0.b1
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php(core) >= 5.0
Requires:	php(xml)
Requires:	php-pear
Requires:	php-pear-Log
Suggests:	php-tidy
Obsoletes:	php-pear-XML_Feed_Parser-tests
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# files not distributed (bug reported)
%define _noautoreq pear(XML/Feed/Parser/RSS11.php) pear(XML/Feed/Parser/RSS11Element.php)

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
