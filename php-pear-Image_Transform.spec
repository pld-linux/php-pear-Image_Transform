%include	/usr/lib/rpm/macros.php
%define		_class		Image
%define		_subclass	Transform
%define		_status		alpha
%define		_pearname	%{_class}_%{_subclass}
Summary:	%{_pearname} - standard interface to manipulate images using different libraries
Summary(pl):	%{_pearname} - standardowy interfejs do manipulacji rysunkami przy u¿yciu ró¿nych bibliotek
Name:		php-pear-%{_pearname}
Version:	0.9.0
Release:	2
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	d72d28211e257bdb1b8e25adbbd0aeec
Patch0:		%{name}-IM-patches.patch
URL:		http://pear.php.net/package/Image_Transform/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-12
Requires:	php-common >= 3:4.3.0
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

%description -l pl
Pakiet zosta³ zrobiony, aby zapewniæ prosty interfejs do ró¿nych
bibliotek pozwalaj±cy na transformacje i manipulacje rysunkami.

Dostarcza:
 - wsparcie dla GD, ImageMagick, Imagick oraz NetPBM,
 - funkcje zwi±zane z plikami,
 - addText,
 - skalowanie (do wielko¶ci, procentowe, maksymalne X/Y),
 - zmiana wielko¶ci,
 - obroty (ró¿ne k±ty),
 - dodanie brzegów (wkrótce),
 - dodanie cienia (wkrótce).

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup
cd ./%{php_pear_dir}/%{_class}/%{_subclass}
%patch0 -p2

# kill compat functions and up php version requirement to 4.3.0
# besides, these files are not referenced from this package
cd Driver
rm -f image_type_to_mime_type.php IMAGETYPE.php

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/%{_class}/*.php
%{php_pear_dir}/%{_class}/%{_subclass}
