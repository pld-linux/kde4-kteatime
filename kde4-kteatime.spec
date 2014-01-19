#
%define		_state		stable
%define		orgname		kteatime
%define		qtver		4.8.0

Summary:	kteatime
Name:		kde4-%{orgname}
Version:	4.12.1
Release:	1
License:	LGPL
Group:		X11/Applications
Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/%{orgname}-%{version}.tar.xz
# Source0-md5:	ed8d935d5f20ee9b9aa706166ea5c29e
URL:		http://www.kde.org/
BuildRequires:	automoc4 >= 0.9.84
BuildRequires:	cmake >= 2.8.0
BuildRequires:	kde4-kdebase-workspace-devel >= 4.11.4
BuildRequires:	kde4-kdelibs-devel >= %{version}
BuildRequires:	qt4-build >= %{qtver}
BuildRequires:	qt4-qmake >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.600
Obsoletes:	kde4-kdetoys-%{orgname}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
System tray applet that makes sure your tea doesn't get too strong.

%prep
%setup -q -n %{orgname}-%{version}

%build
install -d build
cd build
%cmake \
	.. \

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kteatime
%{_desktopdir}/kde4/kteatime.desktop
%{_datadir}/apps/kteatime
%{_kdedocdir}/en/kteatime
%{_iconsdir}/hicolor/*x*/apps/kteatime.png
%{_iconsdir}/hicolor/scalable/apps/kteatime.svgz
