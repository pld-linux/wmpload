Summary:	PPP network monitor for Window Maker Dock
Summary(pl):	Monitor po��cze� ppp dla Doku Window Makera
Name:		wmpload
Version:	0.9.5
Release:	2
License:	GPL
Group:		X11/Window Managers/Tools
Source0:	http://www.engr.utk.edu/~mdsmith/pload/%{name}-%{version}.tar.gz
Source1:	%{name}.desktop
Patch0:		%{name}-distclean.patch
URL:		http://www.engr.utk.edu/~mdsmith/pload/
BuildRequires:	XFree86-devel
Requires:	ppp
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
wmpload is an PPP monitor for Window Maker Dock. It can dislay totals
and current rates for both inbound and outbound data. wmpload was
designed to be portable to any platform that can run pppd and X11, but
for Linux 2.2 any network interface listed in /proc/net/dev can be
also be monitored.

%description -l pl
wmpload jest monitorem po��cze� PPP dla Doku Window Makera. Posiada
mo�liwo�� wy�wietlania ca�o�ciowych i aktualnych wielko�ci transfer�w
danych zar�wno przychodz�cych jak i wychodz�cych. wmpload zosta�
zaprojektowany w spos�b umo�liwiaj�cy u�ywanie go na ka�dej
platformie, gdzie s� dost�pne X11 i pppd. Dodatkowo dla Linuksa 2.2
istnieje mo�liwo�� monitorowania ka�dego interfejsu sieciowego
obecnego w /proc/net/dev.

%prep
%setup -q
%patch0 -p1

%build
./configure
xmkmf -a
%{__make} CDEBUGFLAGS="%{rpmcflags} -DLINUXPROC"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_applnkdir}/DockApplets

%{__make} install install.man \
	DESTDIR=$RPM_BUILD_ROOT

#install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/DockApplets

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README CHANGES CREDITS
%attr(755,root,root) %{_bindir}/wmpload
%{_mandir}/man1/wmpload.1x*
#%{_applnkdir}/DockApplets/wmpload.desktop
