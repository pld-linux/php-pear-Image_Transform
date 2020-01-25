%define		_status		alpha
%define		_pearname	Image_Transform
Summary:	%{_pearname} - standard interface to manipulate images using different libraries
Summary(pl.UTF-8):	%{_pearname} - standardowy interfejs do manipulacji rysunkami przy użyciu różnych bibliotek
Name:		php-pear-%{_pearname}
Version:	0.9.5
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	b616a0f955686bffec3b2b8d3dc70180
Patch0:		%{name}-IM-patches.patch
URL:		http://pear.php.net/package/Image_Transform/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-12
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php(core) >= 4.3.0
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package was written to provide a simpler and cross-library
interface to doing image transformations and manipulations.

It provides :
 - support for GD, ImageMagick, Imagick and NetPBM,
 - files related functions,
 - addText,
 - Scale (by length, percentage, maximum X/Y),
 - Resize,
 - Rotate (custom angle),
 - Add border (soon),
 - Add shadow (soon).

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Pakiet został zrobiony, aby zapewnić prosty interfejs do różnych
bibliotek pozwalający na transformacje i manipulacje rysunkami.

Dostarcza:
 - wsparcie dla GD, ImageMagick, Imagick oraz NetPBM,
 - funkcje związane z plikami,
 - addText,
 - skalowanie (do wielkości, procentowe, maksymalne X/Y),
 - zmiana wielkości,
 - obroty (różne kąty),
 - dodanie brzegów (wkrótce),
 - dodanie cienia (wkrótce).

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup
cd ./%{php_pear_dir}/Image/Transform
%patch0 -p2
cd -

install -d examples
mv .%{php_pear_dir}/Examples/* examples
mv .%{php_pear_dir}/data/Image_Transform/Examples/* examples
mv .%{php_pear_dir}/data/Image_Transform/imgtests examples
mv .%{php_pear_dir}/imgtests/* examples/imgtests

mv .%{php_pear_dir}/data/Image_Transform/Docs/README .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%doc install.log
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/Image/*.php
%{php_pear_dir}/Image/Transform

%{_examplesdir}/%{name}-%{version}
